import serial
from serial.tools import list_ports
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
        while True:
            print(int.from_bytes(ser.read(), "little", signed=True))
            print(int.from_bytes(ser.read(), "little", signed=True))

            incoming_byte = ser.read()
            incoming_int = int.from_bytes(incoming_byte, "little", signed=True)
            print(incoming_hex)
            print(type(incoming_hex))

            incoming_hex = ser.read().hex()
            print(incoming_hex)
            print(type(incoming_hex))

            incoming_hex = ser.read(4).hex()
            print(incoming_hex)
            print(type(incoming_hex))

            incoming_hex = np.uint8(ser.read().hex())
            print(incoming_hex)
            print(type(incoming_hex))

            print(np.uint8(0x17))





    except NameError:
        print("-------- Komunikacija nije uspostavljena jer je port trenutno zauzet! --------")

    try:
        ser.close()
    except NameError:
        pass
