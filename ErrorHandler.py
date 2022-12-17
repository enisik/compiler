
from antlr4 import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy


class MyErrorStrategy(DefaultErrorStrategy):
    def __init__(self):
        self.errors = []
        super().__init__()

    def recover(self, recognizer: Parser, e: RecognitionException):
        #recognizer._errHandler.reportError(recognizer, e)
        self.errors.append(e)
        #uper().recover(recognizer, e)
