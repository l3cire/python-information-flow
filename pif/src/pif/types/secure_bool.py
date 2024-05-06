from pif.src.pif.types.secure_type import SecureType


class SecureBool(SecureType):
    """The SecureBool type is a security wrapper around Python bools."""
    _val = None
    _level = None

    def __init__(self, val, sec):
        # Ensure val is an int or float; otherwise, throw an error
        if not isinstance(val, bool):
            raise ValueError("SecureBool can only be used with bool")
        if not isinstance(sec, int) or sec < 0:
            raise ValueError("Security level should be a non-negative integer")

        # The underscore indicates this field should be private even
        # though there is no way of enforcing this in Python.
        self._val = val
        self._level = sec

    def set_value(self, val):
        if not isinstance(val, bool):
            raise ValueError("SecureBool can only be used with bool")

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
        if isinstance(other, SecureBool):
            return other
        elif isinstance(other, bool):
            return SecureBool(other, 0)
        else:
            raise ValueError("SecureBool can only be used with bool")

    def __repr__(self):
        return f"<SecureBool: val: {self._val}, sec: {self._level}>"

    def __str__(self):
        return str(self._val)

    def __and__(self, other):
        secure_other = SecureBool.wrapper(other)
        return SecureBool(self._val and secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __rand__(self, other):
        secure_other = SecureBool.wrapper(other)
        return SecureBool(secure_other.get_value() and self._val,
                          max(self._level, secure_other.get_level()))

    def __or__(self, other):
        secure_other = SecureBool.wrapper(other)
        return SecureBool(self._val or secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __ror__(self, other):
        secure_other = SecureBool.wrapper(other)
        return SecureBool(secure_other.get_value() or self._val,
                          max(self._level, secure_other.get_level()))

    def __xor__(self, other):
        secure_other = SecureBool.wrapper(other)
        return SecureBool(self._val ^ secure_other.get_value(),
                          max(self._level, secure_other.get_level()))

    def __rxor__(self, other):
        secure_other = SecureBool.wrapper(other)
        return SecureBool(secure_other.get_value() ^ self._val,
                          max(self._level, secure_other.get_level()))
