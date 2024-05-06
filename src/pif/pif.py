import argparse
import ast
import os.path

from pif.runtime.analyzer import Analyzer

parser = argparse.ArgumentParser(
    prog="pif",
    description="PIF Transpiler"
)

parser.add_argument("-g", "--gen", dest="generate", metavar="FILENAME", help="Transpile a PIF file.")
parser.add_argument("-e", "--exec", dest="execute", metavar="FILENAME", help="Execute a PIF file.")

# Get command-line arguments
args = parser.parse_args()


def parse_file(file_name):
    with open(file_name, "r") as file:
        tree = ast.parse(file.read())
        analyzer = Analyzer()
        analyzer.visit(tree)
        ast.fix_missing_locations(tree)

    return tree


def generate(file_name):
    tree = parse_file(file_name)

    # Set up a new output file w/ -mod in the name
    base_name, ext = os.path.splitext(os.path.abspath(file_name))
    output_file_name = base_name + "-mod" + ext

    with open(output_file_name, "w+") as output_file:
        output_file.write("from pif.runtime.security_monitor import SecurityMonitor\n")
        output_file.write(ast.unparse(tree))


def execute(file_name):
    tree = parse_file(file_name)
    exec(ast.unparse(tree))


if __name__ == "__main__":
    if args.generate:
        generate(args.generate)

    elif args.execute:
        execute(args.execute)
