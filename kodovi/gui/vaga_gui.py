from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import time
import serial
from port_widget import PortWidget
from control_widget import ControlWidget
from plot_widget import PlotWidget
from rectangle_widget import RectangleWidget


class VagaWindow(QMainWindow):                  # klasa nasljeduje QMainWindow
    def __init__(self):                         # inicijalizacija klase
        super().__init__()

        # ******* Define class atributes ****** #
        self.selected_port = 'COM10'           # todo treba ic None, pa povezat s ostalim

        self.initUI()

    def initUI(self):                                            # sve sto zelimo u prozoru
        # ******* Create central Widget ******** #
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")


        # ******* Create widgets ******* #
        self.PortWidget = PortWidget(self)
        self.ControlWidget = ControlWidget(self)
        #self.PlotWidget = PlotWidget(self)
        self.RectangleWidget = RectangleWidget(self)


        # ****** Create central layout and add widgets to it ****** #
        centralLayout = QGridLayout()
        centralLayout.setColumnStretch(0, 1)
        centralLayout.setColumnStretch(1, 3)
        centralLayout.setColumnStretch(2, 2)
        centralLayout.setRowStretch(0, 1)
        centralLayout.setRowStretch(1, 2)

        centralLayout.addWidget(self.PortWidget, 0, 0)
        centralLayout.addWidget(self.ControlWidget, 0, 1)
        #centralLayout.addWidget(self.PlotWidget, 1, 1)
        centralLayout.addWidget(self.RectangleWidget, 1, 0)

        # *********** Window properties ************ #
        self.centralwidget.setLayout(centralLayout)
        self.setCentralWidget(self.centralwidget)
        self.setGeometry(200, 100, 800, 500)
        self.setWindowTitle("Biomehanička vaga")

    def measureData(self):
        start = 0
        header = []
        default_header = ['17', 'a3', '91', 'f4']
        package = dict()  # lista u kojoj ce bit jedan paket, pojedinacno ce se prepisivat i zapisivat u datoteku
        legs = ['L1', 'R1', 'L2', 'R2', 'L3', 'R3', 'L4', 'R4', 'L5', 'R5', 'L6', 'R6', 'L7', 'R7', 'L8', 'R8', 'L9',
                'R9',
                'L10', 'R10']

        ser = serial.Serial(self.selected_port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

        try:
            start_time = time.time()
            elapsed_time = 0
            while elapsed_time < 30:  # mjerenje(citanje podataka) traje 30 sekundi
                incoming_hex = ser.read().hex()
                print(incoming_hex)

                header.append(incoming_hex)
                if len(header) >= 4:
                    if header == default_header:
                        start = 1
                        print("Header arrived!")
                    else:
                        header.pop(0)

                if start == 1:
                    incoming_byte = ser.read()
                    package['ID'] = int.from_bytes(incoming_byte, "little", signed=True)  # fiksno 0x01
                    # print(package)
                    incoming_byte = ser.read()
                    package["CycleID"] = int.from_bytes(incoming_byte, "little", signed=False)  # broj paketa - uint8
                    # print(package)
                    incoming_byte = ser.read()
                    package["length"] = int.from_bytes(incoming_byte, "little", signed=True)  # fiksno 85
                    # print(package)

                    for x in range(len(legs)):
                        incoming_byte = ser.read(4)
                        package[legs[x]] = int.from_bytes(incoming_byte, "little", signed=True)
                        print(package)

                    incoming_byte = ser.read(2)
                    package["ANGLE_L"] = int.from_bytes(incoming_byte, "little", signed=True)
                    # print(package)
                    incoming_byte = ser.read(2)
                    package["ANGLE_R"] = int.from_bytes(incoming_byte, "little", signed=True)
                    # print(package)
                    incoming_byte = ser.read()
                    package["DIST"] = int.from_bytes(incoming_byte, "little", signed=False)  # udaljenost - uint8 - OK
                    # print(package)
                    incoming_byte = ser.read(1)
                    package["Checksum"] = int.from_bytes(incoming_byte, "little", signed=True)
                    print(package)

                    start = 0
                    header.clear()
                    print("ciscenjeeeeeeeeeeeeee")

                elapsed_time = time.time() - start_time

        except NameError:
            print("-------- Komunikacija nije uspostavljena jer je port trenutno zauzet! --------")

        try:
            ser.close()
        except NameError:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = VagaWindow()
    win.show()             # prikazuje prozor
    win.measureData()
    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb
