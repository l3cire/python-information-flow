import ast


# This function generates the node that pushes temp on pc stack:
# SecurityMonitor.push_pc(temp)
def get_push_pc_node():
    return ast.Expr(ast.Call(
        func=ast.Attribute(
            ast.Name("SecurityMonitor", ast.Store()),
            'push_pc',
            ast.Store()
        ),
        args=[ast.Name("temp", ast.Store())],
        keywords=[]
    ))


# This function generates the node that pops the last element of pc stack:
# SecurityMonitor.pop_pc()
def get_pop_pc_node():
    return ast.Expr(ast.Call(func=ast.Attribute(
        ast.Name("SecurityMonitor", ast.Store()),
        'pop_pc',
        ast.Store()
    ),
        args=[],
        keywords=[],
    ))


# This function gets the value of temp (current condition of if/while):
# temp.get_value()
def get_temp_pc_value_node():
    return ast.Call(
        func=ast.Attribute(
            ast.Name("temp", ast.Store()),
            'get_value',
            ast.Store()
        ),
        args=[],
        keywords=[]
    )


# This function updates the value of temp (current condition of if/while) with expr:
# temp = SecurityMonitor.sec_type(expr)
def get_update_temp_pc_node(expr):
    return ast.Assign([ast.Name("temp", ast.Store())], ast.Call(
        func=ast.Attribute(
            ast.Name("SecurityMonitor", ast.Store()),
            'sec_type',
            ast.Store()
        ),
        args=[expr],
        keywords=[]))


# This function returns the node that first checks if var is in locals(),
# and if it is, runs SecurityMonitor.check_assignment(var).
# If var is not in locals(), this node checks in globals() as well
def check_assignment(var):
    return ast.If(ast.Compare(left=ast.Constant(value=var.id), ops=[ast.In()],
                              comparators=[ast.Call(func=ast.Name(id='locals', ctz=ast.Load()), args=[], keywords=[])]),
                  body=[ast.Expr(ast.Call(  # if the variable exists in locals(), we check if assignment is OK
                      func=ast.Attribute(
                          ast.Name("SecurityMonitor", ast.Store()),
                          'check_assignment',
                          ast.Store()),
                      # In check_assignment we pass the value of locals()['<variable>']
                      # This way, there are no warnings in the generated code when the variable
                      # actually doesn't exist, since we just access the dictionary by its name
                      args=[ast.Subscript(
                          ast.Call(func=ast.Name(id='locals', ctz=ast.Load()), args=[], keywords=[]),
                          ast.Constant(value=var.id), ast.Store())], keywords=[], ))],
                  # If we didn't find the variable in locals, we look for it in globals()
                  # If the variable is in globals, we do exactly the same check
                  orelse=[ast.If(ast.Compare(left=ast.Constant(value=var.id), ops=[ast.In()],
                                             comparators=[
                                                 ast.Call(func=ast.Name(id='globals', ctz=ast.Load()), args=[],
                                                          keywords=[])]),
                                 body=[ast.Expr(ast.Call(
                                     func=ast.Attribute(
                                         ast.Name("SecurityMonitor", ast.Store()),
                                         'check_assignment',
                                         ast.Store()),
                                     args=[ast.Subscript(
                                         ast.Call(func=ast.Name(id='globals', ctz=ast.Load()), args=[], keywords=[]),
                                         ast.Constant(value=var.id), ast.Store())], keywords=[])
                                 )], orelse=[])])


class Analyzer(ast.NodeTransformer):
    """Class to walk the ast and enforce our security features."""

    def visit_If(self, node):
        self.generic_visit(node)
        return [
            # First, we save the condition into a temporary variable to push it to pc
            # The condition is wrapped in SecurityMonitor.sec_type() so that it has
            # security level
            get_update_temp_pc_node(node.test),
            # Then, the condition (already being cast to SecureType), is pushed on pc stack
            get_push_pc_node(),
            # Then, the actual if statement is executing, passing temp.get_value() insight
            ast.If(
                get_temp_pc_value_node(),
                node.body,
                node.orelse),
            # Finally, after the if statement ends, the security of temp is popped
            # from the pc stack
            get_pop_pc_node()
        ]

    def visit_While(self, node):
        self.generic_visit(node)
        return [
            # First, we save the condition into a temporary variable to push it to pc
            # The condition is wrapped in SecurityMonitor.sec_type() so that it has
            # security level
            get_update_temp_pc_node(node.test),
            # Then, the condition (already being cast to SecureType), is pushed on pc stack
            get_push_pc_node(),
            # Then, the actual while statement is executing, passing temp.get_value() insight
            ast.While(
                get_temp_pc_value_node(),
                node.body + [
                    get_pop_pc_node(),
                    get_update_temp_pc_node(node.test),
                    get_push_pc_node()
                ],
                node.orelse),
            # Finally, after the if statement ends, the security of temp is popped
            # from the pc stack
            get_pop_pc_node()
        ]

    def visit_Assign(self, node):
        self.generic_visit(node)
        return [
            # First, we check if the variable we try to set was already defined before
            # To do this, we check if it is contained in locals() dictionaries
            check_assignment(node.targets[0]),
            # After the check is done, we perform the assignment, wrapping the value we assign
            # into SecurityMonitor.sec_type
            ast.Assign(node.targets, ast.Call(
                func=ast.Attribute(
                    ast.Name("SecurityMonitor", ast.Store()),
                    'sec_type',
                    ast.Store()
                ),
                args=[node.value],
                keywords=[]))
        ]
