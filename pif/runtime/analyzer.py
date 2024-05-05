import ast


class Analyzer(ast.NodeTransformer):
    """Class to walk the ast and enforce our security features."""
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
        return [
            ast.If(ast.BoolOp(op=ast.Or(), values=[
                ast.Compare(left=ast.Constant(value=node.targets[0].id), ops=[ast.In()],
                            comparators=[ast.Call(func=ast.Name(id='locals', ctz=ast.Load()), args=[], keywords=[])]),
                ast.Compare(left=ast.Constant(value=node.targets[0].id), ops=[ast.In()],
                            comparators=[ast.Call(func=ast.Name(id='globals', ctz=ast.Load()), args=[], keywords=[])])
            ]), body=[ast.Expr(ast.Call(
                func=ast.Attribute(
                    ast.Name("SecurityMonitor", ast.Store()),
                    'check_assignment',
                    ast.Store()
                ),
                args=[node.targets[0]],
                keywords=[],
            ))], orelse=[]),

            ast.Assign(node.targets, ast.Call(
                func=ast.Attribute(
                    ast.Name("SecurityMonitor", ast.Store()),
                    'sec_type',
                    ast.Store()
                ),
                args=[node.value],
                keywords=[]))
        ]
