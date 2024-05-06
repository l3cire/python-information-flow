import ast

from pif.pif import parse_file
from pif.runtime.security_monitor import SecurityMonitor
from pif.runtime.security_exception import SecurityException


def test_if_fail():
    """Tests a conditional on higher security level so should fail."""
    tree = parse_file("./tests/examples/if_1.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_if_succeed():
    """Tests a conditional on low security level for assigning high -- should succeed."""
    tree = parse_file("./tests/examples/if_2.py")
    SecurityMonitor.clean()
    exec(ast.unparse(tree))


def test_if_nested_fail():
    tree = parse_file("./tests/examples/if_3.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_if_nested_succeed():
    """Tests a conditional on higher security level so should fail."""
    tree = parse_file("./tests/examples/if_4.py")
    SecurityMonitor.clean()
    exec(ast.unparse(tree))


def test_if_multiple_conditions_fail():
    tree = parse_file("./tests/examples/if_5.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_if_multiple_conditions_succeed():
    """Tests a conditional on higher security level so should fail."""
    tree = parse_file("./tests/examples/if_6.py")
    SecurityMonitor.clean()
    exec(ast.unparse(tree))


def test_elif_multiple_fail():
    tree = parse_file("./tests/examples/if_7.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_elif_succeed():
    """Tests a conditional on higher security level so should fail."""
    tree = parse_file("./tests/examples/if_8.py")
    SecurityMonitor.clean()
    exec(ast.unparse(tree))


def test_else_fail():
    tree = parse_file("./tests/examples/if_9.py")
    try:
        SecurityMonitor.clean()
        exec(ast.unparse(tree))
    except Exception as e:
        assert isinstance(e, SecurityException)
        return

    assert False


def test_else_succeed():
    """Tests a conditional on higher security level so should fail."""
    tree = parse_file("./tests/examples/if_10.py")
    SecurityMonitor.clean()
    exec(ast.unparse(tree))
