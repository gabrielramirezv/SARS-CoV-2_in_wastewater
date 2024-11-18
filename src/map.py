'''
NAME
    map

VERSION
    1.0

AUTHOR
    Santiago Orozco & Gabriel Ramirez

GITHUB
    https://github.com/gabrielramirezv/SARS-CoV-2_in_wastewater/blob/main/src/map.py

DESCRIPTION
    Plot locations in a map by clusters

CATEGORY
    location analysis

USAGE
    python map.py

ARGUMENTS
    None

SEE ALSO
    k_means
    cluster_analysis

'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from k_means_v1 import uk_cluter
from mpl_toolkits.basemap import Basemap

# ============================================================================

# Read coordinates list
co = pd.read_csv("../data/monitoring-sites.csv")

# Generate the cluster by location
uk_cluter = uk_cluter.reset_index()

# Merge coordinates
coords_merged = pd.merge(uk_cluter[["Site_ID", "Cluster"]], 
                         co[["site_id", "latitude", "longitude"]], 
                         left_on='Site_ID', 
                         right_on='site_id', 
                         how='inner')

# Get each cluster
cluster_0 = coords_merged[coords_merged.Cluster == 0]
cluster_1 = coords_merged[coords_merged.Cluster == 1]
cluster_2 = coords_merged[coords_merged.Cluster == 2]

# ============================================================================

plt.figure(figsize=(8, 8))

# Create the map with UK coordinates
m = Basemap(projection ='merc', 
            llcrnrlat = 54, urcrnrlat=61, 
            llcrnrlon=-8, urcrnrlon=2, 
            resolution='i')

# Define map characteristics
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='lightblue')
m.fillcontinents(color='lightgray', lake_color='lightblue')

# Convert cluster 0 coordinates to map coordinates system and plot them
for index, row in cluster_0.iterrows():
    x, y = m(row['longitude'], row['latitude'])
    m.plot(x, y, 'bo', markersize=4) 

# Convert cluster 1 coordinates to map coordinates system and plot them
for index, row in cluster_1.iterrows():
    x, y = m(row['longitude'], row['latitude'])
    m.plot(x, y, 'go', markersize=4) 

# Convert cluster 2 coordinates to map coordinates system and plot them
for index, row in cluster_2.iterrows():
    x, y = m(row['longitude'], row['latitude'])
    m.plot(x, y, 'ro', markersize=4) 

# Show plot
plt.title('Geographic Coordinates Map')
plt.show()
