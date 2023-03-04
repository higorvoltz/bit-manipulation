
############################################

# ^ bitwise XOR
# This operator compares each bit of the first operand to the corresponding bit
# of the second operand, and if the bits are different, the corresponding result
# bit is set to 1

x = 0b10101010 # 170 in binary
y = 0b01010101 # 85 in binary
z = x ^ y #the result is 0b11111111, or 255 in decimal
print(z, bin(z))