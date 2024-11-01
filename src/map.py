import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
from k_means import uk_pivot_hifi

# Lista de coordenadas (latitud, longitud)
co = pd.read_csv("../data/monitoring-sites.csv")

coords = pd.DataFrame({"Site_ID":co.site_id,"latitude":co.latitude, "longitude":co.longitude})

# Crear una figura
plt.figure(figsize=(8, 8))

# Crear el mapa con límites ajustados para enfocar Inglaterra
m = Basemap(
    projection='merc', 
    llcrnrlat=54, urcrnrlat=61,   # Limites de latitud
    llcrnrlon=-8, urcrnrlon=2,    # Limites de longitud
    resolution='i'
)
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='lightblue')
m.fillcontinents(color='lightgray', lake_color='lightblue')

# Convertir las coordenadas al sistema de coordenadas del mapa y graficarlas
for index, row in coords.iterrows():
    x, y = m(row['longitude'], row['latitude'])
    m.plot(x, y, 'bo', markersize=8)  # 'bo' indica puntos azules (blue dots)

# Mostrar el mapa
plt.title('Mapa de Coordenadas Geográficas')
plt.show()


group = pd.DataFrame({"Site_ID": uk_pivot_hifi.Site_ID, "latitude":coords.latitude, "longitude":coords.longitude, "Cluster": uk_pivot_hifi.Cluster, })
print(group)
