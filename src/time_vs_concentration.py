'''
NAME
    time_vs_concentration

VERSION
    1.0

AUTHOR
    Santiago Orozco & Gabriel Ramirez

GITHUB
    https://github.com/gabrielramirezv/SARS-CoV-2_in_wastewater/blob/main/src/time_vs_concentration.py

DESCRIPTION
    Plots SARS-CoV-2 elements found in wastewater throughout months

CATEGORY
    time analysis

USAGE
    python src/time_vs_concentration.py

ARGUMENTS
    None

SEE ALSO
    k_means_v1

'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================================

# Read dataset
uk_data = pd.read_csv("../data/uk_sepa_samples_202312.csv")

# Remove the data with NaN
uk_data = uk_data.dropna()

# Rename the columns
uk_data.columns = uk_data.columns.str.replace(" ","_") 
uk_data.columns = uk_data.columns.str.replace("/","_")

# Convert the date into integer value
time = pd.to_datetime(uk_data.loc[:,"Date_Time"])

# Add a new column to the dataframe
uk_data["Date_epoch"] = time

# Reshape the dataframe in a k-means suitable format
uk_pivot = uk_data.pivot(index='Site_ID', 
                         columns='Date_epoch', 
                         values='Target_1_Concentration') 

# ============================================================================

# Create data frame with statistics
statistics = pd.DataFrame({
    'Mean': uk_pivot.mean(),
    'Median': uk_pivot.median()
})
statistics = statistics.reset_index()

# Plot by concentrations
plt.plot(statistics.Date_epoch, statistics.Mean)
plt.plot(statistics.Date_epoch, statistics.Median)
plt.title('Time vs Concentration')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend(["Mean", "Median"])
plt.savefig("../results/time_vs_concentration.png")
