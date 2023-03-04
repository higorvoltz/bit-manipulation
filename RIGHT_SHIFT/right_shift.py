
#############################################

# right shift
# This operator shifts the bits of the operand to the right by the number of
# positions specified by the second operand

x = 0b10101010 # 170 in binary

x_right = x >> 2 # The result is 0b00101010, or 42 in decimal
print(x_right, bin(x_right))