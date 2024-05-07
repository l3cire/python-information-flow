from pif.stypes.secure_num import SecureNum

a = SecureNum(5, 3)
b = SecureNum(10, 8)

if b > 5:
    a = 10

print(repr(a))
