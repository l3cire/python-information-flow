from pif.src.pif.types.secure_type import SecureType
from pif.src.pif.types.secure_num import SecureNum
from pif.src.pif.types.secure_bool import SecureBool
from pif.src.pif.types.secure_string import SecureString
from security_exception import SecurityException

type_map = {
    int: SecureNum,
    float: SecureNum,
    str: SecureString,
    bool: SecureBool
}


class SecurityMonitor:
    @staticmethod
    def sec_type(expr):
        if isinstance(expr, SecureType):
            expr.set_level(max(expr.get_level(), SecurityMonitor.get_pc()))
            return expr

        if type(expr) in type_map:
            type_map[type(expr)](expr, SecurityMonitor.get_pc())
        else:
            raise ValueError("Python type " + type(expr) + "not supported in PIF")

    stack = []
    stack_cumulative = []

    @staticmethod
    def push_pc(expr):
        SecurityMonitor.stack.append(expr.get_level())
        if len(SecurityMonitor.stack_cumulative) == 0:
            SecurityMonitor.stack_cumulative.append(SecurityMonitor.stack[-1])
        else:
            SecurityMonitor.stack_cumulative.append(
                max(SecurityMonitor.stack[-1], SecurityMonitor.stack_cumulative[-1])
            )

    @staticmethod
    def get_pc():
        return 0 if len(SecurityMonitor.stack_cumulative) == 0 else SecurityMonitor.stack_cumulative[-1]

    @staticmethod
    def pop_pc():
        SecurityMonitor.stack.pop()
        SecurityMonitor.stack_cumulative.pop()

    @staticmethod
    def check_assignment(expr):
        if isinstance(expr, SecureType) and expr.get_level() < SecurityMonitor.get_pc():
            raise SecurityException("Security level of the expression is too low")
