import numpy as np

#Pozycja każdej zmiennej w wektorze stanu
iX = 0
iY = 1
iZ = 2
NUMVARS = iZ + 1

class KalmanFilter:
    def __init__(self, initial_x: float,initial_y: float, initial_z: float, gps_variance, a_matrix) -> None:
        #Stan systemu
        self._x = np.zeros(NUMVARS)
        self._x[iX] = initial_x
        self._x[iY] = initial_y
        self._x[iZ] = initial_z
        self.H = H = np.eye(NUMVARS)
        self.A = a_matrix
        #Kowariancja stanu podana na bazie pierwszych dwóch pomiarów
        self.R = gps_variance
        self._P = np.array([[10, 10, 10],[10, 10, 10], [10, 10, 10]])  # P z dupska, potem się zupdejtuje
        self.Q = np.array([[0.1, 0.1, 0.1],[0.1, 0.1, 0.1], [0.1, 0.1, 0.1]]) 

    def predict(self) -> None:
        new_P = self.A * self._P * np.transpose(self.A) + self.Q
        new_x = self.A * self._x 
        self._P = new_P
        self._x = new_x
        #print(self._P)

    def compute_Kalman_Gain(self):
        #print(np.linalg.det((self.H * self._P * (np.transpose(self.H) + self.R)))) # kuwa osobliwa jest i nie da sie odwrotnej
        self.K = self._P * np.transpose(self.H) * np.linalg.inv(self.H * self._P * (np.transpose(self.H) + self.R))
        #print("kalman gain")
        #print(self.K)
   

    def estimate(self, meas_value):
        new_x = self._x  + self.K * (meas_value - self.H * self._x)
        new_P = self._P - self.K * self.H * self._P
        self._P = new_P
        self._x = new_x

    @property
    def position_x(self) -> float:
        return self._x[iX]

    @property
    def position_y(self) -> float:
       return self._x[iY]

    @property
    def position_z(self) -> float:
       return self._x[iZ]

    @property
    def covariance(self) -> np.array:
        return self._P

    @property
    def mean(self) -> np.array:
        return self._x



