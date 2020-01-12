import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import animation
from matplotlib.figure import Figure
import serial


class PlotWidget(QWidget):  # or QWidget ??? or QDialog as it was default

    def __init__(self, parent=None):
        super().__init__(parent)  # preko parenta pristupam atributima i metodama od VagaWindow
        self.parent = parent

        ## Dodano za provejru s arduinom
        # self.ser = serial.Serial('COM10', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        # if (self.ser.isOpen()): print("Port je otvoren!")
        ###

        self.fig = Figure(figsize=(6, 5), dpi=100)
        self.fig.suptitle("Real-time prikaz podataka")
        self.canvas = FigureCanvas(self.fig)
        #self.button = QPushButton('Animate')
        #self.button.clicked.connect(self.setup)


        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        #layout.addWidget(self.button)
        self.setLayout(layout)

        #self.setup()

    #def setup(self):
        self.ax = self.fig.add_subplot(111)  # create an axis
        self.xs = []
        self.ys = []
        # self.i = 0;

        self.anim = animation.FuncAnimation(self.fig, self.animate, fargs=(self.xs, self.ys), interval=1000)
        self.canvas.draw()

    def animate(self, i, xs, ys):
        ## Dodano za provejru s arduinom
        #self.i = self.ser.read()
        #self.i = int.from_bytes(self.i, "little", signed=True)
        #print(self.i)
        ###

        # self.i = self.i + 1;

        self.xs.append(dt.datetime.now().strftime('%H:%M:%S.%f')[:-5])
        print(dt.datetime.now().strftime('%H:%M:%S.%f')[:-4])
        self.ys.append(self.i)


        self.xs = self.xs[-30:]
        self.ys = self.ys[-30:]

        self.ax.clear()
        self.ax.plot(self.xs, self.ys)

        self.ax.set_xlabel('Vrijeme', fontsize='xx-large')
        self.ax.set_ylabel('Vrijednost', fontsize='xx-large')

        self.ax.set_xticklabels(self.xs, rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        # self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PlotWidget()
    win.show()              # prikazuje prozor
    sys.exit(app.exec_())   # zatvara kad stisnemo x gumb
