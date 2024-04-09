import ast


class Analyzer(ast.NodeTransformer):
    def visit_If(self, node):
        # Add the "s" attribute access here
        self.generic_visit(node)
        return [
            ast.Assign([ast.Name("temp", ast.Store())], node.test),
            ast.Expr(ast.Call(
                func=ast.Attribute(
                    ast.Name("SecurityMonitor", ast.Store()),
                    'push_pc',
                    ast.Store()
                ),
                args=[ast.Name("temp", ast.Store())],
                keywords=[]
            )),
            ast.If(
                ast.Call(
                    func=ast.Attribute(
                        ast.Name("SecurityMonitor", ast.Store()),
                        'get_val',
                        ast.Store()
                    ),
                    args=[ast.Name("temp", ast.Store())],
                    keywords=[]
                ),
                node.body,
                node.orelse),
            ast.Expr(ast.Call(
                func=ast.Attribute(
                    ast.Name("SecurityMonitor", ast.Store()),
                    'pop_pc',
                    ast.Store()
                ),
                args=[],
                keywords=[],
            ))
        ]

    def visit_Assign(self, node):
        self.generic_visit(node)
        return (ast.Assign(node.targets, ast.Call(
            func=ast.Attribute(
                ast.Name("SecurityMonitor", ast.Store()),
                'sec_type',
                ast.Store()
            ),
            args=[node.value],
            keywords=[])
                           ))


f = open('solve.py', 'r')
tree = ast.parse(f.read())

b = Analyzer()
b.visit(tree)
ast.fix_missing_locations(tree)

f2 = open('solve-mod.py', 'w')
f2.write(ast.unparse(tree))
