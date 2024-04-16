from inf_flow_types import SecureType, SecurityMonitor

a = SecureType(5, 3)
b = SecureType(10, 8)
if b < 5:
    a = 10
if b > 5:
    a = 10
print(repr(a))
