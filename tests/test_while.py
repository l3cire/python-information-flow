import ast

from pif.pif import parse_file
from pif.runtime.security_monitor import SecurityMonitor
from pif.runtime.security_exception import SecurityException


def test_while_fail():
    """Tests a conditional (while) on higher security level so should fail."""
    tree = parse_file("./tests/examples/while_1.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_while_succeed():
    """Tests a conditional (while) on higher security level so should fail."""
    tree = parse_file("./tests/examples/while_2.py")
    SecurityMonitor.clean()
    exec(ast.unparse(tree))


def test_while_end_fail():
    """Modifies low security variable at the vary last iteration (condition is high sec) -- should fail"""
    tree = parse_file("./tests/examples/while_3.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_while_else_fail():
    tree = parse_file("./tests/examples/while_4.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_while_else_succeed():
    tree = parse_file("./tests/examples/while_5.py")
    SecurityMonitor.clean()
    exec(ast.unparse(tree))


def test_while_mod_cond_while_fail():
    tree = parse_file("./tests/examples/while_6.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False
