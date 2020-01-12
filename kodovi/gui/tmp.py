import sys
import numpy as np
#from matplotlib.backends.qt_compat import QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import animation


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QWidget()
        self.setCentralWidget(self._main)
        layout = QVBoxLayout(self._main)

        self.fig = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.addToolBar(NavigationToolbar(self.canvas, self))

        self.setup()

    def setup(self):
        self.ax = self.fig.subplots()
        self.ax.set_aspect('equal')
        self.ax.grid(True, linestyle = '-', color = '0.10')
        self.ax.set_xlim([-15, 15])
        self.ax.set_ylim([-15, 15])

        self.scat = self.ax.scatter([], [], c=(0.9, 0.1, 0.5),  zorder=3)
        self.scat.set_alpha(0.8)

        self.anim = animation.FuncAnimation(self.fig, self.update, frames = 720, interval = 10)

    def update(self, i):

        self.scat.set_offsets(([np.cos(np.radians(i))*7.5, np.sin(np.radians(i))*7.5], [0,0]))

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()