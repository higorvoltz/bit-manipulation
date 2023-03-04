
############################################

# BITMASKING

# Bitmasking is a technique for setting, clearing, or checking individual bits
# in a number. It involves using bitwise operators to manipulate the bits of a
# number in order to set or clear specific bits or to check the values of
# specific bits.
# For example, suppose you have a number x and you want to set the third and
# fifth bits (counting from the right) to 1. You can do this using the
# following code:

byte_initial = 0b00000000  # The number 0 in binary
mask = 0b00101000  # The mask with the third and fifth bits set to 1
byte_initial = byte_initial | mask # The result is 0b00101000, or 40 in decimal
print(byte_initial, bin(byte_initial))

# Alternatively, suppose you have a number x and you want to clear the fourth
# and sixth bits (counting from the right). You can do this using the
# following code:

other_initial = 0b11111111  # The number 255 in binary
other_mask = 0b11010111  # The mask with the fourth and sixth bits set to 0
other_initial = other_initial & other_mask # The result is 0b11010111, or 215 in decimal
print(other_initial, bin(other_initial))

# Bitmasking can also be used to check the values of specific bits in a number.
# For example, suppose you have a number x and you want to check if the seventh
# bit (counting from the right) is set to 1. You can do this using the
# following code:

target = 0b11010111  # The number 215 in binary
mask_target = 0b10000000  # The mask with the seventh bit set to 1
if target & mask:
    print("the seventh bit is set to 1")
else:
  print("the seventh bit is not set to 1")

print(target & mask_target, bin(target & mask_target))

# Bitmasking is often used in programming to represent a set of flags or to
# implement certain algorithms efficiently. For example, you might use
# bitmasking to represent a set of permissions (e.g., read, write, execute) or
# to implement a fast algorithm for finding the intersection of two sets.
# Suppose you want to represent a set of flags that indicate whether a user has
# read, write, and execute permissions for a particular file. You could define
# the following constants:

READ_PERMISSION = 0b001  # 1
WRITE_PERMISSION = 0b010 # 2
EXECUTE_PERMISSION = 0b100 # 4

# compare USER_ENTRY with READ_PERMISSION

mask_permissions = 0b101

# grant the user read permission
mask_permissions = mask_permissions | READ_PERMISSION

if mask_permissions & READ_PERMISSION:
    print("user allowed to read")
else:
    print("user denied")

print(mask_permissions & READ_PERMISSION, bin(mask_permissions & READ_PERMISSION))

# grant the user write permission
mask_permissions = mask_permissions | WRITE_PERMISSION
if mask_permissions & WRITE_PERMISSION:
    print("user allowed to write")
else:
    print("user denied")

print(mask_permissions & WRITE_PERMISSION, bin(mask_permissions & WRITE_PERMISSION))

# grant the user execute permision
mask_permissions = mask_permissions | EXECUTE_PERMISSION
if mask_permissions & EXECUTE_PERMISSION:
    print("user allowed to execute")
else:
    print("user denied")

print(mask_permissions & EXECUTE_PERMISSION, bin(mask_permissions & EXECUTE_PERMISSION))