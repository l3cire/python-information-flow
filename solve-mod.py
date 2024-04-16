from inf_flow_types import SecureType, SecurityMonitor
if 'a' in locals() or 'a' in globals():
    SecurityMonitor.check_assignment(a)
a = SecurityMonitor.sec_type(SecureType(5, 3))
if 'b' in locals() or 'b' in globals():
    SecurityMonitor.check_assignment(b)
b = SecurityMonitor.sec_type(SecureType(10, 8))
temp = b < 5
SecurityMonitor.push_pc(temp)
if SecurityMonitor.get_val(temp):
    if 'a' in locals() or 'a' in globals():
        SecurityMonitor.check_assignment(a)
    a = SecurityMonitor.sec_type(10)
SecurityMonitor.pop_pc()
temp = b > 5
SecurityMonitor.push_pc(temp)
if SecurityMonitor.get_val(temp):
    if 'a' in locals() or 'a' in globals():
        SecurityMonitor.check_assignment(a)
    a = SecurityMonitor.sec_type(10)
SecurityMonitor.pop_pc()
print(repr(a))