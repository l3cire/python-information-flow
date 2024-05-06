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
