# & bitwise AND

# This operator compares each bit of the first operand to the corresponding bit
# of the second operand, and if both bits are 1, the corresponding result bit
# is set to 1 on the other hand if both bits are 0, the result is 0 too.


x = 0b10101010 # 170 in binary
y = 0b01010101 # 85 in binary
z = x & y #the result is 0b00000000, or 0 in decimal

print(z)