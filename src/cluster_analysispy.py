'''
Para cada grupo, sera que comparten una media de concentraciones similar
Por cada Site id, encontrar su media y mediana
Con cada media y mediana, graficarlos en un box plot por grupo
'''

import pandas as pd
import matplotlib.pyplot as plt

from k_means_v1 import uk_cluter

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

# =================================================================================================


uk_pivot['Mean'] = uk_pivot.mean(axis=1)
uk_pivot['Median'] = uk_pivot.median(axis=1)

uk_cluter = uk_cluter.reset_index()
uk_cluter = uk_cluter.reset_index()

uk_merged = pd.merge(uk_pivot, uk_cluter[["Site_ID", "Cluster"]], on='Site_ID', how='inner')

uk_merged.set_index('Site_ID', inplace=True)

cluster_0 = uk_merged[uk_merged.Cluster == 0]
cluster_1 = uk_merged[uk_merged.Cluster == 1]
cluster_2 = uk_merged[uk_merged.Cluster == 2]

# =================================================================================================

plt.figure(figsize=(8, 6))
plt.boxplot([cluster_0["Mean"], cluster_1["Mean"], cluster_2["Mean"]], labels=['Dataset1', 'Dataset2', 'Dataset3'])
plt.title("Box Plot de Tres Datasets")
plt.ylabel("Valores")
plt.show()

# =================================================================================================

plt.figure(figsize=(8, 6))
plt.boxplot([cluster_0["Median"], cluster_1["Median"], cluster_2["Median"]], labels=['Dataset1', 'Dataset2', 'Dataset3'])
plt.title("Box Plot de Tres Datasets")
plt.ylabel("Valores")
plt.show()