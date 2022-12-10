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


    # Enter a parse tree produced by GoParser#main_function.
    def enterMain_function(self, ctx:GoParser.Main_functionContext):
        pass

    # Exit a parse tree produced by GoParser#main_function.
    def exitMain_function(self, ctx:GoParser.Main_functionContext):
        pass


    # Enter a parse tree produced by GoParser#functions.
    def enterFunctions(self, ctx:GoParser.FunctionsContext):
        pass

    # Exit a parse tree produced by GoParser#functions.
    def exitFunctions(self, ctx:GoParser.FunctionsContext):
        pass


    # Enter a parse tree produced by GoParser#function.
    def enterFunction(self, ctx:GoParser.FunctionContext):
        pass

    # Exit a parse tree produced by GoParser#function.
    def exitFunction(self, ctx:GoParser.FunctionContext):
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


    # Enter a parse tree produced by GoParser#block_stmt.
    def enterBlock_stmt(self, ctx:GoParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by GoParser#block_stmt.
    def exitBlock_stmt(self, ctx:GoParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by GoParser#assignment.
    def enterAssignment(self, ctx:GoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GoParser#assignment.
    def exitAssignment(self, ctx:GoParser.AssignmentContext):
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


    # Enter a parse tree produced by GoParser#func_call.
    def enterFunc_call(self, ctx:GoParser.Func_callContext):
        pass

    # Exit a parse tree produced by GoParser#func_call.
    def exitFunc_call(self, ctx:GoParser.Func_callContext):
        pass


    # Enter a parse tree produced by GoParser#expr.
    def enterExpr(self, ctx:GoParser.ExprContext):
        pass

    # Exit a parse tree produced by GoParser#expr.
    def exitExpr(self, ctx:GoParser.ExprContext):
        pass


    # Enter a parse tree produced by GoParser#literals.
    def enterLiterals(self, ctx:GoParser.LiteralsContext):
        pass

    # Exit a parse tree produced by GoParser#literals.
    def exitLiterals(self, ctx:GoParser.LiteralsContext):
        pass



del GoParser