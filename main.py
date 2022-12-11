# antlr4 -Dlanguage=Python3 GoLexer.g4
# antlr4 -Dlanguage=Python3 GoParser.g4
# python main.oy input.txt
import sys
import os
from antlr4 import *
from GoLexer import GoLexer
from GoParser import GoParser
from GoASTParser import GoASTParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GoParser(stream)
    #print("START:\tLEXING AND PARSING")
    tree = parser.program()
    if tree.ast is None:
        print("------TASK FAILED SUCCESSFULLY------")
        return False

    # print("START:\tTYPCHECKING")
    # print(tree.ast)
    # print(tree.global_scope)
    parser.typeChecking(tree)
    # for token in stream.tokens:
    #    print(token)
    #a = ASTGenerator.Node('a')
    # print(a.value)
    # print(tree.toStringTree())
    #print("------CORRECT INPUT------")
    return True


if __name__ == '__main__':
    if sys.argv[1] == "test":
        print("Begin Testing\n")
        for filename in os.listdir("test"):
            print(filename)
            if not main(["main", f"test/{filename}"]) and filename != "failure.txt":
                print(f"Something wrong with {filename}")
            print()
        print("Testing Finished")
    else:
        if main(sys.argv):
            print("PARSING SUCCESSFULLY")
