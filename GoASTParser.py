from antlr4 import *


class GoASTParser(Parser):
    class Node:

        def __init__(self, value=None, val_type=None, node_type=None) -> None:
            self.value = value
            self.type = val_type
            self.node_type = node_type
            self.children = []

        def __repr__(self) -> str:
            if len(self.children) != 0:
                return f"Node({self.value}, {self.children})"
            else:
                if self.node_type == 'FUNCCALL':
                    return f"Node({self.value}, {self.args})"
                return f"Node({self.value}, {self.type})"

    def typeChecking(self, ast):
        if ast == None:
            print("Typechecking failed!")
            return False

        return True

    def atomNode(self, val, val_type):
        node = self.Node(val, val_type, 'ATOM')
        # print(node)
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

    def IdNode(self, iden, id_type):
        node = self.Node(iden, id_type, node_type='ID')
        return

    def ifNode(self, expr, statments, else_statments=None):
        node = self.Node('if', node_type='IF')
        node.children.append(expr)
        node.children.append(statments)
        if not (else_statments is None):
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

    def funcNode(self, value, val_type, body_node):
        node = self.Node(value, val_type, node_type='FUNC')
        node.children.append(body_node)
        # print(node)
        return node

    def bodyNode(self, decl, stat):
        node = self.Node('body', node_type='BODY')
        if not (decl is None):
            node.children.append(decl)
        if not (stat is None):
            node.children.append(stat)
        return node

    def blockNode(self, new_node, block_node, node_type='BLOCK'):
        if block_node is None:
            node = self.Node(node_type)
            node.children.append(new_node)
            return node
        if len(block_node.children) <= 1:
            node = self.Node(node_type, node_type=node_type)
            node.children = [new_node, block_node]
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
        node.children.append(other.children)
        return node
