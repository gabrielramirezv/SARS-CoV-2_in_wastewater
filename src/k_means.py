

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler





def best_K(X):
    Nc = range(1,20)
    kmeans = [KMeans(n_clusters=i) for i in Nc]

    score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]

    plt.plot(Nc,score)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Score')
    plt.title('Elbow Curve')
    plt.show()

uk_data = pd.read_csv("../data/uk_sepa_samples_202312.csv")

# 1. Remove the data with NaN
uk_data = uk_data.dropna()

# 2. Rename the columns
colu = uk_data.columns.str.replace(" ","_") 
uk_data.columns=colu
# 3. Convert the date into integer value
fechas = pd.to_datetime(uk_data.loc[:,"Date/Time"])
time = fechas.astype('int64') // 1e9 # En segundos
# 4. Add a new column to the dataframe
uk_data["Date_epoch"] = time

# 5. Reshape the dataframe in a k-means suitable format
uk_pivot = uk_data.pivot(index='Site_ID', columns='Date_epoch', values='Target_1_Concentration')
uk_pivot_NaN = uk_pivot

# 6. Interpolar
uk_pivot.interpolate(method='linear', axis=1, inplace=True)
# 7. Dos maneras para lidiar con los NaN restantes
# 7.1 Eliminar las columnas con NaN, bajo el argumento de no tener suficiente puntos de comparación
#    con los demás datos. Reduce casi a la mitad las columnas (118 rows x 547 columns)
uk_pivot_hifi = uk_pivot.T.dropna().T
# 7.2 Susituilo con 0, mete información falsa, pero no baja el número de columnas (118 rows x 920 columns)
uk_pivot_raw = uk_pivot.fillna(0)

'''
X = np.array(uk_pivot_hifi)
# best_K(X)

kmeans = KMeans(n_clusters=5).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)

labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
colores=['red','green','blue','cyan','yellow']
asignar=[]
for row in labels:
    asignar.append(colores[row])
 
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000)

f1 = uk_pivot_hifi[1.615162e+09].values
f2 = uk_pivot_hifi[1.696205e+09].values
 
plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()

'''



# Suponiendo que `df_pivot` es tu DataFrame con concentraciones de N1 por fecha y Site_ID como índice

# Estandarización de los datos
scaler = StandardScaler()
data_scaled = scaler.fit_transform(uk_pivot_hifi)

# Definir y ajustar k-means
n_clusters = 3  # Puedes ajustar este número según lo que necesites
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
kmeans.fit(data_scaled)

# Asignar los resultados al DataFrame original
uk_pivot_hifi['Cluster'] = kmeans.labels_

# Imprimir los resultados
print("Clusters asignados a cada Site_ID:")
print(uk_pivot_hifi[['Cluster']])