#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'

class RectangleWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # preko parenta pristupam atributima i metodama od VagaWindow
        self.parent = parent

        # ******* Create widgets ******* #
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvas(self.fig)

        # ****** Create layout and add widgets to it ****** #
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # ****** Draw rectangles on the figure in canvas **** #
        self.ax1 = self.fig.add_subplot(111)

        # ***** Make 2 rectangles and add it to the figure ********* #
        self.width = 2
        self.len = 4
        self.rect1 = matplotlib.patches.Rectangle((0, 0), self.width, self.len, linewidth=1.5, edgecolor='k', facecolor='none')
        self.ax1.add_patch(self.rect1)

        self.rect2 = matplotlib.patches.Rectangle((5, 0), self.width, self.len, linewidth=1.5, edgecolor='k', facecolor='none')
        self.ax1.add_patch(self.rect2)

        # ******** Figure settings ****** #
        self.ax1.axis('off')
        self.ax1.set_xlim(-1, 8)
        self.ax1.set_ylim(-1, 5)
        self.ax1.set_aspect('equal')

        self.canvas.draw()

        self.angle_l = 10
        self.angle_r = -10
        # Provjera pravokutnika da plesu
        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(500)
        # self.timer.timeout.connect(self.update_rectangle)
        # self.timer.start()


    def update_rectangle(self):
        self.ax1.clear()
        self.ax1.set_aspect('equal')
        ts = self.ax1.transData
        coords = [1, 2]  # tocka oko koje se rotira pravokutnik (centar)
        tr = matplotlib.transforms.Affine2D().rotate_deg_around(coords[0], coords[1], self.angle_l)
        t = tr + ts

        coords2 = [6, 2]  # tocka oko koje se rotira pravokutnik (centar)
        tr2 = matplotlib.transforms.Affine2D().rotate_deg_around(coords2[0], coords2[1], self.angle_r)
        t2 = tr2 + ts

        # ****** Rotate rectangles and add it to the figure ****** #
        rect1_rot = matplotlib.patches.Rectangle((0, 0), self.width, self.len, linewidth=1, edgecolor='k', facecolor='none',
                                                 transform=t)
        self.ax1.add_patch(rect1_rot)

        rect2_rot = matplotlib.patches.Rectangle((5, 0), self.width, self.len, linewidth=1, edgecolor='k', facecolor='none',
                                                 transform=t2)
        self.ax1.add_patch(rect2_rot)

        # ******** Figure settings ****** #
        self.ax1.axis('off')
        self.ax1.set_xlim(-1, 8)
        self.ax1.set_ylim(-1, 5)

        self.angle_l *= -1
        self.angle_r *= -1

        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = RectangleWidget()
    win.show()  # prikazuje prozor

    sys.exit(app.exec_())  # zatvara kad stisnemo x gumb
