# antlr4 -Dlanguage=Python3 GoLexer.g4
# antlr4 -no-listener -Dlanguage=Python3 GoParser.g4
# python main.py -compile input.txt
import sys
from antlr4 import *
from GoLexer import GoLexer
from GoParser import GoParser
from TypeChecker import typeChecking
from ErrorHandler import MyErrorListener
from CodeGenerator import codeGen


def parse(file):
    err_listener = MyErrorListener()

    input_stream = FileStream(file)
    lexer = GoLexer(input_stream)

    lexer.removeErrorListeners()
    lexer.addErrorListener(err_listener)

    stream = CommonTokenStream(lexer)
    parser = GoParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)
    tree = parser.program()
    if tree.ast is None or len(err_listener.errors) != 0:
        sys.exit("LEXING/PARSING/AST-GENERATING FAILED")
    print("LEXING & PARSING & AST-GENERATING SUCCESSFUL")
    typeChecking(tree)
    print("TYPECHECKING SUCCESSFUL")
    return tree


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit("too few arguments")
    filename = sys.argv[2]
    match sys.argv[1]:
        case "-compile":
            tree = parse(filename)
            code = codeGen(tree)
            filename = filename.removesuffix(".go")
            with open(filename+".j", 'w') as file:
                file.write(code)
        case "-parse":
            ast = parse(filename)
        case "-liveness":
            print("not implemented yet")
        case other:
            print("I don't know what to do")
