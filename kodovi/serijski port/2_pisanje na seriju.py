import serial
from serial.tools import list_ports

if __name__ == "__main__":
    ports = serial.tools.list_ports.comports(include_links=False)  # spremanje dostupnih portova u listu
    print("Dostupni COM portovi su: ")
    for port in ports:
        print(port.device)

    selected_port = input("Unesite ime porta: ")
    ser = serial.Serial(selected_port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE)
    if (ser.isOpen()):
        print(selected_port + " port je otvoren!")  # provjera da je serijski port otvoren

    print(ser.write(b'\xee'))  # write() vraca broj zapisanih bajtova (int varijabla)
    # \xee je jedan oktet u heksidecimalnoj bazi (8 bitova)

    ser.close()
