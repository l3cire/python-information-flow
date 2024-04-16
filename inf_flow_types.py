class SecureType:
    val = None
    sec = None

    def __init__(self, val, sec):
        # Ensure val is an int or float; otherwise, throw an error
        if not isinstance(val, (int, float)):
            raise ValueError("SecureType can only be used with int or float")
        self.val = val
        self.sec = sec

    def __add__(self, other):
        return SecureType(self.val + SecurityMonitor.get_val(other), 
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __radd__(self, other):
        return SecureType(self.val + SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __sub__(self, other):
        return SecureType(self.val - SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rsub__(self, other):
        return SecureType(self.val - SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __mul__(self, other):
        return SecureType(self.val * SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rmul__(self, other):
        return SecureType(self.val * SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __floordiv__(self, other):
        return SecureType(self.val // SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rfloordiv__(self, other):
        return SecureType(SecurityMonitor.get_val(other) // self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __mod__(self, other):
        return SecureType(self.val % SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rmod__(self, other):
        return SecureType(SecurityMonitor.get_val(other) % self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __pow__(self, other):
        return SecureType(self.val ** SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rpow__(self, other):
        return SecureType(SecurityMonitor.get_val(other) ** self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __and__(self, other):
        return SecureType(self.val & SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rand__(self, other):
        return SecureType(SecurityMonitor.get_val(other) & self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __or__(self, other):
        return SecureType(self.val | SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __ror__(self, other):
        return SecureType(SecurityMonitor.get_val(other) | self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __xor__(self, other):
        return SecureType(self.val ^ SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __rxor__(self, other):
        return SecureType(SecurityMonitor.get_val(other) ^ self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rshift__(self, other):
        return SecureType(self.val >> SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rrshift__(self, other):
        return SecureType(SecurityMonitor.get_val(other) >> self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __lshift__(self, other):
        return SecureType(self.val << SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))
    
    def __rlshift__(self, other):
        return SecureType(SecurityMonitor.get_val(other) << self.val,
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __lt__(self, other):
        return SecureType(self.val < SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __gt__(self, other):
        return SecureType(self.val > SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __le__(self, other):
        return SecureType(self.val <= SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __ge__(self, other):
        return SecureType(self.val >= SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __eq__(self, other):
        return SecureType(self.val == SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __ne__(self, other):
        return SecureType(self.val != SecurityMonitor.get_val(other),
                          max(self.sec, SecurityMonitor.get_sec(other)))

    def __isub__(self, other):
        self.val -= SecurityMonitor.get_val(other)
        self.level = max(self.sec, SecurityMonitor.get_sec(other))

    def __iadd__(self, other):
        self.val += SecurityMonitor.get_val(other)
        self.level = max(self.sec, SecurityMonitor.get_sec(other))

    def __imul__(self, other):
        self.val *= SecurityMonitor.get_val(other)
        self.level = max(self.sec, SecurityMonitor.get_sec(other))

    def __ifloordiv__(self, other):
        self.val //= SecurityMonitor.get_val(other)
        self.level = max(self.sec, SecurityMonitor.get_sec(other))

    def __imod__(self, other):
        self.val %= SecurityMonitor.get_val(other)
        self.level = max(self.sec, SecurityMonitor.get_sec(other))

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"<SecureType: val: {self.val}, sec: {self.sec}>"


class SecurityMonitor:

    @staticmethod
    def sec_type(expr):
        if isinstance(expr, SecureType):
            expr.sec = max(expr.sec, SecurityMonitor.get_pc())
            return expr
        # Check if expr is not a float int:
        if not isinstance(expr, (int, float)):
            raise ValueError("SecureType can only be used with int or float")
        return SecureType(expr, SecurityMonitor.get_pc())

    @staticmethod
    def get_sec(expr):
        if isinstance(expr, SecureType):
            return max(SecurityMonitor.get_pc(), expr.sec)
        return SecurityMonitor.get_pc()

    @staticmethod
    def get_val(expr):
        if isinstance(expr, SecureType):
            return expr.val
        return expr

    stack = []
    stack_cumulative = []

    @staticmethod
    def push_pc(expr):
        SecurityMonitor.stack.append(SecurityMonitor.get_sec(expr))
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

