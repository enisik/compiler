from antlr4 import *


class GoASTParser(Parser):
    class Node:

        def __init__(self, value, val_type=None) -> None:
            self.value = value
            if val_type is None:
                self.type = type(value)
            else:
                self.type = val_type
            self.children = dict()

        def __repr__(self) -> str:
            if len(self.children) != 0:
                return f"Node({self.value}, {self.children})"
            else:
                return f"Node({self.value}, {self.type})"

    def atomNode(self, val):
        return self.Node(val)

    def unaryNode(self, value, child_node):
        node = self.atomNode(value)
        node.children['child'] = child_node
        return node

    def binaryNode(self, left_node, value, right_node):
        node = self.Node(value)
        node.children['left'] = left_node
        node.children['right'] = right_node
        return node

    def funcCallNode(self, Ids, args, type):
        pass

    def funcNode(self, value, val_type, body_node):
        node = self.Node(value, val_type)
        node.children['body'] = body_node
        print(node)
        return node

    def funcNodes(self, func, funcs):
        print(funcs)
        if funcs is None:
            print(func)
            return func
        return None
