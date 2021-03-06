#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class StatisticsWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent

        # ******* Create widgets ******* #
        self.statisticsLabel = QtWidgets.QLabel()
        self.statisticsLabel.setText("Statistika")
        self.statisticsLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.statisticsLabel.setFont(QtGui.QFont('Arial', 12, QtGui.QFont.Bold))

        self.mLeftLabel = QtWidgets.QLabel()
        self.mLeftLabel.setText("m (Lijeva): ")
        self.mLeftLabel.setAlignment(QtCore.Qt.AlignHCenter)

        self.mRightLabel = QtWidgets.QLabel()
        self.mRightLabel.setText("m (Desna): ")
        self.mRightLabel.setAlignment(QtCore.Qt.AlignHCenter)

        self.statDataLeftLabel = QtWidgets.QLabel()
        self.statDataLeftLabel.setText("       Aritm. sredina =  0  kg"
                                       "\n\n  Stand. devijacija =  0  kg"
                                       "\n\n                Max =  0  kg"
                                       "\n\n                Min =  0  kg")
        self.statDataLeftLabel.setAlignment(QtCore.Qt.AlignRight)

        self.statDataRightLabel = QtWidgets.QLabel()
        self.statDataRightLabel.setText("       Aritm. sredina =  0  kg"
                                        "\n\n  Stand. devijacija =  0  kg"
                                        "\n\n                Max =  0  kg"
                                        "\n\n                Min =  0  kg")
        self.statDataRightLabel.setAlignment(QtCore.Qt.AlignRight)

        self.statDataBothLabel = QtWidgets.QLabel()
        self.statDataBothLabel.setText("\nmL : mR = 50 % : 50 %"
                                       "\n\nRazlika = 0 %"
                                       "\n\nmL + mR = 0 kg")
        self.statDataBothLabel.setAlignment(QtCore.Qt.AlignCenter)


        # ****** Create layout and add widgets to it ****** #
        layout = QtWidgets.QGridLayout(self)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 3)                  #todo zamijenit 3 sa necim drugim?
        layout.setRowStretch(3, 3)

        layout.addWidget(self.statisticsLabel, 0, 0, 1, 2)
        layout.addWidget(self.mLeftLabel, 1, 0)
        layout.addWidget(self.mRightLabel, 1, 1)
        layout.addWidget(self.statDataLeftLabel, 2, 0)
        layout.addWidget(self.statDataRightLabel, 2, 1)
        layout.addWidget(self.statDataBothLabel, 3, 0, 1, 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = StatisticsWidget()
    win.show()  # prikazuje prozor
    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb
