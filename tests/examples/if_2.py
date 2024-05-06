from pif.stypes.secure_num import SecureNum

a = SecureNum(1, 0)
b = SecureNum(2, 10)

if a > 0:
    b = SecureNum(1, 2)

print(repr(b))
