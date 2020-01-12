import serial
from serial.tools import list_ports

if __name__ == "__main__":
    ports = serial.tools.list_ports.comports(include_links=False)
    for port in ports:
        print(port.device)
