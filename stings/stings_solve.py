def hexToAscii(hexx):
    ascii = ""
    for i in range(0, len(hexx), 2):
        part = hexx[i: i+2]
        ascii += chr(int(part, 16) - 1)
    return ascii[::-1]

v14 = "7375747C6775646A"
v15 = "3473356074686F32"
v16 = "346565326960756F"
v17 = "623233633832606F"
v18 = "7E3A37"
print(hexToAscii(v14) + hexToAscii(v15) + hexToAscii(v16) + hexToAscii(v17) + hexToAscii(v18))