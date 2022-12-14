import sys


def typeChecking(tree):
    numeric_type = ['INT', 'FLOAT']
    numeric_ops = ['+', '-', '*', '/', '%']
    bool_ops = ['!', '&&', '||']
    check_ops = ['==', '!=']
    comparison_ops = ['<', '>', '<=', '>=']

    def getType(node, scope):
        node_type = node.node_type
        if node_type == 'ATOM':
            return node.type
        elif node_type == 'ID':
            if node.value not in scope:
                sys.exit("variable not found in scope")
            return scope[node.value]
        elif node_type == 'UNARY':
            return getUnaryType(node, scope)
        elif node_type == 'BINARY':
            return getBinaryType(node, scope)
        elif node_type == 'FUNCCALL':
            func_name = node.value
            if func_name == "fmt.Println":
                return None
            if func_name not in tree.global_scope:
                sys.exit("function not found")
            (func_args, return_type) = tree.global_scope[func_name]
            if node.args is None and func_args is None:
                return return_type
            if node.args is None and func_args is not None:
                sys.exit("FunctionArgumentMismatch")
            elif node.args is not None and func_args is None:
                sys.exit("FunctionArgumentMismatch")
            elif len(node.args) != len(func_args):
                sys.exit("FunctionArgumentMismatch")
            for i in range(len(func_args)):
                if getType(node.args[i], scope) != func_args[i][1]:
                    sys.exit("FunctionArgumentMismatch")
            return return_type
        sys.exit("TypeMismatch")

    def getUnaryType(node, scope):
        if node.value == '-':
            arg_type = getType(node.children[0], scope)
            if arg_type in numeric_type:
                return arg_type
        elif node.value == '+':
            arg_type = getType(node.children[0], scope)
            if arg_type in numeric_type:
                return arg_type
        if node.value == '!':
            arg_type = getType(node.children[0], scope)
            if arg_type == 'BOOL':
                return arg_type

    def getBinaryType(node, scope):
        if node.value in numeric_ops:
            left_side = getType(node.children[0], scope)
            right_side = getType(node.children[1], scope)
            if left_side == right_side:
                if left_side in numeric_type:
                    return right_side
                if node.value == '+' and left_side == 'STRING':
                    return right_side

        elif node.value in bool_ops:
            left_side = getType(node.children[0], scope)
            right_side = getType(node.children[1], scope)
            if left_side == right_side and left_side == 'BOOL':
                return right_side

        elif node.value in check_ops:
            left_side = getType(node.children[0], scope)
            right_side = getType(node.children[1], scope)
            if left_side == right_side:
                return right_side

        elif node.value in comparison_ops:
            left_side = getType(node.children[0], scope)
            right_side = getType(node.children[1], scope)
            if left_side == right_side and (left_side in numeric_type) or left_side == 'BOOL':
                return 'BOOL'

    def get_scope(name):
        func_info = tree.global_scope[name]
        if func_info[0] is None:
            return dict()
        else:
            return dict(func_info[0])

    def check_decl(declarations, scope):
        for decl in declarations:
            var_type = decl.type
            right_side = decl.children[0]
            right_node_type = right_side.node_type
            right_side_type = getType(right_side, scope)

            if var_type != right_side_type:
                if var_type == 'FLOAT':
                    if right_node_type != 'ATOM' or right_side_type != 'INT':
                        sys.exit(
                            "float mismatch; right side is not float or int literal")
                else:
                    sys.exit("TYPE MISMATCH")
            scope[decl.value] = decl.type

    def check_returns(func_return, returns):
        if func_return is not None and not returns:
            sys.exit("check returns failed")

    def check_stmts(statemants, scope, func_return):
        returns = False
        if not isinstance(statemants, list):
            statemants = statemants.children
        for stmt in statemants:
            action = stmt.node_type

            if action == "ASSIGN":
                var_type = scope[stmt.value]
                right_side = getType(stmt.children[0], scope)
                if var_type != right_side:
                    sys.exit("left and right side mismatch")

            elif action in ['IF', 'IF_ELSE']:
                if getType(stmt.children[0], scope) != 'BOOL':
                    sys.exit("if argument not bool")
                stmts1 = stmt.children[1]
                if stmts1 is not None:
                    returns = check_stmts(stmts1, scope, func_return)
                    check_returns(func_return, returns)
                if action == 'IF_ELSE':
                    stmts2 = stmt.children[2]
                    if stmts2 is not None:
                        returns = check_stmts(
                            stmts2, scope, func_return)
                        check_returns(func_return, returns)

            elif action == "FOR":
                if getType(stmt.children[0], scope) != 'BOOL':
                    sys.exit("for argument not bool")
                for_stmt = stmt.children[1]
                if for_stmt is not None:
                    returns = check_stmts(for_stmt, scope, func_return)
                    check_returns(func_return, returns)

            elif action == "RETURN":
                right_side = stmt.children[0]
                if right_side is None:
                    right_side_type = None
                else:
                    right_side_type = getType(stmt.children[0], scope)
                if right_side_type != func_return:

                    sys.exit("return argument mismatch")
                return True

            elif action == "FUNCCALL":
                getType(stmt, scope)

            elif action == "STMT":
                check_stmts(stmt.children, scope, func_return)

        return returns

    ast = tree.ast
    if ast == None:
        print("Typechecking failed!")
        return False
    for func in ast.children:
        func_scope = get_scope(func.value)
        if len(func.children) != 1:
            print("Function doesnt have body :(")
        body = func.children[0].children
        func_return = tree.global_scope[func.value][1]
        for block in body:
            node_type = block.node_type
            if node_type == "DECL":
                check_decl(block.children, func_scope)
            if node_type == "STMT":
                check_stmts(block.children, func_scope, func_return)
    return True
