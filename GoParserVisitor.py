# Generated from GoParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GoParser import GoParser
else:
    from GoParser import GoParser

# This class defines a complete generic visitor for a parse tree produced by GoParser.

class GoParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GoParser#program.
    def visitProgram(self, ctx:GoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#main_function.
    def visitMain_function(self, ctx:GoParser.Main_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#functions.
    def visitFunctions(self, ctx:GoParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#function.
    def visitFunction(self, ctx:GoParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#body.
    def visitBody(self, ctx:GoParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#func_args.
    def visitFunc_args(self, ctx:GoParser.Func_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#type.
    def visitType(self, ctx:GoParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#declarations.
    def visitDeclarations(self, ctx:GoParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#declaration.
    def visitDeclaration(self, ctx:GoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#statements.
    def visitStatements(self, ctx:GoParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#statement.
    def visitStatement(self, ctx:GoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#block_stmt.
    def visitBlock_stmt(self, ctx:GoParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#assignment.
    def visitAssignment(self, ctx:GoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#if_control.
    def visitIf_control(self, ctx:GoParser.If_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#for_control.
    def visitFor_control(self, ctx:GoParser.For_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#func_call.
    def visitFunc_call(self, ctx:GoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#expr.
    def visitExpr(self, ctx:GoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#literals.
    def visitLiterals(self, ctx:GoParser.LiteralsContext):
        return self.visitChildren(ctx)



del GoParser