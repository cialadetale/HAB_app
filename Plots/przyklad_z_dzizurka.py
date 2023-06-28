# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import pandas as pd

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import numpy as np
import random
     
class MatplotlibWidget(QMainWindow):
    
    def __init__(self):
        
        QMainWindow . __init__ ( self )

        loadUi("archived_data3.ui",self)

        #self.setWindowTitle("PyQt5 & Matplotlib Example GUI")

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))


    def update_graph(self):


        self.MplWidget.canvas.axes.clear()
        data = pd.read_csv('misja.csv')
        self.MplWidget.canvas.axes.plot(data.mission_time, data.bat_v)
        self.MplWidget.canvas.axes.legend(('battery_voltage'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Battery Voltage')
        self.MplWidget.canvas.draw()
        

app = QApplication([])
window = MatplotlibWidget()
window.show()
window.update_graph()
app.exec_()