'''
NAME
    cluster_analysis

VERSION
    1.0

AUTHOR
    Santiago Orozco & Gabriel Ramirez

GITHUB
    https://github.com/gabrielramirezv/SARS-CoV-2_in_wastewater/blob/main/src/cluster_analysis.py

DESCRIPTION
    Calculates mean and median for each site ID, and then plots them in
    a box plot by group

CATEGORY
    location analysis

USAGE
    python cluster_analysis.py

ARGUMENTS
    None

SEE ALSO
    k_means
    map

'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from k_means_v1 import uk_cluter

# ============================================================================

# Read data from data file
uk_data = pd.read_csv("../data/uk_sepa_samples_202312.csv")

# Remove the data with NaN
uk_data = uk_data.dropna()

# Rename the columns
colu = uk_data.columns.str.replace(" ","_") 
uk_data.columns=colu

# Convert the date into integer value
fechas = pd.to_datetime(uk_data.loc[:,"Date/Time"])
time = fechas.astype('int64') // 1e9 # Seconds

# Add a new column to the dataframe
uk_data["Date_epoch"] = time

# Reshape the dataframe in a k-means suitable format
uk_pivot = uk_data.pivot(index='Site_ID', 
                         columns='Date_epoch', 
                         values='Target_1_Concentration')

# ============================================================================

# Calculate mean and median
uk_pivot['Mean'] = uk_pivot.mean(axis=1)
uk_pivot['Median'] = uk_pivot.median(axis=1)

# Reset index in cluster
uk_cluter = uk_cluter.reset_index()

# Merge pivot and cluster
uk_merged = pd.merge(uk_pivot, 
                     uk_cluter[["Site_ID", "Cluster"]], 
                     on='Site_ID', 
                     how='inner')

# Set indexes
uk_merged.set_index('Site_ID', inplace=True)

# Separate clusters
cluster_0 = uk_merged[uk_merged.Cluster == 0]
cluster_1 = uk_merged[uk_merged.Cluster == 1]
cluster_2 = uk_merged[uk_merged.Cluster == 2]

# ============================================================================

# Generate plot by mean
plt.figure(figsize=(8, 6))
plt.boxplot([cluster_0["Mean"], cluster_1["Mean"], cluster_2["Mean"]], 
             labels=['Dataset1', 'Dataset2', 'Dataset3'])
plt.title("Three Datasets Boxplot")
plt.ylabel("Values")
plt.savefig("../results/cluster_analysis_mean.png")

# ============================================================================

# Generate plot by median
plt.figure(figsize=(8, 6))
plt.boxplot([cluster_0["Median"], cluster_1["Median"], cluster_2["Median"]], 
            labels=['Dataset1', 'Dataset2', 'Dataset3'])
plt.title("Three Datasets Boxplot")
plt.ylabel("Values")
plt.savefig("../results/cluster_analysis_median.png")
