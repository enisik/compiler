# antlr4 -Dlanguage=Python3 GoLexer.g4
# antlr4 -no-listener -Dlanguage=Python3 GoParser.g4
# python main.py input.txt
import sys
import os
from antlr4 import *
from GoLexer import GoLexer
from GoParser import GoParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GoParser(stream)
    tree = parser.program()
    if tree.ast is None:
        print("PAST-GENERATING FAILED")
        return
    parser.typeChecking(tree)
    print("PARSING & TYPECHECKING SUCCESSFUL")


if __name__ == '__main__':

    if sys.argv[1] == "test":
        print("Begin Testing\n")
        for filename in os.listdir("test"):
            print(filename)
            main(["main", f"test/{filename}"])
        print("Testing Finished")
    else:
        main(sys.argv)
