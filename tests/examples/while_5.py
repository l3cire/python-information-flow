from pif.stypes.secure_num import SecureNum

a = SecureNum(1, 0)
b = SecureNum(2, 10)

while b > 0:
    b = b - 1
else:
    b = 7

print(repr(b))
