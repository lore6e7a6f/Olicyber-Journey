# da ghidra

hexstr = "66 00 6c 00 61 00 67 00 7b 00 38 00 31 00 37 00 35 00 30 00 65 00 36 00 33 00 7d 00"
b = bytes.fromhex(hexstr)
print(b.decode('utf-16le')) 
