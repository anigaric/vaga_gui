import serial
from serial.tools import list_ports
import time

if __name__ == "__main__":
    start = 0
    header = []
    default_header = ['17', 'a3', '91', 'f4']
    package = dict()  # lista u kojoj ce bit jedan paket, pojedinacno ce se prepisivat i zapisivat u datoteku
    package_hex = dict()
    legs = ['L1', 'R1', 'L2', 'R2', 'L3', 'R3', 'L4', 'R4', 'L5', 'R5', 'L6', 'R6', 'L7', 'R7', 'L8', 'R8', 'L9', 'R9',
            'L10', 'R10']

    # ports = serial.tools.list_ports.comports(include_links=False)  # spremanje dostupnih portova u listu
    # print("Dostupni COM portovi su: ")
    # for port in ports:
    #     print(port.device)
    #
    # selected_port = input("Unesite ime porta: ")
    selected_port = 'COM7'
    try:
        ser = serial.Serial(selected_port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE)
        if (ser.isOpen()): print(selected_port + " port je otvoren!")  # provjera da je serijski port otvoren
    except (OSError, serial.SerialException):
        print("------------------- Odabrani serijski port trenutno zauzet! ------------------")

    try:
        ser.reset_input_buffer()
        file = open("raw_data.txt", "w")
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < 10:
            incoming = ser.read().hex()
            file.write(incoming)
            file.write("\n")

            elapsed_time = time.time() - start_time
        file.close()

    except NameError:
        print("-------- Komunikacija nije uspostavljena jer je port trenutno zauzet! --------")

    try:
        ser.close()
    except NameError:
        pass