from matplotlib import pyplot as plt
import pandas as pd



plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True


data = pd.read_csv('rozladowanie.csv')

#plt.plot(data.mission_time, data.MARG_AHRS_U_a_z)
#plt.plot(data.mission_time, data.temp_1)
plt.plot(data.mission_time, data.bat_v)
plt.show()