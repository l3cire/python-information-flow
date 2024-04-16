from inf_flow_types import SecureType, SecurityMonitor
a = SecurityMonitor.sec_type(SecureType(5, 3))
b = SecurityMonitor.sec_type(SecureType(10, 8))
temp = b < 5
SecurityMonitor.push_pc(temp)
if SecurityMonitor.get_val(temp):
    a = SecurityMonitor.sec_type(10)
SecurityMonitor.pop_pc()
temp = b > 5
SecurityMonitor.push_pc(temp)
if SecurityMonitor.get_val(temp):
    a = SecurityMonitor.sec_type(10)
SecurityMonitor.pop_pc()
print(repr(a))