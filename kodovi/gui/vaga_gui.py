from PyQt5 import QtWidgets
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import *
import sys
from port_widget import PortWidget
from control_widget import ControlWidget
from plot_widget import PlotWidget
from rectangle_widget import RectangleWidget
from statistics_widget import StatisticsWidget
from worker import Worker
from DataClasses import MeasurementData


class VagaWindow(QMainWindow):                  # klasa nasljeduje QMainWindow
    def __init__(self):                         # inicijalizacija klase
        super().__init__()

        # ******* Define class atributes ****** #
        self.selected_port = None
        self.data = MeasurementData()                          # apsolutno svi podaci, polje dictionaryja
        self.threadpool = QThreadPool()

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
        centralLayout = QGridLayout()
        centralLayout.setColumnStretch(0, 1)
        centralLayout.setColumnStretch(1, 3)
        centralLayout.setColumnStretch(2, 2)
        centralLayout.setRowStretch(0, 1)
        centralLayout.setRowStretch(1, 2)

        centralLayout.addWidget(self.PortWidget, 0, 0)
        centralLayout.addWidget(self.ControlWidget, 0, 1)
        centralLayout.addWidget(self.PlotWidget, 1, 1)
        centralLayout.addWidget(self.RectangleWidget, 1, 0)
        centralLayout.addWidget(self.StatisticsWidget, 1, 2)

        # *********** Window properties ************ #
        self.centralwidget.setLayout(centralLayout)
        self.setCentralWidget(self.centralwidget)
        self.setGeometry(200, 100, 800, 500)
        self.setWindowTitle("Biomehanička vaga")

    def measureData(self):
        worker = Worker(self.PortWidget.ser)
        worker.signals.result.connect(self.print_result)

        self.threadpool.start(worker)

    def print_result(self, res):
        self.data.measurement.append(res)
        self.PlotWidget.animate(self.data.measurement[-1]["CycleID"])
        print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = VagaWindow()
    win.show()             # prikazuje prozor
    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb
