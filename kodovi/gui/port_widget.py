from PyQt5.QtWidgets import *
from serial.tools import list_ports

class PortWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)            #preko parenta pristupam atributima i metodama od VagaWindow
        self.parent = parent

        # ******* Create widgets ******* #
        self.portLabel = QLabel()
        self.portLabel.setObjectName("portLabel")
        self.portLabel.setText("Odaberi port: ")

        self.portComboBox = QComboBox()
        self.portComboBox.setObjectName("portComboBox")
        ports = list_ports.comports(include_links=False)
        for port in ports:
            self.portComboBox.addItem(port.device)
        self.portComboBox.activated.connect(self.selectedPort)

        # ****** Create layout and add widgets to it ****** #
        layout = QHBoxLayout(self)
        layout.addWidget(self.portLabel)
        layout.addWidget(self.portComboBox)

        self.setLayout(layout)

    # ****** Methods triggered by widget events **** #
    def selectedPort(self):
        self.parent.selected_port = self.portComboBox.currentText()
        print(self.parent.selected_port)
