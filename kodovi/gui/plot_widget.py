#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import animation
from matplotlib.figure import Figure

class PlotWidget(QtWidgets.QWidget):  # or QtWidgets.QWidget ??? or QDialog as it was default

    def __init__(self, parent=None):
        super().__init__(parent)  # preko parenta pristupam atributima i metodama od VagaWindow
        self.parent = parent

        self.fig = Figure(figsize=(6, 5), dpi=100)
        self.fig.suptitle("Real-time prikaz podataka")
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)


        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.setup()

    def setup(self):
        self.ax = self.fig.add_subplot(111)  # create an axis
        self.xs = []
        self.ax.set_xlim(0, 30)
        self.ax.set_ylim(0, 150)            #todo ta potrebe testiranja staviti 255
        self.ys = []
        self.i = 0

       # self.anim = animation.FuncAnimation(self.fig, self.animate, fargs=(self.ys), interval=500)
        self.canvas.draw()

    def animate(self, ys):
        self.i = self.i + 1

        self.xs.append(self.i)
        self.ys.append(ys)

        self.xs = self.xs[-30:]
        self.ys = self.ys[-30:]

        self.ax.clear()
        self.ax.plot(self.xs, self.ys, 'ro')
        self.ax.grid(True)

        self.ax.set_xlim(max(0, self.i-30), max(30, self.i + 1))
        self.ax.set_ylim(0, 150)            #todo vratit u 150 kg kad dobijem podatke o masi, potrebe testiranja 255

        self.ax.set_xlabel('Uzorak', fontsize='large')
        self.ax.set_ylabel('Vrijednost', fontsize='large')

        # self.ax.set_xticklabels(self.xs, rotation=0, ha='right')
        plt.subplots_adjust(bottom=0.30)
        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = PlotWidget()
    win.show()              # prikazuje prozor
    sys.exit(app.exec_())   # zatvara kad stisnemo x gumb
