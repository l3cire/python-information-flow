from pif.stypes.secure_num import SecureNum

a = SecureNum(1, 0)
b = SecureNum(2, 10)

while b > 0:
    b -= 1
else:
    a = 0

print(repr(a))
