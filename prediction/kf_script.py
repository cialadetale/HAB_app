from ctypes import sizeof
import numpy as np
from kf import KalmanFilter
from data import sampleDataset
import matplotlib.pyplot as plt
from math import cos

#kf = KalmanFilter(initial_x=0.0,initial_y=0.0, initial_z=0.0, gps_variance=1.0)

dane_misja = sampleDataset("misja.csv")

x_y_z_dane = dane_misja.change_coordinate_system()


# sigma_x2 = 0 # bo na początku pozycja stała 
# E_xy = ((x_y_z_dane[0][0] * x_y_z_dane[0][1])+(x_y_z_dane[1][0] * x_y_z_dane[1][1]))/2
# E_x = (x_y_z_dane[0][0]+x_y_z_dane[0][0])/2
# E_y = (x_y_z_dane[0][1]+x_y_z_dane[1][1])/2
# sigma_xy = E_xy - (E_x * E_y)
# E_xz = ((x_y_z_dane[0][0] * x_y_z_dane[0][2])+(x_y_z_dane[1][0] * x_y_z_dane[1][2]))/2
# E_z = (x_y_z_dane[0][2]+x_y_z_dane[1][2])/2
# sigma_xz = E_xz - (E_x * E_z)
# E_yz = ((x_y_z_dane[0][1] * x_y_z_dane[0][2])+(x_y_z_dane[1][1] * x_y_z_dane[1][2]))/2
# sigma_yz = E_yz - (E_y * E_z)
# sigma_y2 = 0 # bo na początku pozycja stała
# sigma_z2 = 0 # bo na początku pozycja stała
# #kuwa wszystkie są zero



# licze parametry statystyczne na bazie zestawu danych
dane_uczace = x_y_z_dane[1:10:]
suma_x = 0
suma_y = 0
suma_z = 0
suma_xy = 0
suma_xz = 0
suma_yz = 0

for i in range(len(dane_uczace)):
    suma_x += dane_uczace[i][0]
    suma_y += dane_uczace[i][1]
    suma_z += dane_uczace[i][2]
    suma_xy += dane_uczace[i][0] * dane_uczace[i][1]
    suma_xz += dane_uczace[i][0] * dane_uczace[i][2]
    suma_yz += dane_uczace[i][1] * dane_uczace[i][2]

mean_x = suma_x/len(dane_uczace)
mean_y = suma_y/len(dane_uczace)
mean_z = suma_z/len(dane_uczace)
mean_xy = suma_xy/len(dane_uczace)
mean_xz = suma_xz/len(dane_uczace)
mean_yz = suma_yz/len(dane_uczace)

suma_sigma_x2 =0
suma_sigma_y2 =0
suma_sigma_z2 =0

for i in range(len(dane_uczace)):
    suma_sigma_x2 += (dane_uczace[i][0]-mean_x)**2
    suma_sigma_y2 += (dane_uczace[i][1]-mean_y)**2
    suma_sigma_z2 += (dane_uczace[i][2]-mean_z)**2

sigma_x2 = suma_sigma_x2/len(dane_uczace)
sigma_y2 = suma_sigma_y2/len(dane_uczace)
sigma_z2 = suma_sigma_z2/len(dane_uczace)
sigma_xy = mean_xy - (mean_x * mean_y)
sigma_xz = mean_xz - (mean_x * mean_z)
sigma_yz = mean_yz - (mean_y * mean_z)

R = np.array([[sigma_x2, sigma_xy, sigma_xz], [sigma_xy, sigma_y2, sigma_yz], [sigma_xz, sigma_yz, sigma_z2]])
A = np.eye(3)

x_y_z_dane = x_y_z_dane[4600:5000] # start end step


kf = KalmanFilter(x_y_z_dane[0][0], x_y_z_dane[0][1], x_y_z_dane[0][2], R, A)

dane_filtrowane = (x_y_z_dane[0:1])
#czas_filtrowany = [0.0, 0.1, 0.2]





for i in range(len(x_y_z_dane)):
    kf.predict()
    dane_filtrowane.append([kf._x[0][0],kf._x[1][1],kf._x[2][2]])
    #print(dane_filtrowane)
    #czas = czas_filtrowany[i+2] + 0.05
    #czas_filtrowany.append(czas)
    kf.compute_Kalman_Gain()
    measured_values = np.array([[x_y_z_dane[i][0],0,0],[0,x_y_z_dane[i][1],0],[0,0,x_y_z_dane[i][2]]])
    kf.estimate(measured_values)
    #print(measured_values)
    dane_filtrowane.append([kf._x[0][0],kf._x[1][1],kf._x[2][2]])
    #print(dane_filtrowane)
    #czas = czas_filtrowany[i+2] + 0.05
    #czas_filtrowany.append(czas)
    #break
    
    
#print(dane_filtrowane[0])
koordynaty_filtrowane = dane_misja.return_to_wgs(dane_filtrowane)

plt.subplot(2,1,1)
plt.title('Position lat data')
plt.plot( dane_misja.data.gps_latitude[4600:5000])
plt.plot(dane_misja.data.gps_longitude[4600:5000])
plt.subplot(2,1,2)
plt.title('Position lat filtered')
plt.plot(koordynaty_filtrowane)
plt.show()
    


# real_x = 0
# meas_variance = 0.5**2
# real_y = 0
# real_z = 0

# mus = []
# covs = []

# real_xs = []
# real_ys = []
# real_zs = []

# for step in range(NUM_STEPS):

#     if step>100 and step<600:
#         real_x += cos(step*0.017)

#     if step<100:
#         real_y += 1+cos(step*0.017)

#     if step<500:
#         real_z += 5

#     covs.append(kf.covariance)
#     mus.append(kf.mean)

#     real_xs.append(real_x)
#     real_ys.append(real_y)
#     real_zs.append(real_z)

#     kf.predict(dt = DT)
#     if step != 0 and step % MEAS_EVERY_STEPS == 0:
#         meas_x = real_x+np.random.rand()*np.sqrt(meas_variance)
#         meas_y = real_y+np.random.rand()*np.sqrt(meas_variance)
#         meas_z = real_z+np.random.rand()*np.sqrt(meas_variance)
#         kf.update(meas_value=[meas_x, meas_y, meas_z], meas_variance=meas_variance)



# plt.subplot(3,1,1)
# plt.title('Position x')
# plt.plot([mu[0] for mu in mus], 'b')
# plt.plot(real_xs, 'g')
# plt.plot([mu[0] - 2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs)], 'r--')
# plt.plot([mu[0] + 2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs)], 'r--')

# plt.subplot(3,1,2)
# plt.title('Position y')
# plt.plot([mu[1] for mu in mus], 'b')
# plt.plot(real_ys, 'g')
# plt.plot([mu[1] - 2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs)], 'r--')
# plt.plot([mu[1] + 2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs)], 'r--')

# plt.subplot(3,1,3)
# plt.title('Position z')
# plt.plot([mu[2] for mu in mus], 'b')
# plt.plot(real_zs, 'g')
# plt.plot([mu[2] - 2*np.sqrt(cov[2,2]) for mu,cov in zip(mus,covs)], 'r--')
# plt.plot([mu[2] + 2*np.sqrt(cov[2,2]) for mu,cov in zip(mus,covs)], 'r--')

# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot3D([mu[0] for mu in mus], [mu[1] for mu in mus], [mu[2] for mu in mus], 'b')
# ax.scatter([mu[0] for mu in mus], [mu[1] for mu in mus], [mu[2] for mu in mus], 'b')
# ax.plot3D(real_xs, real_ys, real_zs, 'g')
# plt.show()

# plt.ginput(1)