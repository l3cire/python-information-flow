from pif.stypes.secure_num import SecureNum

a = SecureNum(1, 0)
b = SecureNum(2, 10)

while a > 0:
    b = SecureNum(1, 2)
    a -= 1

print(repr(b))
