from pif.stypes.secure_num import SecureNum

a = SecureNum(1, 0)
b = SecureNum(2, 10)
c = SecureNum(2, 0)

while b > 0:
    b -= 1
    if b == 0:
        a = SecureNum(1, 2)

print(repr(a))
