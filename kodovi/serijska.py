import serial
from serial.tools import list_ports
import time
import numpy as np

if __name__ == "__main__":
    start = 0
    header = []
    default_header = ['17', 'a3', '91', 'f4']
    package = dict()  # lista u kojoj ce bit jedan paket, pojedinacno ce se prepisivat i zapisivat u datoteku
    legs = ['L1', 'R1', 'L2', 'R2', 'L3', 'R3', 'L4', 'R4', 'L5', 'R5', 'L6', 'R6', 'L7', 'R7', 'L8', 'R8', 'L9', 'R9',
            'L10', 'R10']

    ports = serial.tools.list_ports.comports(include_links=False)  # spremanje dostupnih portova u listu
    print("Dostupni COM portovi su: ")
    for port in ports:
        print(port.device)

    selected_port = input("Unesite ime porta: ")
    try:
        ser = serial.Serial(selected_port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE)
        if (ser.isOpen()): print(selected_port + " port je otvoren!")  # provjera da je serijski port otvoren
    except (OSError, serial.SerialException):
        print("------------------- Odabrani serijski port trenutno zauzet! ------------------")

    try:
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < 30:                # mjerenje(citanje podataka) traje 30 sekundi
            incoming_hex = ser.read().hex()
            print(incoming_hex)

            header.append(incoming_hex)
            if len(header) >= 4:
                if header == default_header:
                    start = 1
                    print("Header arrived!")
                else:
                    header.pop(0)

            if start == 1:
                incoming_byte = ser.read()
                package['ID'] = int.from_bytes(incoming_byte, "little", signed=True)  # fiksno 0x01
                # print(package)
                incoming_byte = ser.read()
                package["CycleID"] = int.from_bytes(incoming_byte, "little", signed=False)  # broj paketa - uint8
                # print(package)
                incoming_byte = ser.read()
                package["length"] = int.from_bytes(incoming_byte, "little", signed=True)  # fiksno 85
                # print(package)

                for x in range(len(legs)):
                    incoming_byte = ser.read(4)
                    package[legs[x]] = int.from_bytes(incoming_byte, "little", signed=True)
                    print(package)

                incoming_byte = ser.read(2)
                package["ANGLE_L"] = int.from_bytes(incoming_byte, "little", signed=True)
                # print(package)
                incoming_byte = ser.read(2)
                package["ANGLE_R"] = int.from_bytes(incoming_byte, "little", signed=True)
                # print(package)
                incoming_byte = ser.read()
                package["DIST"] = int.from_bytes(incoming_byte, "little", signed=False)  # udaljenost - uint8 - OK
                # print(package)
                incoming_byte = ser.read(1)
                package["Checksum"] = int.from_bytes(incoming_byte, "little", signed=True)
                print(package)

                start = 0
                header.clear()
                print("ciscenjeeeeeeeeeeeeee")

            elapsed_time = time.time() - start_time

    except NameError:
        print("-------- Komunikacija nije uspostavljena jer je port trenutno zauzet! --------")

    try:
        ser.close()
    except NameError:
        pass
