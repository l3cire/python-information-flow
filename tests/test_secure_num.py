from pif.stypes.secure_num import SecureNum
from helpers import assert_val_level

a = SecureNum(1, 0)
b = SecureNum(2, 0)


# Test the normal non-specific operands. The right operands are tested later on their own.
def test_add():
    assert_val_level(a + b, 3, 0)


def test_sub():
    assert_val_level(b - a, 1, 0)


def test_mul():
    assert_val_level(a * b, 2, 0)


def test_floordiv():
    assert_val_level(b // a, 2, 0)


def test_mod():
    assert_val_level(b % a, 0, 0)


def test_pow():
    assert_val_level(b ** a, 2, 0)


# Right operands
def test_radd():
    temp = 3 + a

    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 4, 0)


def test_rsub():
    temp = 1 - a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 0, 0)


def test_rmul():
    temp = 1 * a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 1, 0)


def test_rfloordiv():
    temp = 1 // a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 1, 0)


def test_rmod():
    temp = 1 % a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 0, 0)


def test_rpow():
    temp = 1 ** a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 1, 0)


def test_rand():
    temp = 1 & a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 1, 0)


def test_ror():
    temp = 1 | a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 1, 0)


def test_rxor():
    temp = 1 ^ a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 0, 0)


def test_rrshift():
    temp = 1 >> a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 0, 0)


def test_rlshift():
    temp = 1 << a
    assert isinstance(temp, SecureNum)
    assert_val_level(temp, 2, 0)


# Bitwise operators
def test_and():
    assert_val_level(b & a, 0, 0)


def test_or():
    assert_val_level(b | a, 3, 0)


def test_xor():
    assert_val_level(b ^ a, 3, 0)


def test_rshift():
    assert_val_level(b >> a, 1, 0)


def test_lshift():
    assert_val_level(b << a, 4, 0)


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
    assert a.__str__() == "1"


def test_repr():
    assert a.__repr__() == f"<SecureNum: val: 1, sec: 0>"


def test_get_value():
    assert a.get_value() == 1


def test_get_level():
    assert a.get_level() == 0


def test_set_value():
    a.set_value(100)
    assert a.get_value() == 100
    a.set_value(1)


def test_set_value_str():
    try:
        a.set_value("1")
    except Exception as e:
        assert isinstance(e, ValueError)
        return

    assert False


def test_set_level():
    a.set_level(1)
    assert a.get_level() == 1


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
    temp = SecureNum.wrapper(a)
    assert temp is a


def test_wrapper_other():
    temp = SecureNum.wrapper(3)

    assert isinstance(temp, SecureNum)
    assert temp.get_value() == 3
    assert temp.get_level() == 0


def test_wrapper_str():
    try:
        _ = SecureNum.wrapper("1")
    except Exception as e:
        assert isinstance(e, ValueError)
        return

    assert False


# testing that security levels update correctly
def test_security():
    a.set_level(0)
    b.set_level(1)
    assert (a + b).get_level() == 1
    assert (a - b).get_level() == 1
    assert (a * b).get_level() == 1
    assert (a // b).get_level() == 1
    assert (a % b).get_level() == 1
    assert (a ** b).get_level() == 1
    assert (b + 10).get_level() == 1
    assert (10 + b).get_level() == 1
    assert (2 ** b).get_level() == 1
    assert (a == b).get_level() == 1
