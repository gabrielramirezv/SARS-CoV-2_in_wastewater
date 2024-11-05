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

Mean = uk_pivot.mean()
Median = uk_pivot.median()


estadisticas = pd.DataFrame({
    'Mean': Mean,
    'Median': Median
})
estadisticas = estadisticas.reset_index()

plt.plot(estadisticas.Date_epoch, estadisticas.Mean)
plt.title('Time vs Concentration')
plt.xlabel('Time')
plt.ylabel('Mean concentration')
plt.show()

plt.plot(estadisticas.Date_epoch, estadisticas.Median)
plt.title('Time vs Concentration')
plt.xlabel('Time')
plt.ylabel('Median concentration')
plt.show()