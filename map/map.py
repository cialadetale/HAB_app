import sys
import io
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
import pandas as pd


class mapWidget(QWidget):
    def __init__(self, *args,**kwargs):
        QWidget.__init__(self, *args,**kwargs)
        
        coordinate = (50.041187, 21.999121)
        self.folium_map = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=13,
        	location=coordinate
        )

    #    self.import_data()
        

        layout = QVBoxLayout()
        self.setLayout(layout)

        data = io.BytesIO()
        self.folium_map.save(data, close_file=False)

        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())
        layout.addWidget(self.webView)

        self.show()

    def update_map(self, data_frame):

        coordinate = (data_frame["gps_latitude"].values[0], data_frame["gps_longitude"].values[0])
        self.folium_map = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=10,
        	location=coordinate
        )


        for _, row in data_frame.iterrows():
            popup_text = 'Mission time: %s s <br>Latitude: %s <br>Longituge: %s <br>Height: %s m' % (row['mission_time'], row["gps_latitude"], row['gps_longitude'], row['gps_altitude'])
            popup = folium.Popup(popup_text, max_width=200,min_width=100)
            folium.CircleMarker(location=[row["gps_latitude"], row['gps_longitude']], radius=3, popup=popup).add_to(self.folium_map)
        
        data = io.BytesIO()
        self.folium_map.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())


    def import_data(self, data_path='sample_data/misja.csv'):
        print('Importing data %s' % data_path)
        data = pd.read_csv(data_path)
      #  data_filtered = data.iloc[9000:720000:100, :]
        data_filtered = data.iloc[0:-1:100, :]
        print(data_filtered.head())
        
        coordinate = (data_filtered["gps_latitude"].values[0], data_filtered["gps_longitude"].values[0])
        self.folium_map = folium.Map(
        	tiles='Stamen Terrain',
        	zoom_start=10,
        	location=coordinate
        )


        for _, row in data_filtered.iterrows():
            popup_text = 'Mission time: %s s <br>Latitude: %s <br>Longituge: %s <br>Height: %s m' % (row['mission_time'], row["gps_latitude"], row['gps_longitude'], row['gps_altitude'])
            popup = folium.Popup(popup_text, max_width=200,min_width=100)
            folium.CircleMarker(location=[row["gps_latitude"], row['gps_longitude']], radius=3, popup=popup).add_to(self.folium_map)
        
        data = io.BytesIO()
        self.folium_map.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())
