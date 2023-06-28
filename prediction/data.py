import pandas as pd
from math import tan, cos, sin, asin, atan2, radians, degrees

class sampleDataset:
    def __init__(self, path):
        self.data = pd.read_csv(path)
        
     #   self.dataset_initial = data_filtered['mission_time', 'gps_longitude', 'gps_latitude','gps_altitude']
        
       # print(self.data_filtered.head())


    def change_coordinate_system(self):
        R = 6371000 #m
        coordinates = []

        for index, points in self.data.iterrows():
            x = R*cos(radians(points.gps_latitude))*cos(radians(points.gps_longitude))
            y = R*cos(radians(points.gps_latitude))*sin(radians((points.gps_longitude)))
            z = R*sin(radians(points.gps_latitude))
            coordinates.append([x, y, z])

        return coordinates
            
      #  print('x: {} y: {} z: {}'.format(x,y,z))
        


    def return_to_wgs(self, points):
        R = 6371000 #m
        coordinates = []
        for point in points:
            lat = asin(point[2]/R)
            lon = atan2(point[1],point[0])
            coordinates.append([degrees(lat), degrees(lon)])

        return coordinates