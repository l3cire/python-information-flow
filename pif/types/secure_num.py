from secure_type import SecureType
from secure_bool import SecureBool


class SecureNum(SecureType):
    """The SecureNum type is a security wrapper around Python ints and floats."""

    _val = None
    _level = None

    def __init__(self, val, sec):
        # Ensure val is an int or float; otherwise, throw an error
        if not isinstance(val, (int, float)):
            raise ValueError("SecureNum can only be used with int or float")
        if not isinstance(sec, int) or sec < 0:
            raise ValueError("Security level should be a non-negative integer")

        # The underscore indicates this field should be private even
        # though there is no way of enforcing this in Python.
        self._val = val
        self._level = sec

    def set_value(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError("SecureNum can only be used with int or float")

        self._val = val

    def get_level(self):
        return self._level

    def set_level(self, level):
        if not isinstance(level, (int, float)) or level < 0:
            raise ValueError("Must set security level to a non-negative integer")
        self._level = level

    def get_value(self):
        return self._val

    @staticmethod
    def wrapper(other):
        if isinstance(other, SecureNum):
            return other
        elif isinstance(other, (int, float)):
            return SecureNum(other, 0)
        else:
            raise ValueError("SecureNum can only be used with int or float")

    def __add__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val + secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __radd__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val + secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __sub__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val - secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rsub__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val - secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __mul__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val * secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rmul__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val * secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __floordiv__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val // secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rfloordiv__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() // self._val,
                         max(self._level, secure_other.get_level()))

    def __mod__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val % secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rmod__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() % self._val,
                         max(self._level, secure_other.get_level()))

    def __pow__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val ** secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rpow__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() ** self._val,
                         max(self._level, secure_other.get_level()))

    def __and__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val & secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rand__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() & self._val,
                         max(self._level, secure_other.get_level()))

    def __or__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val | secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __ror__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() | self._val,
                         max(self._level, secure_other.get_level()))

    def __xor__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val ^ secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rxor__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() ^ self._val,
                         max(self._level, secure_other.get_level()))

    def __rshift__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val >> secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rrshift__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() >> self._val,
                         max(self._level, secure_other.get_level()))

    def __lshift__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(self._val << secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __rlshift__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureNum(secure_other.get_value() << self._val,
                         max(self._level, secure_other.get_level()))

    def __lt__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureBool(self._val < secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __gt__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureBool(self._val > secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __le__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureBool(self._val <= secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __ge__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureBool(self._val >= secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __eq__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureBool(self._val == secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __ne__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureBool(self._val != secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return f"<SecureNum: val: {self._val}, sec: {self._level}>"
