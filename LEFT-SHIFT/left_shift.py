
############################################

# << left shift
# This operator shifts the bits of the operand to the left by the number of
# positions specified by the second operand

x = 0b10101010 # 170 in binary

x_left = x << 2 # the result is 0b1010101000, or 680 in decimal
print(x_left, bin(x_left))
