from antlr4 import *


class GoASTParser(Parser):
    class Node:

        def __init__(self, value) -> None:
            self.value = value
            self.type = type(value)

        def __repr__(self) -> str:
            return str(f"Node({self.value}, {self.type})")

    def node(self, val):
        return self.Node(val)
