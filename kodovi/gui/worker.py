from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal
import time

class WorkerSignals(QObject):
    result = pyqtSignal(object)
    finished = pyqtSignal()


class Worker(QRunnable):
    def __init__(self, ser):
        super(Worker, self).__init__()
        self.ser = ser
        self.signals = WorkerSignals()
        print("Init worker done")
        self.force_stop = False

    @pyqtSlot()
    def run(self):
        start = 0
        header = []
        default_header = ['17', 'a3', '91', 'f4']
        package = dict()  # lista u kojoj ce bit jedan paket, pojedinacno ce se prepisivat i zapisivat u datoteku
        legs = ['L1', 'R1', 'L2', 'R2', 'L3', 'R3', 'L4', 'R4', 'L5', 'R5', 'L6', 'R6', 'L7', 'R7', 'L8', 'R8', 'L9', 'R9', 'L10', 'R10']

        self.ser.reset_input_buffer()
        print("Run started")
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < 30 and self.force_stop is False:     # mjerenje(citanje podataka) traje 30 sekundi            #todo vratit na 30 sek
            incoming_hex = self.ser.read().hex()
            # print(incoming_hex)

            header.append(incoming_hex)
            if len(header) >= 4:
                if header == default_header:
                    start = True
                    print("Header arrived!")
                else:
                    header.pop(0)

            if start:
                incoming_byte = self.ser.read()
                package['ID'] = int.from_bytes(incoming_byte, "little", signed=True)  # fiksno 0x01
                # print(package)
                incoming_byte = self.ser.read()
                package["CycleID"] = int.from_bytes(incoming_byte, "little", signed=False)  # broj paketa - uint8
                # print(package)
                incoming_byte = self.ser.read()
                package["length"] = int.from_bytes(incoming_byte, "little", signed=True)  # fiksno 85
                # print(package)

                for x in range(len(legs)):
                    incoming_byte = self.ser.read(4)
                    package[legs[x]] = int.from_bytes(incoming_byte, "little", signed=True)
                    #print(package)

                incoming_byte = self.ser.read(2)
                package["ANGLE_L"] = int.from_bytes(incoming_byte, "little", signed=True)
                # print(package)
                incoming_byte = self.ser.read(2)
                package["ANGLE_R"] = int.from_bytes(incoming_byte, "little", signed=True)
                # print(package)
                incoming_byte = self.ser.read()
                package["DIST"] = int.from_bytes(incoming_byte, "little", signed=False)  # udaljenost - uint8 - OK
                # print(package)
                incoming_byte = self.ser.read(1)
                package["Checksum"] = int.from_bytes(incoming_byte, "little", signed=True)
                #print(package)

                print("Sending package")
                self.signals.result.emit(package)

                start = False
                header.clear()
                #print("ciscenjeeeeeeeeeeeeee")

            elapsed_time = time.time() - start_time

        self.signals.finished.emit()

