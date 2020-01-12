import serial
from serial.tools import list_ports
import sys

if __name__ == "__main__":
	ports = serial.tools.list_ports.comports(include_links=False)	#spremanje dostupnih portova u listu
	print("Dostupni COM portovi su: ")
	for port in ports :
   		print(port.device)

	selected_port = input("Unesite ime porta: ")
	try:
		ser = serial.Serial(selected_port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
		if(ser.isOpen()): print(selected_port+" port je otvoren!")		#provjera da je serijski port otvoren
	except (OSError, serial.SerialException):
		print("------------------- Odabrani serijski port trenutno zauzet! ------------------")
		#kako skroz izac iz main-a ovdje??? ili kako zatvorit taj port ako ne postoji ser objekt i ne moze se napravit (ne postoji rjesenje za ovo drugo)

	file = open("incoming_data.bin", "wb")

	try:
		while True:
			incoming_hex = ser.read().hex()
			print(incoming_hex)
			file.write(str.encode(incoming_hex))
			file.write(str.encode(" "))
	except NameError:
		print("-------- Komunikacija nije uspostavljena jer je port trenutno zauzet! --------")

	try:
		ser.close()
	except NameError:
		pass

	file.close()