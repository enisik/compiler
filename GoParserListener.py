# Generated from GoParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GoParser import GoParser
else:
    from GoParser import GoParser

# This class defines a complete listener for a parse tree produced by GoParser.
class GoParserListener(ParseTreeListener):

    # Enter a parse tree produced by GoParser#program.
    def enterProgram(self, ctx:GoParser.ProgramContext):
        pass

    # Exit a parse tree produced by GoParser#program.
    def exitProgram(self, ctx:GoParser.ProgramContext):
        pass


    # Enter a parse tree produced by GoParser#main_method.
    def enterMain_method(self, ctx:GoParser.Main_methodContext):
        pass

    # Exit a parse tree produced by GoParser#main_method.
    def exitMain_method(self, ctx:GoParser.Main_methodContext):
        pass


    # Enter a parse tree produced by GoParser#methods.
    def enterMethods(self, ctx:GoParser.MethodsContext):
        pass

    # Exit a parse tree produced by GoParser#methods.
    def exitMethods(self, ctx:GoParser.MethodsContext):
        pass


    # Enter a parse tree produced by GoParser#body.
    def enterBody(self, ctx:GoParser.BodyContext):
        pass

    # Exit a parse tree produced by GoParser#body.
    def exitBody(self, ctx:GoParser.BodyContext):
        pass


    # Enter a parse tree produced by GoParser#func_args.
    def enterFunc_args(self, ctx:GoParser.Func_argsContext):
        pass

    # Exit a parse tree produced by GoParser#func_args.
    def exitFunc_args(self, ctx:GoParser.Func_argsContext):
        pass


    # Enter a parse tree produced by GoParser#type.
    def enterType(self, ctx:GoParser.TypeContext):
        pass

    # Exit a parse tree produced by GoParser#type.
    def exitType(self, ctx:GoParser.TypeContext):
        pass


    # Enter a parse tree produced by GoParser#declarations.
    def enterDeclarations(self, ctx:GoParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by GoParser#declarations.
    def exitDeclarations(self, ctx:GoParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by GoParser#declaration.
    def enterDeclaration(self, ctx:GoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GoParser#declaration.
    def exitDeclaration(self, ctx:GoParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GoParser#statements.
    def enterStatements(self, ctx:GoParser.StatementsContext):
        pass

    # Exit a parse tree produced by GoParser#statements.
    def exitStatements(self, ctx:GoParser.StatementsContext):
        pass


    # Enter a parse tree produced by GoParser#statement.
    def enterStatement(self, ctx:GoParser.StatementContext):
        pass

    # Exit a parse tree produced by GoParser#statement.
    def exitStatement(self, ctx:GoParser.StatementContext):
        pass


    # Enter a parse tree produced by GoParser#expr.
    def enterExpr(self, ctx:GoParser.ExprContext):
        pass

    # Exit a parse tree produced by GoParser#expr.
    def exitExpr(self, ctx:GoParser.ExprContext):
        pass


    # Enter a parse tree produced by GoParser#opt_return.
    def enterOpt_return(self, ctx:GoParser.Opt_returnContext):
        pass

    # Exit a parse tree produced by GoParser#opt_return.
    def exitOpt_return(self, ctx:GoParser.Opt_returnContext):
        pass


    # Enter a parse tree produced by GoParser#literals.
    def enterLiterals(self, ctx:GoParser.LiteralsContext):
        pass

    # Exit a parse tree produced by GoParser#literals.
    def exitLiterals(self, ctx:GoParser.LiteralsContext):
        pass


    # Enter a parse tree produced by GoParser#if_control.
    def enterIf_control(self, ctx:GoParser.If_controlContext):
        pass

    # Exit a parse tree produced by GoParser#if_control.
    def exitIf_control(self, ctx:GoParser.If_controlContext):
        pass


    # Enter a parse tree produced by GoParser#for_control.
    def enterFor_control(self, ctx:GoParser.For_controlContext):
        pass

    # Exit a parse tree produced by GoParser#for_control.
    def exitFor_control(self, ctx:GoParser.For_controlContext):
        pass



del GoParser