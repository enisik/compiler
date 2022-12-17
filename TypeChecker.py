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
                sys.exit(f"VARIABLE {node.value} NOT FOUND")
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
                sys.exit(f"FUNCTION {func_name} NOT DEFINED")
            (func_args, return_type) = tree.global_scope[func_name]
            if node.args is None and func_args is None:
                return return_type
            if node.args is None and func_args is not None:
                sys.exit("FUNCTION ARGUMENT MISMATCH")
            elif node.args is not None and func_args is None:
                sys.exit("FUNCTION ARGUMENT MISMATCH")
            elif len(node.args) != len(func_args):
                sys.exit("FUNCTION ARGUMENT MISMATCH")
            for i in range(len(func_args)):
                func_arg = func_args[i][1]
                node_arg_type = getType(node.args[i], scope)
                if node_arg_type != func_arg:
                    if func_arg == 'FLOAT' and node_arg_type == 'INT' and node.args[i].is_pure:
                        continue
                    sys.exit(
                        f"FUNCTION ARGUMENT MISMATCH\nEXPECTED: {func_arg.value}\tGOT: {node.args[i].value}")
            return return_type
        sys.exit("TYPE MISMATCH")

    def getUnaryType(node, scope):
        argument = node.children[0]
        arg_type = getType(argument, scope)

        if argument.is_pure:
            node.is_pure = True

        if node.value == '-':
            if arg_type in numeric_type:
                return arg_type
        elif node.value == '+':
            if arg_type in numeric_type:
                return arg_type
        if node.value == '!':
            if arg_type == 'BOOL':
                return arg_type
        sys.exit(
            f"OPERATOR MISMATCH\nOPERATOR: {node.value}\tARGUMENT: {argument.value}")

    def getBinaryType(node, scope):
        left_expr = node.children[0]
        right_expr = node.children[1]
        left_type = getType(left_expr, scope)
        right_type = getType(right_expr, scope)

        if left_expr.is_pure and right_expr.is_pure:
            node.is_pure = True

        if node.value == '%':
            if left_type == 'FLOAT' or right_type == 'FLOAT':
                sys.exit("CAN'T MODULO FLOAT")

        if node.value in numeric_ops:
            if left_type == right_type:
                if left_type in numeric_type:
                    return right_type
                if node.value == '+' and left_type == 'STRING':
                    return right_type

        elif node.value in bool_ops:
            if left_type == right_type and left_type == 'BOOL':
                return 'BOOL'

        elif node.value in check_ops:
            if left_type == right_type:
                return 'BOOL'

        elif node.value in comparison_ops:
            if left_type == right_type and (left_type in numeric_type) or left_type == 'BOOL':
                return 'BOOL'
        sys.exit(
            f"OPERATOR MISMATCH\nLEFT: {left_expr.value}\t Operator: {node.value}\t RIGHT: {right_expr.value}")

    def get_scope(name):
        func_info = tree.global_scope[name]
        if func_info[0] is None:
            return dict()
        else:
            return dict(func_info[0])

    def check_decl(declarations, scope):
        for decl in declarations:
            var_type = decl.type
            right_node = decl.children[0]
            right_side_type = getType(right_node, scope)

            if var_type != right_side_type:
                if var_type == 'FLOAT':
                    if not right_node.is_pure or right_side_type != 'INT':
                        sys.exit(
                            f"DECLARATION TYPE MISTMATCH\nLEFT: {var_type}\tRIGHT: {right_side_type}")
                else:
                    sys.exit(
                        f"DECLARATION TYPE MISTMATCH\nLEFT:{var_type}\tRIGHT:{right_side_type}")
            if decl.value in scope:
                sys.exit(f"REDECLARATION ERROR\n{decl.value} already declared")
            scope[decl.value] = decl.type

    # def check_returns(func_return, returns):
    #    if func_return is not None and not returns:
    #        sys.exit("RETURNS CHECK FAILED")

    def check_stmts(statemants, scope, func_return):
        returns = False
        if not isinstance(statemants, list):
            statemants = statemants.children
        for stmt in statemants:
            action = stmt.node_type

            if action == "ASSIGN":
                if stmt.value not in scope:
                    sys.exit(f"VARIABLE NOT FOUND\n{stmt.value}")
                var_type = scope[stmt.value]
                right_side = getType(stmt.children[0], scope)
                if var_type != right_side:
                    sys.exit(
                        f"TYPE MISTMATCH\nLEFT:{var_type}\tRIGHT:{right_side}")

            elif action in ['IF', 'IF_ELSE']:
                if getType(stmt.children[0], scope) != 'BOOL':
                    sys.exit("IF ARGUMENT IS NOT BOOL")
                stmts1 = stmt.children[1]
                if stmts1 is not None:
                    returns = check_stmts(stmts1, scope, func_return)
                    #check_returns(func_return, returns)
                if action == 'IF_ELSE':
                    stmts2 = stmt.children[2]
                    if stmts2 is not None:
                        returns = check_stmts(
                            stmts2, scope, func_return)
                        #check_returns(func_return, returns)

            elif action == "FOR":
                if getType(stmt.children[0], scope) != 'BOOL':
                    sys.exit("FOR ARGUMENT IS NOT BOOL")
                for_stmt = stmt.children[1]
                if for_stmt is not None:
                    returns = check_stmts(for_stmt, scope, func_return)
                    #check_returns(func_return, returns)

            elif action == "RETURN":
                right_node = stmt.children[0]
                if right_node is None:
                    right_node_type = None
                else:
                    right_node_type = getType(stmt.children[0], scope)
                if right_node_type != func_return:

                    sys.exit(
                        f"RETURN ARGUMENT TYPE MISMATCH\nRETURN:{right_node_type}\tFUNCTION RETURN TYPE:{func_return}")
                return True

            elif action == "FUNCCALL":
                getType(stmt, scope)

            elif action == "STMT":
                check_stmts(stmt.children, scope, func_return)

        return returns

    ast = tree.ast
    if ast == None:
        sys.exit("CAN'T TYPCHECK EMPTY AST")
    for func in ast.children:
        func_scope = get_scope(func.value)
        body = func.children[0].children
        func_return = tree.global_scope[func.value][1]
        for block in body:
            node_type = block.node_type
            if node_type == "DECL":
                check_decl(block.children, func_scope)
            if node_type == "STMT":
                check_stmts(block.children, func_scope, func_return)
    return True
