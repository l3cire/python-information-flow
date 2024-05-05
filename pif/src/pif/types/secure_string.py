from secure_type import SecureType
from secure_num import SecureNum
from secure_bool import SecureBool


class SecureString(SecureType):
    """The SecureString type is a security wrapper around Python ints and floats."""
    _val = None
    _level = None

    def __init__(self, val, sec):
        # Ensure val is an int or float; otherwise, throw an error
        if not isinstance(val, str):
            raise ValueError("SecureString can only be used with string")
        if not isinstance(sec, int) or sec < 0:
            raise ValueError("Security level should be a non-negative integer")

        # The underscore indicates this field should be private even
        # though there is no way of enforcing this in Python.
        self._val = val
        self._level = sec

    def set_value(self, val):
        if not isinstance(val, str):
            raise ValueError("SecureString can only be used with string")

        self._val = val

    def get_level(self):
        return self._level

    def set_level(self, level):
        if not isinstance(level, (int, float)) or level < 0:
            raise ValueError("Must set security level to a non-negative integer")
        self._level = level

    def get_value(self):
        return self._val

    def get_length(self):
        return SecureNum(len(self._val), self._level)

    @staticmethod
    def wrapper(other):
        if isinstance(other, SecureString):
            return other
        elif isinstance(other, str):
            return SecureString(other, 0)
        else:
            raise ValueError("SecureString can only be used with string")

    def __add__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureString(self._val + secure_other.get_value(),
                            max(self._level, secure_other.get_level()))

    def __radd__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureString(secure_other.get_value() + self._val,
                            max(self._level, secure_other.get_level()))

    def __mul__(self, other):
        secure_other = SecureNum.wrapper(other)
        return SecureString(self._val * secure_other.get_value(),
                         max(self._level, secure_other.get_level()))

    def __lt__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureBool(self._val < secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __gt__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureBool(self._val > secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __le__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureBool(self._val <= secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __ge__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureBool(self._val >= secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __eq__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureBool(self._val == secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __ne__(self, other):
        secure_other = SecureString.wrapper(other)
        return SecureBool(self._val != secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __getitem__(self, item):
        if isinstance(item, int):
            if item >= len(self._val) or item < -len(self._val):
                return SecureString('', self._level)
        return SecureString(self._val[item], self._level)

    def __repr__(self):
        return f"<SecureNum: val: '{self._val}', sec: {self._level}>"

    def __str__(self):
        return self._val
