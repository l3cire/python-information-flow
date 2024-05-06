from pif.stypes.secure_num import SecureNum

a = SecureNum(1, 0)
b = SecureNum(2, 10)

if b < 0:
    b = SecureNum(1, 2)
else:
    a = SecureNum(1, 2)

print(repr(a))
