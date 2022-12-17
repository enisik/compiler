
from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4 import *


class MyErrorListener(ConsoleErrorListener):
    def __init__(self):
        self.errors = []
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(e)
        return super().syntaxError(recognizer, offendingSymbol, line, column, msg, e)
