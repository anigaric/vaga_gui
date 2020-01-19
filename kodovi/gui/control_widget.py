import sys
import time
from PyQt5.QtWidgets import *

class ControlWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)            #preko parenta pristupam atributima i metodama od VagaWindow
        self.parent = parent


        # ******* Create widgets ******* #
        self.zeroingButton = QPushButton()
        self.zeroingButton.setObjectName("zeroingButton")
        self.zeroingButton.setText("Nuliranje vage")
        self.zeroingButton.clicked.connect(self.zeroingFunc)
        self.zeroingButton.setEnabled(True)

        self.startButton = QPushButton()
        self.startButton.setObjectName("startButton")
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.startFunc)
        self.startButton.setDisabled(True)

        self.stopButton = QPushButton()
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setText("Stop")
        self.stopButton.clicked.connect(self.stopFunc)
        self.stopButton.setDisabled(True)

        self.storeButton = QPushButton()
        self.storeButton.setObjectName("storeButton")
        self.storeButton.setText("Spremi u bazu")
        self.storeButton.clicked.connect(self.storeFunc)
        self.storeButton.setDisabled(True)


        # ****** Create layout and add widgets to it ****** #
        layout = QHBoxLayout(self)
        layout.addWidget(self.zeroingButton)
        layout.addWidget(self.startButton)
        layout.addWidget(self.stopButton)
        layout.addWidget(self.storeButton)

        self.setLayout(layout)

    def zeroingFunc(self):
        self.zeroingButton.setDisabled(True)
        time.sleep(2)                           #koristan rad tj. nuliranje vage
        print("Vaga uspješno nulirana")
        self.startButton.setEnabled(True)       #na kraj funkcije obavezno
        self.zeroingButton.setEnabled(True)

    def startFunc(self):
        self.startButton.setDisabled(True)
        self.stopButton.setEnabled(True)
        print("Mjerenje pokrenuto")
        self.parent.measureData()              #todo dodat varijablu mjerenjeUToku u glavnom programu koja ce citat, pa prema tome postavljat gumbove
        # self.startButton.setEnabled(True)     # todo handlano preko do_after_finish_measure funkcije u vaga_gui
        # self.stopButton.setDisabled(True)

    def stopFunc(self):
        self.stopButton.setDisabled(True)
        self.parent.worker.force_stop = True
        print("Mjerenje zaustavljeno")
        self.startButton.setEnabled(True)
        self.storeButton.setEnabled(True)

    def storeFunc(self):
        self.storeButton.setDisabled(True)
        print("Mjerenje spremljeno u bazu")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ControlWidget()
    win.show()  # prikazuje prozor
    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb
