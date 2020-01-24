#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QtWidgets.QApplication
import os
from random import randint

class GraphWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)            #preko parenta pristupam atributima i metodama od VagaWindow
        self.parent = parent

        self.graphWidget = pg.PlotWidget()

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.graphWidget)
        self.setLayout(layout)

        self.x = [0] # list(range(30))  # 30 time points
        self.y = []

        print(self.x)
        print(self.y)

        # hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle("Your Title Here")
        # Add Axis Labels
        self.graphWidget.setLabel('left', 'Temperature (°C)', color='red', size=30)
        self.graphWidget.setLabel('bottom', 'Hour (H)', color='red', size=30)
        # Add legend
        # self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set Range
        self.graphWidget.setXRange(0, 31, padding=0)
        self.graphWidget.setYRange(0, 151, padding=0)

        # pen = pg.mkPen(color=(255, 0, 0))
        # self.graphWidget.plot(self.x, self.y, name="Sensor 1", symbol='+', symbolSize=10, symbolBrush=('b'))

        # ... init continued ...
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y.append(randint(0, 100))  # Add a new random value.

        # self.data_line.setData(self.x, self.y)  # Update the data.
        self.graphWidget.plot(self.x, self.y)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = GraphWidget()
    win.show()  # prikazuje prozor
    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb
