if __name__ == "__main__":

    print(int.from_bytes(b'\x00\xfc', "little", signed=True))
print(int.from_bytes(b'\x00\xfc', "little", signed=False))
print(int.from_bytes(b'\xfc', "little", signed=True))
print(int.from_bytes(b'\xfc', "little", signed=False))
print(int.from_bytes(b'\x33\x00\xfc', "little", signed=True))
print(int.from_bytes(b'\x33\x00\xfc', "little", signed=False))


print(int.from_bytes(b'\xfd', byteorder='big', signed=True))  # -3
print(int.from_bytes(b'\x03', byteorder='big', signed=True))  # 3
print(int.from_bytes(b'\xff\xfd', byteorder='big', signed=True))  # -3
print(int.from_bytes(b'\x00\x03', byteorder='big', signed=True))  # 3

