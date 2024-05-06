from pif.stypes.secure_bool import SecureBool
from pif.stypes.secure_num import SecureNum
from helpers import assert_val_level

a = SecureBool(True, 0)
b = SecureBool(False, 0)

n = SecureNum(1, 0)
m = SecureNum(2, 0)


# Test the normal non-specific operands. The right operands are tested later on their own.
def test_and():
    assert_val_level(a & b, False, 0)


def test_or():
    assert_val_level(b | a, True, 0)


def test_xor():
    assert_val_level(a ^ b, True, 0)


# Right operands
def test_rand():
    temp = a & False

    assert isinstance(temp, SecureBool)
    assert_val_level(temp, False, 0)


def test_ror():
    temp = False | a
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, True, 0)


def test_rxor():
    temp = True ^ a
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, False, 0)


def test_num_eq():
    temp = (n == 1)
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, True, 0)


def test_num_neq():
    temp = (n != 1)
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, False, 0)


def test_num_greater():
    temp = n > 0
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, True, 0)


def test_num_cmp():
    temp = n < m
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, True, 0)


def test_num_cmp_and():
    temp = (n == 1) and (m < 0)
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, False, 0)


def test_num_cmp_or():
    temp = (n == 1) or (m < 0)
    assert isinstance(temp, SecureBool)
    assert_val_level(temp, True, 0)


# Test SecureType interface is working properly
def test_str():
    assert a.__str__() == "True"


def test_repr():
    assert a.__repr__() == f"<SecureBool: val: True, sec: 0>"


def test_get_value():
    assert a.get_value() == True


def test_get_level():
    assert a.get_level() == 0


def test_set_value():
    a.set_value(False)
    assert a.get_value() == False
    a.set_value(True)


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
    temp = SecureBool.wrapper(a)
    assert temp is a


def test_wrapper_other():
    temp = SecureBool.wrapper(6 < 7)

    assert isinstance(temp, SecureBool)
    assert temp.get_value()
    assert temp.get_level() == 0


def test_wrapper_str():
    try:
        _ = SecureBool.wrapper("1")
    except Exception as e:
        assert isinstance(e, ValueError)
        return

    assert False


# testing that security levels update correctly
def test_security():
    a.set_level(0)
    b.set_level(1)
    assert (a | b).get_level() == 1
    assert (a & b).get_level() == 1
    assert (a ^ b).get_level() == 1
