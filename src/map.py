import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.basemap import Basemap

from k_means_v1 import uk_cluter

# =================================================================================================


# Lista de coordenadas (latitud, longitud)
co = pd.read_csv("../data/monitoring-sites.csv")

uk_cluter = uk_cluter.reset_index()

coords_merged = pd.merge(uk_cluter[["Site_ID", "Cluster"]], co[["site_id", "latitude", "longitude"]], left_on='Site_ID', right_on='site_id', how='inner')


cluster_0 = coords_merged[coords_merged.Cluster == 0]

cluster_1 = coords_merged[coords_merged.Cluster == 1]

cluster_2 = coords_merged[coords_merged.Cluster == 2]

# =================================================================================================

plt.figure(figsize=(8, 8))

# Crear el mapa con limites ajustados para enfocar Inglaterra
m = Basemap(
    projection='merc', 
    llcrnrlat=54, urcrnrlat=61,   # Latitud
    llcrnrlon=-8, urcrnrlon=2,    #  longitud
    resolution='i'
)
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='lightblue')
m.fillcontinents(color='lightgray', lake_color='lightblue')

# Convertir las coordenadas al sistema de coordenadas del mapa y graficarlas
for index, row in cluster_0.iterrows():
    x, y = m(row['longitude'], row['latitude'])
    m.plot(x, y, 'bo', markersize=4) 

for index, row in cluster_1.iterrows():
    x, y = m(row['longitude'], row['latitude'])
    m.plot(x, y, 'go', markersize=4) 

for index, row in cluster_2.iterrows():
    x, y = m(row['longitude'], row['latitude'])
    m.plot(x, y, 'ro', markersize=4) 

# Mostrar el mapa
plt.title('Mapa de Coordenadas Geograficas')
plt.show()
