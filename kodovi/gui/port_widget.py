#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from serial.tools import list_ports
import serial

class PortWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)            #preko parenta pristupam atributima i metodama od VagaWindow
        self.parent = parent

        # ******* Create widgets ******* #
        self.portLabel = QtWidgets.QLabel()
        self.portLabel.setObjectName("portLabel")
        self.portLabel.setText("Odaberi port: ")

        self.portComboBox = QtWidgets.QComboBox()
        self.portComboBox.setObjectName("portComboBox")
        ports = list_ports.comports(include_links=False)
        for port in ports:
            self.portComboBox.addItem(port.device)
        self.portComboBox.activated.connect(self.selectedPort)

        # ****** Create layout and add widgets to it ****** #
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.portLabel)
        layout.addWidget(self.portComboBox)

        self.setLayout(layout)

    # ****** Methods triggered by widget events **** #
    def selectedPort(self):
        self.parent.selected_port = self.portComboBox.currentText()
        print(self.parent.selected_port)

        try:
            self.ser = serial.Serial(self.parent.selected_port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        except (OSError, serial.SerialException):
            print("Port nedostupan")

