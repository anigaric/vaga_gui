import serial
from serial.tools import list_ports
import numpy as np

if __name__ == "__main__":
    ser = serial.Serial('COM10', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    if ser.isOpen(): print("Port je otvoren!")

    while True:
        incoming_byte = ser.read(2)
        print(b"%b" % incoming_byte)
        angle = int.from_bytes(incoming_byte, "little", signed=True)
        print(angle)