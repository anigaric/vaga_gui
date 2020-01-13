import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class StatisticsWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent

        # ******* Create widgets ******* #
        self.statisticsLabel = QLabel()
        self.statisticsLabel.setText("Statistika")
        self.statisticsLabel.setAlignment(Qt.AlignHCenter)
        self.statisticsLabel.setFont(QFont('Arial', 12, QFont.Bold))

        self.mLeftLabel = QLabel()
        self.mLeftLabel.setText("m (Lijeva): ")
        self.mLeftLabel.setAlignment(Qt.AlignHCenter)

        self.mRightLabel = QLabel()
        self.mRightLabel.setText("m (Desna): ")
        self.mRightLabel.setAlignment(Qt.AlignHCenter)

        self.statDataLeftLabel = QLabel()
        self.statDataLeftLabel.setText("       Aritm. sredina =  0  kg"
                                       "\n  Stand. devijacija =  0  kg"
                                       "\n                Max =  0  kg"
                                       "\n                Min =  0  kg")
        self.statDataLeftLabel.setAlignment(Qt.AlignRight)

        self.statDataRightLabel = QLabel()
        self.statDataRightLabel.setText("       Aritm. sredina =  0  kg"
                                        "\n  Stand. devijacija =  0  kg"
                                        "\n                Max =  0  kg"
                                        "\n                Min =  0  kg")
        self.statDataRightLabel.setAlignment(Qt.AlignRight)

        self.statDataBothLabel = QLabel()
        self.statDataBothLabel.setText("mL : mR = 50 % : 50 %"
                                       "\nRazlika = 0 %"
                                       "\nmL + mR = 0 kg")
        self.statDataBothLabel.setAlignment(Qt.AlignCenter)


        # ****** Create layout and add widgets to it ****** #
        layout = QGridLayout(self)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)

        layout.addWidget(self.statisticsLabel, 0, 0, 1, 2)
        layout.addWidget(self.mLeftLabel, 1, 0)
        layout.addWidget(self.mRightLabel, 1, 1)
        layout.addWidget(self.statDataLeftLabel, 2, 0)
        layout.addWidget(self.statDataRightLabel, 2, 1)
        layout.addWidget(self.statDataBothLabel, 3, 0, 1, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StatisticsWidget()
    win.show()  # prikazuje prozor
    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb