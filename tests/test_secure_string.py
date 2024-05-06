from pif.stypes.secure_bool import SecureBool
from pif.stypes.secure_num import SecureNum
from pif.stypes.secure_string import SecureString
from helpers import assert_val_level

a = SecureString("abc", 0)
b = SecureString("def", 0)

n = SecureNum(3, 0)


# Test the normal non-specific operands. The right operands are tested later on their own.
def test_add():
    assert_val_level(a + b, "abcdef", 0)


def test_add_str():
    temp = a + "abc"
    assert isinstance(temp, SecureString)
    assert_val_level(temp, "abcabc", 0)


def test_len():
    assert_val_level(a.get_length(), 3, 0)


def test_mul():
    assert_val_level(a * n, "abcabcabc", 0)


# Right operands
def test_radd():
    temp = "aaa" + a

    assert isinstance(temp, SecureString)
    assert_val_level(temp, "aaaabc", 0)


# Comparison operators
def test_lt():
    assert_val_level(a < b, True, 0)


def test_gt():
    assert_val_level(a > b, False, 0)


def test_le():
    assert_val_level(a <= b, True, 0)


def test_ge():
    assert_val_level(a >= b, False, 0)


def test_eq():
    assert_val_level(a == b, False, 0)


def test_ne():
    assert_val_level(a != b, True, 0)


# Test SecureType interface is working properly
def test_str():
    assert a.__str__() == "abc"


def test_repr():
    assert a.__repr__() == f"<SecureString: val: 'abc', sec: 0>"


def test_get_value():
    assert a.get_value() == "abc"


def test_get_level():
    assert a.get_level() == 0


def test_set_value():
    a.set_value("def")
    assert a.get_value() == "def"
    a.set_value("abc")


def test_set_value_num():
    try:
        a.set_value(1)
    except Exception as e:
        assert isinstance(e, ValueError)
        return

    assert False


def test_set_level():
    a.set_level(1)
    assert a.get_level() == 1
    a.set_level(0)


def test_set_level_neg():
    try:
        a.set_level(-1)
    except Exception as e:
        assert isinstance(e, ValueError)
        return

    assert False


def test_set_level_str():
    try:
        a.set_level("s")
    except Exception as e:
        assert isinstance(e, ValueError)
        return

    assert False


def test_wrapper_a():
    temp = SecureString.wrapper(a)
    assert temp is a


def test_wrapper_other():
    temp = SecureString.wrapper("aaa")

    assert isinstance(temp, SecureString)
    assert temp.get_value() == "aaa"
    assert temp.get_level() == 0


def test_wrapper_num():
    try:
        _ = SecureString.wrapper(123)
    except Exception as e:
        assert isinstance(e, ValueError)
        return

    assert False


# testing indexing and slices
def test_index():
    temp = a[0]
    assert isinstance(temp, SecureString)
    assert_val_level(temp, 'a', 0)


def test_slice():
    temp = a[1:3]
    assert isinstance(temp, SecureString)
    assert_val_level(temp, 'bc', 0)


# testing that security levels update correctly
def test_security():
    a.set_level(0)
    b.set_level(1)
    n.set_level(2)
    assert (a + b).get_level() == 1
    assert (a * n).get_level() == 2
    assert (b + "aaa").get_level() == 1
    assert ("aaa" + b).get_level() == 1
    assert (a == b).get_level() == 1
    assert b[0].get_level() == 1
