# https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/
# https://gis.stackexchange.com/questions/171236/qtdesigner-add-map-canvas-widget
# https://www.youtube.com/watch?v=uzQYfjJezjk

from ast import Pass
from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
#from pyqtgraph import PlotWidget, plot
#import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from map.map import mapWidget
from assets import resources
import pandas as pd
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.data_source = None
        self.toolbar = None
        
        
        
        #Load the UI Page
        uic.loadUi('appUI.ui', self)
        


        self.stackedWidget.setCurrentWidget(self.mainPage)
        self.archiveDataBtn.clicked.connect(self.go_to_archive_data)
        self.liveDataBtn.clicked.connect(self.go_to_live_data)
        self.dataBtn.clicked.connect(self.go_to_table_view)

        self.chartsBtn.clicked.connect(self.go_to_charts_page)
        

        self.returnBtn.clicked.connect(self.go_to_home_page)
        self.uploadBtn.clicked.connect(self.upload_data)
        self.returnBtn_2.clicked.connect(self.go_to_home_page)
        self.returnBtn_3.clicked.connect(self.go_to_archive_data)
        self.returnBtn_4.clicked.connect(self.go_to_archive_data)
        self.returnBtn_6.clicked.connect(self.go_to_archive_data)
        self.returnBtn_7.clicked.connect(self.go_to_archive_data)
        self.returnBtn_5.clicked.connect(self.go_to_charts_page)
        self.rtnBtnPg1.clicked.connect(self.go_to_charts_page)
        self.nxtPgBtn1.clicked.connect(self.go_to_charts_page2)
        self.fwdBtnPg3.clicked.connect(self.go_to_charts_page3)
        self.rtnBtnPg2.clicked.connect(self.go_to_charts_page2)


        #charts
        self.chartsBtn.clicked.connect(self.go_to_charts_page)
        self.pressureButton.clicked.connect(lambda: self.go_to_chart("pressure"))
        self.outsideTempBtn.clicked.connect(lambda: self.go_to_chart("OAT"))
        self.tempBmpBtn.clicked.connect(lambda: self.go_to_chart("bmpTemp"))
        self.difPressureBtn.clicked.connect(lambda: self.go_to_chart("difP"))
        self.hscTempBtn.clicked.connect(lambda: self.go_to_chart("hscTemp"))
        self.windNsBtn.clicked.connect(lambda: self.go_to_chart("ns"))
        self.windWeBtn.clicked.connect(lambda: self.go_to_chart("we"))
        self.axBtn.clicked.connect(lambda: self.go_to_chart("ax"))
        self.ayBtn.clicked.connect(lambda: self.go_to_chart("ay"))
        self.azBtn.clicked.connect(lambda: self.go_to_chart("az"))
        self.angPBtn.clicked.connect(lambda: self.go_to_chart("angp"))
        self.angQBtn.clicked.connect(lambda: self.go_to_chart("angq"))
        self.angRBtn.clicked.connect(lambda: self.go_to_chart("angr"))
        self.hxBtn.clicked.connect(lambda: self.go_to_chart("hx"))
        self.hyBtn.clicked.connect(lambda: self.go_to_chart("hy"))
        self.hzBtn.clicked.connect(lambda: self.go_to_chart("hz"))
        self.radDioBtn.clicked.connect(lambda: self.go_to_chart("dioRad"))
        self.geigBtn.clicked.connect(lambda: self.go_to_chart("geigRad"))
        self.iUseBtn.clicked.connect(lambda: self.go_to_chart("i_use"))
        self.batVBtn.clicked.connect(lambda: self.go_to_chart("bat_v"))
        self.gpsSpeedBtn.clicked.connect(lambda: self.go_to_chart("gps_speed"))
        self.gpsTrackBtn.clicked.connect(lambda: self.go_to_chart("gps_track"))
        self.satNumBtn.clicked.connect(lambda: self.go_to_chart("gps_sats"))
        self.gpsAltBtn.clicked.connect(lambda: self.go_to_chart("gps_altitude"))

    def go_to_archive_data(self):
        self.stackedWidget.setCurrentWidget(self.archiveData)

        

    def go_to_live_data(self):
        self.stackedWidget.setCurrentWidget(self.liveData)
        

    def go_to_home_page(self):
        self.stackedWidget.setCurrentWidget(self.mainPage)

    def go_to_table_view(self):
        self.stackedWidget.setCurrentWidget(self.dataTablePage)

    def go_to_charts_page(self):
        self.stackedWidget.setCurrentWidget(self.dataChartsPage)
        self.removeToolBar(self.toolbar)
        

    def go_to_charts_page2(self):
        self.stackedWidget.setCurrentWidget(self.dataChartsPage2)

    def go_to_charts_page3(self):
        self.stackedWidget.setCurrentWidget(self.dataChartsPage3)

    def upload_data(self):
        file_filter = 'Data File (*.csv)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,         
        )
        
        self.data_source = response[0]

        if self.data_source is not None:
            try:
                self.data = pd.read_csv(self.data_source)
                self.data_filtered = self.data.iloc[9000:720000:300, :]
                self.mapWidget.update_map(self.data_filtered)
                self.filePathLabel.setText(response[0])
                self.uploadBtn.setText('Change file')
                self.write_df_to_qtable(self.data, self.tableWidget)
                self.chart_dict = {
                    "pressure": [self.data.pressure, "Atmospheric Pressure"],
                    "OAT": [self.data.value_1, "Outside Air Temperature"],
                    "bmpTemp": [self.data.temp_1, "Internal Temperature BMP"],
                    "difP": [self.data.value_2, "Differential Pressure"],
                    "hscTemp": [self.data.temp_2, "Internal Temperature HSC"],
                    "ns": [self.data.time_NS, "Wind NS"],
                    "we": [self.data.time_WE, "Wind WE"],
                    "ax": [self.data.MARG_AHRS_U_a_x, "Acceleration X axis"],
                    "ay": [self.data.MARG_AHRS_U_a_y, "Acceleration Y axis"],
                    "az": [self.data.MARG_AHRS_U_a_z, "Acceleration Z axis"],
                    "angp": [self.data.MARG_AHRS_U_P, "Angular rate P"],
                    "angq": [self.data.MARG_AHRS_U_Q, "Angular rate Q"],
                    "angr": [self.data.MARG_AHRS_U_R, "Angular rate R"],
                    "hx": [self.data.MARG_AHRS_U_Hx, "Magnetic field X axis"],
                    "hy": [self.data.MARG_AHRS_U_Hy, "Magnetic field Y axis"],
                    "hz": [self.data.MARG_AHRS_U_Hz, "Magnetic field Z axis"],
                    "dioRad": [self.data.dio_label, "Cosmic radiatione - diode measurement"],
                    "geigRad": [self.data.geig_label, "Cosmic radiatione - Geiger Tube measurement"],
                    "i_use": [self.data.i_use, "Currant usage"],
                    "bat_v": [self.data.bat_v, "Battery voltage"],
                    "gps_altitude": [self.data.gps_altitude, "GPS altitude"],
                    "gps_speed": [self.data.gps_speed_kph, "GPS speed"],
                    "gps_track": [self.data.gps_track, "GPS track"],
                    "gps_sats": [self.data.sat_num, "GPS satellite number"]
                }
            except:
                print('Nie udało się otworzyć pliku')
        


    #chart page

    def go_to_chart(self, picklock_word):
        try:
            self.toolbar = NavigationToolbar(self.pressurePlot.canvas, self)
            self.stackedWidget.setCurrentWidget(self.pressureChartPage)
            self.addToolBar(0x1, self.toolbar)
            self.pressurePlot.canvas.axes.clear()
            self.pressurePlot.canvas.axes.plot(self.data.mission_time, self.chart_dict[picklock_word][0])
            self.pressurePlot.canvas.axes.legend((''),loc='upper right')
            self.pressurePlot.canvas.axes.set_title(self.chart_dict[picklock_word][1])
            self.pressurePlot.canvas.draw()
            
            
            
        except Exception as ee:
            print(ee)

    

    def update_data_table(self, data_frame):
        pass

    @staticmethod
    def write_df_to_qtable(df,table):
        df = df[['mission_time', 'pressure', 'temp_1', 'sat_num', 'gps_latitude', 'gps_longitude', 'gps_speed_kph', 'gps_altitude', 'gps_track', 'bat_v', 'i_use']]
  #      headers = list(df)
        table.setRowCount(df.shape[0])
  #      table.setColumnCount(df.shape[1])
  #      table.setHorizontalHeaderLabels(headers)        

    # getting data from df is computationally costly so convert it to array first
        df_array = df.values
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(round(df_array[row,col], 2))))




class ArchiveDataWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(ArchiveDataWindow, self).__init__(*args, **kwargs)
        uic.loadUi('archiveData.ui', self)
        
    


def main():
    app = QtWidgets.QApplication(sys.argv)
   
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()