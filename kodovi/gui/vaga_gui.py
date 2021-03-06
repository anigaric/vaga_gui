#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys
from port_widget import PortWidget
from control_widget import ControlWidget
from plot_widget import PlotWidget
from rectangle_widget import RectangleWidget
from statistics_widget import StatisticsWidget
from worker import Worker
from DataClasses import MeasurementData


class VagaWindow(QtWidgets.QMainWindow):                  # klasa nasljeduje QMainWindow
    def __init__(self):                         # inicijalizacija klase
        super().__init__()

        # ******* Define class atributes ****** #
        self.selected_port = None
        self.data = MeasurementData()                          # apsolutno svi podaci, polje dictionaryja
        self.threadpool = QtCore.QThreadPool()

        self.initUI()

    def initUI(self):                                            # sve sto zelimo u prozoru
        # ******* Create central Widget ******** #
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")


        # ******* Create widgets ******* #
        self.PortWidget = PortWidget(self)
        self.ControlWidget = ControlWidget(self)
        self.PlotWidget = PlotWidget(self)
        self.RectangleWidget = RectangleWidget(self)
        self.StatisticsWidget = StatisticsWidget(self)


        # ****** Create central layout and add widgets to it ****** #
        centralLayout = QtWidgets.QGridLayout()
        centralLayout.setColumnStretch(0, 1)
        centralLayout.setColumnStretch(1, 3)
        centralLayout.setColumnStretch(2, 2)
        centralLayout.setRowStretch(0, 1)
        centralLayout.setRowStretch(1, 5)           #todo vratit sa 5 na 2

        centralLayout.addWidget(self.PortWidget, 0, 0)
        centralLayout.addWidget(self.ControlWidget, 0, 1)
        centralLayout.addWidget(self.PlotWidget, 1, 1)
        centralLayout.addWidget(self.RectangleWidget, 1, 0)
        centralLayout.addWidget(self.StatisticsWidget, 1, 2)

        # *********** Window properties ************ #
        self.centralwidget.setLayout(centralLayout)
        self.setCentralWidget(self.centralwidget)
        self.setGeometry(200, 100, 900, 500)           #todo maybe vratit sirinu na 1000
        self.setWindowTitle("Biomehanička vaga")

    def measureData(self):
        self.worker = Worker(self.PortWidget.ser)
        self.worker.signals.result.connect(self.print_result)
        self.worker.signals.finished.connect(self.do_after_finish_measure)

        self.threadpool.start(self.worker)

    def print_result(self, res):
        self.data.measurement.append(res)
        self.PlotWidget.animate(self.data.measurement[-1]["CycleID"])
        print(res)

    def do_after_finish_measure(self):
        print("Gotovo cijelo mjerenje od 30 sek")
        self.ControlWidget.startButton.setEnabled(True)
        self.ControlWidget.stopButton.setDisabled(True)
        self.ControlWidget.storeButton.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = VagaWindow()
    win.show()             # prikazuje prozor
    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb
