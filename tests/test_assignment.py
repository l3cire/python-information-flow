import ast

from pif.pif import parse_file
from pif.runtime.security_monitor import SecurityMonitor


def test_assignment_simple():
    """Tests a single assignment. No reason to fail."""
    tree = parse_file("./tests/examples/assignment_1.py")
    exec(ast.unparse(tree))

