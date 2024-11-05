import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# =================================================================================================

def best_K(X):
    Nc = range(1,20)
    kmeans = [KMeans(n_clusters=i) for i in Nc]

    inertias = []

    for i in range (1,15):
        kmeans = KMeans(n_clusters= i)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)

    plt.plot(range(1,15),inertias, marker = "o")
    plt.title('Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia/Score')
    plt.show()


# =================================================================================================

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

# =================================================================================================

# Quiza la razon, de que no haya una separacion aparente sea por el muestreo. K-means en realidad 
# esta viendo las diferencias basadas en otras caracteristicas como patrones en que dias esta la 
# muestra

# 6. Interpolar
# uk_pivot.interpolate(method='linear', axis=1, inplace=True)

# 7 Eliminar las columnas con NaN
uk_pivot_hifi = uk_pivot.T.dropna().T

print(uk_pivot_hifi) # ==> No hay ninguna fecha en donde se haya muestreado en todos los lugares 

'''
# =================================================================================================

X = np.array(uk_pivot_hifi)
# best_K(X)

# Estandarizacion de los datos
scaler = StandardScaler()
data_scaled = scaler.fit_transform(uk_pivot_hifi)

# Definir y ajustar k-means
n_clusters = 3 
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
kmeans.fit(data_scaled)

# Asignar los resultados
uk_pivot_hifi['Cluster'] = kmeans.labels_

# Imprimir los resultados
print("Clusters asignados a cada Site_ID:")
print(uk_pivot_hifi[['Cluster']])

uk_cluter = uk_pivot_hifi
'''