'''
NAME
    k_means_v1.py

VERSION
    1.0

AUTHOR
    Santiago Orozco & Gabriel Ramirez

GITHUB
    https://github.com/gabrielramirezv/SARS-CoV-2_in_wastewater/blob/main/src/k_means_v1.py

DESCRIPTION
    Reorganizes the samples of the location, in order to describe them in terms of its Covid 
    concentration across the time. It then cluster the site samples. 

CATEGORY
    location analysis

USAGE
    python k_means_v1.py

ARGUMENTS
    None

SEE ALSO
    map.py
    cluster_analysis.ppy

'''

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# =================================================================================================

# Define Functions

def best_K(X):
    '''
    This function looks for the best cluster number. It graficates the inertia value for n cluster groups. 
    The best cluster number is define as the point where the line curves, called the "elbow point"

    Parameters:
        - X : the input sample data
    '''
    # Start the object for the inertia of each n number of clusters. 
    inertias = []

    # In the following range:
    for i in range (1,15):
        # KMeans object with i clusters is created
        kmeans = KMeans(n_clusters= i)
        # Train the model (with i clusters) with the data in X 
        kmeans.fit(X)
        # Add the calculated inertia to the inertias object
        inertias.append(kmeans.inertia_)

    # Visualize the inertia
    plt.plot(range(1,15),inertias, marker = "o")
    plt.title('Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia/Score')
    plt.show()


# =================================================================================================

# Read the input file from the data directory
uk_data = pd.read_csv("../data/uk_sepa_samples_202312.csv")

# 1. Remove the data with NaN
uk_data = uk_data.dropna()

# 2. Rename the columns for better data processing
colu = uk_data.columns.str.replace(" ","_") 
uk_data.columns=colu
# 3. Convert the date into integer value
fechas = pd.to_datetime(uk_data.loc[:,"Date/Time"])
time = fechas.astype('int64') // 1e9 # In seconds
# 4. Add a new column to the dataframe with the time in seconds
uk_data["Date_epoch"] = time

# 5. Reshape the dataframe in a k-means suitable format
uk_pivot = uk_data.pivot(index='Site_ID', columns='Date_epoch', values='Target_1_Concentration')
uk_pivot_NaN = uk_pivot

# =================================================================================================

# 6. Interpolate, this will fill the NaN values that remains. 
# This NaN values are present because not every location has the same date of sampling
uk_pivot.interpolate(method='linear', axis=1, inplace=True)
# 7. Eliminate columns with NaN, under the argument of not having enough comparison points with the other data. 
# Reduces the columns by almost half (118 rows x 547 columns)
uk_pivot_hifi = uk_pivot.T.dropna().T

# =================================================================================================

X = np.array(uk_pivot_hifi)
# Call the best_K function to determine how many clusters is the best fitting 
# best_K(X)

# Standardization of data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(uk_pivot_hifi)

# Defining and adjusting k-means
n_clusters = 3 
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
kmeans.fit(data_scaled)

# Assign the results
uk_pivot_hifi['Cluster'] = kmeans.labels_

# Print the results
#print("Clusters asignados a cada Site_ID:")
#print(uk_pivot_hifi[['Cluster']])

# The complete, clusterized dataset are kept in other object
uk_cluter = uk_pivot_hifi

