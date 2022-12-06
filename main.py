# antlr4 -Dlanguage=Python3 GoLexer.g4
# antlr4 -Dlanguage=Python3 GoParser.g4
# python main.oy input.txt
import sys
from antlr4 import *
from GoLexer import GoLexer
from GoParser import GoParser
import antlr4


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GoParser(stream)
    tree = parser.program()
    return tree, stream


if __name__ == '__main__':
    tree, stream = main(sys.argv)
    # for token in stream.tokens:
    # print(token)
    print(tree.toStringTree())
