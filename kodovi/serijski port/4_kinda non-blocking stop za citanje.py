import serial
from serial.tools import list_ports
import msvcrt


if __name__ == "__main__":
	ports = serial.tools.list_ports.comports(include_links=False)	#spremanje dostupnih portova u listu
	print("Dostupni COM portovi su: ")
	for port in ports :
   		print(port.device)

	selected_port = input("Unesite ime porta: ")
	ser = serial.Serial(selected_port, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
	if(ser.isOpen()): print(selected_port+" port je otvoren!")		#provjera da je serijski port otvoren

	while True:
		print(ser.read().hex())
		if msvcrt.kbhit():						#ova opcija radi samo ako se pokrece iz cmd-a, malo beskorisno ovak
												#zaustavlja kad bilo sta na tipkovnici pritisnemo
			print ("you pressed",msvcrt.getch(),"so now i will quit")
			break
		#if (input() == 'q'): ser.close()		#input je blokirajuci, ne moze ovak
	
	ser.close()