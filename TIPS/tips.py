#################################################################

# BIT MANIPULATION TRICKS

# Bit manipulation tricks are techniques that involve using bit manipulation to
# solve problems in clever ways. Here are a few examples of common bit
# manipulation tricks:

# Isolating the rightmost 1-bit: You can use the x & (-x) idiom to isolate the
# rightmost 1-bit in a number. For example:

number1 = 0b01010101  # The number 85 in binary
number2 = 0b11010111  # The number 85 in binary 256+128+32+0+8+2+1
number3 = 0b11111111  # The number 85 in binary
isolate_number = number1 & (-number1) # The result is 0b00000001, or 1 in decimal
print(isolate_number, bin(isolate_number))

# Clearing the rightmost 1-bit: You can use the x & (x - 1) idiom to clear the
# rightmost 1-bit in a number. For example:

number_a = 0b01010101  # The number 85 in binary
a_less = number_a & (number_a - 1) # The result is 0b01010100, or 84 in decimal
print(a_less, bin(a_less))

# Checking if a number is a power of 2: You can use the x & (x - 1) == 0 idiom
# to check if a number is a power of 2. For example:

power_two = 8
if power_two & (power_two - 1) == 0:
    print("x is a power of 2")

# power_two = 9
# if power_two & (power_two - 1) == 0:
#     print("x is a power of 2") # this line will not be printed

# Counting the number of 1-bits: You can use the x &= (x - 1) idiom to count
# the number of 1-bits in a number. For example:

number_b = 0b01010101  # The number 85 in binary
count = 0
while number_b:
    count += 1
    number_b &= (number_b - 1)
print(count)  # The output is 4

# Swapping the values of two variables: You can use bit manipulation to swap
# the values of two variables without using a temporary variable. For example:

num_swap = 10
num_swap2 = 20

num_swap ^= num_swap2
num_swap2 ^= num_swap
num_swap ^= num_swap2

print("num swap", num_swap) # 20
print("num_swap2", num_swap2) # 10

# Checking if a number is odd or even: You can use the x & 1 idiom to check
# if a number is odd or even. For example:

if 11 & 1:
    print("11 is odd")

if 10 | 0:
    print("10 is even")

# Determining the sign of a number: You can use the x >> 31 idiom to determine
# the sign of a number. For example:

if 10 << 31:
    print("10 is positive")

if -10 >> 31:
    print("-10 is negative")

# Calculating the absolute value of a number: You can use
# the (x + (x >> 31)) ^ (x >> 31) idiom to calculate the absolute value
# of a number. For example:

# num_c = 10
num_c = -10
abs_c = (num_c + (num_c >> 31)) ^ (num_c >> 31)
print(abs_c) # The output is 10

# Reversing the bits of a number: You can use bit manipulation to reverse the
# bits of a number. For example:

num_d = 0b01010101  # The number 85 in binary
print('   ', bin(num_d))
dd = 0

# reverse the bits of num_d
for i in range(8):
    dd = (dd << 1) | (num_d & 1)
    num_d >>= 1

print(dd, bin(dd)) # The output is 0b10101010, or 170 in decimal

# Calculating the logarithm of a number: You can use bit manipulation to
# calculate the logarithm of a number. For example:

num_e = 256 # The logarithm of 256 is 8
ee = 0
while num_e > 1:
    ee += 1
    num_e >>= 1
print(ee) # The output is 8

# Calculating the square root of a number: You can use bit manipulation to
# calculate the square root of a number. For example:

num_f = 256
ff = 0
while num_f > 0:
    ff += 1
    num_f >>= 2
print(ff) # The output is 16