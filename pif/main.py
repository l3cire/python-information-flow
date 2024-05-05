import ast
import os.path
import sys

from runtime.analyzer import Analyzer

# Get command-line arguments
args = sys.argv

if len(args) != 2:
    print("Must pass a file name to the script.")
    quit(1)

file_name = args[1]
with open(file_name, 'r') as file:
    tree = ast.parse(file.read())
    analyzer = Analyzer()
    analyzer.visit(tree)
    ast.fix_missing_locations(tree)

base_name, ext = os.path.splitext(os.path.abspath(file_name))
output_file_name = base_name + "-mod" + ext

with open(output_file_name, "w+") as output_file:
    output_file.write("from pif.runtime.security_monitor import SecurityMonitor\n")
    output_file.write(ast.unparse(tree))
