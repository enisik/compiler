# antlr4 -Dlanguage=Python3 GoLexer.g4
# antlr4 -no-listener -Dlanguage=Python3 GoParser.g4
# python main.py input.txt
import sys
from antlr4 import *
from GoLexer import GoLexer
from GoParser import GoParser
from TypeChecker import typeChecking
from ErrorHandler import MyErrorStrategy


def main(file):
    input_stream = FileStream(file)
    lexer = GoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GoParser(stream)
    parser._errHandler = MyErrorStrategy()
    tree = parser.program()
    print(f"PARSING ERRORS: {parser._errHandler.errors}")
    if tree.ast is None:  # or len(parser._errHandler.errors) != 0:
        sys.exit("----PARSING/AST-GENERATING FAILED----")
    print("----PARSING/AST-GENERATING SUCCESSFUL----")
    typeChecking(tree)
    print("----TYPECHECKING SUCCESSFUL----")


if __name__ == '__main__':

    match sys.argv[1]:
        case "-compile":
            main(sys.argv[2])
        case "-liveness":
            print("not implemented yet")
        case other:
            print("I don't know what to do")
