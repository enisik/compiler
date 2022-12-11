from antlr4 import *


class VariableNotFound(Exception):
    pass


class TypeMismatch(Exception):
    pass


class FunctionNotFound(Exception):
    pass


class FunctionArgumentMismatch(Exception):
    pass


class GoASTParser(Parser):
    class Node:

        def __init__(self, value=None, value_type=None, node_type=None) -> None:
            self.value = value
            self.type = value_type
            self.node_type = node_type
            self.children = []

        def __repr__(self) -> str:
            if len(self.children) != 0:
                if self.node_type == 'DECL':
                    return f"Node({self.value}, {self.type}, {self.children})"
                return f"Node({self.value}, {self.children})"
            else:
                if self.node_type == 'FUNCCALL':
                    return f"Node({self.value}, {self.args})"
                return f"Node({self.value}, {self.type})"

    def typeChecking(self, tree):
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
                    raise VariableNotFound
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
                    raise FunctionNotFound
                (func_args, return_type) = tree.global_scope[func_name]
                if (node.args is None and not len(func_args) == 0) or len(func_args) != len(node.args):
                    raise FunctionArgumentMismatch
                for i in range(len(func_args)):
                    if getType(node.args[i], scope) != func_args[i][1]:
                        raise FunctionArgumentMismatch
                return return_type
            raise TypeMismatch

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
                    if not (var_type == 'FLOAT' and right_node_type == 'ATOM' and right_side_type == 'INT'):
                        raise TypeMismatch
                scope[decl.value] = decl.type

        def check_returns(func_return, returns):
            if func_return is not None and not returns:
                raise TypeMismatch

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
                        raise TypeMismatch

                elif action in ['IF', 'IF_ELSE']:
                    if getType(stmt.children[0], scope) != 'BOOL':
                        raise TypeMismatch
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
                        raise TypeMismatch
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

                        raise TypeMismatch
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

    def atomNode(self, val, value_type):
        node = self.Node(val, value_type, 'ATOM')
        return node

    def unaryNode(self, value, child_node):
        node = self.Node(value, node_type='UNARY')
        node.children.append(child_node)
        return node

    def binaryNode(self, left_node, value, right_node):
        node = self.Node(value, node_type='BINARY')
        node.children.append(left_node)
        node.children.append(right_node)
        # print(node)
        return node

    def funcCallNode(self, func_name, args):
        node = self.Node(func_name, node_type='FUNCCALL')
        node.args = args
        return node

    def idNode(self, iden, id_type):
        node = self.Node(iden, id_type, node_type='ID')
        return node

    def ifNode(self, expr, statments, else_statments=None):
        node = self.Node('if', node_type='IF')
        node.children.append(expr)
        node.children.append(statments)
        if else_statments is not None:
            node.node_type = 'IF_ELSE'
            node.children.append(else_statments)
        return node

    def forNode(self, expr, statments):
        node = self.Node('for', node_type='FOR')
        node.children.append(expr)
        node.children.append(statments)
        return node

    def returnNode(self, expr_node):
        node = self.Node('RETURN', node_type='RETURN')
        node.children.append(expr_node)
        return node

    def funcNode(self, value, value_type, body_node):
        node = self.Node(value, value_type, node_type='FUNC')
        node.children.append(body_node)
        # print(node)
        return node

    def bodyNode(self, decl, stat):
        node = self.Node('body', node_type='BODY')
        if decl is not None:
            node.children.append(decl)
        if stat is not None:
            node.children.append(stat)
        return node

    def blockNode(self, new_node, block_node, node_type='BLOCK'):
        if block_node is None:
            node = self.Node(node_type, node_type=node_type)
            node.children.append(new_node)
            return node
        block_node.children.insert(0, new_node)
        return block_node

    def declNode(self, iden, id_type, expr_node):
        node = self.Node(iden, id_type, node_type='DECL')
        node.children.append(expr_node)
        # print(node)
        return node

    def assignNode(self, iden, expr_node):
        node = self.Node(iden, node_type='ASSIGN')
        node.children.append(expr_node)
        return node

    def ast(self, main, other):
        node = self.Node('ROOT', node_type='ROOT')
        node.children.append(main)
        if other is None:
            return node
        node.children.append(*other.children)
        return node
