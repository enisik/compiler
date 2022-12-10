# Generated from GoParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if __name__ is not None and "." in __name__:
    from .GoASTParser import GoASTParser
else:
    from GoASTParser import GoASTParser

def serializedATN():
    return [
        4,1,42,321,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,1,0,
        5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,0,1,0,3,0,52,8,0,1,0,3,0,55,
        8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,1,3,1,68,8,1,1,
        1,1,1,3,1,72,8,1,1,1,1,1,3,1,76,8,1,1,1,1,1,1,2,1,2,1,2,3,2,83,8,
        2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,91,8,3,1,3,1,3,3,3,95,8,3,1,3,3,3,
        98,8,3,1,3,1,3,3,3,102,8,3,1,3,1,3,3,3,106,8,3,1,3,1,3,1,3,1,4,1,
        4,1,4,3,4,114,8,4,1,4,5,4,117,8,4,10,4,12,4,120,9,4,1,4,3,4,123,
        8,4,1,5,1,5,1,5,1,5,1,5,5,5,130,8,5,10,5,12,5,133,9,5,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,3,7,142,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,3,9,155,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,164,
        8,10,1,11,1,11,3,11,168,8,11,1,11,3,11,171,8,11,1,11,3,11,174,8,
        11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,185,8,13,1,
        13,1,13,3,13,189,8,13,1,13,3,13,192,8,13,1,13,3,13,195,8,13,1,13,
        1,13,3,13,199,8,13,1,13,1,13,3,13,203,8,13,1,13,1,13,3,13,207,8,
        13,1,13,3,13,210,8,13,1,13,3,13,213,8,13,1,13,1,13,1,13,1,13,1,13,
        3,13,220,8,13,1,13,1,13,3,13,224,8,13,1,13,3,13,227,8,13,1,13,1,
        13,3,13,231,8,13,1,14,1,14,1,14,3,14,236,8,14,1,14,1,14,3,14,240,
        8,14,1,14,3,14,243,8,14,1,14,3,14,246,8,14,1,14,1,14,1,15,1,15,1,
        15,5,15,253,8,15,10,15,12,15,256,9,15,1,15,1,15,1,15,1,15,5,15,262,
        8,15,10,15,12,15,265,9,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,284,8,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,5,16,306,8,16,10,16,12,16,309,9,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,319,8,17,1,17,0,1,32,
        18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,6,1,0,9,12,
        2,0,13,14,26,26,1,0,15,17,1,0,13,14,1,0,18,23,1,0,24,25,359,0,36,
        1,0,0,0,2,58,1,0,0,0,4,79,1,0,0,0,6,86,1,0,0,0,8,113,1,0,0,0,10,
        124,1,0,0,0,12,134,1,0,0,0,14,141,1,0,0,0,16,143,1,0,0,0,18,154,
        1,0,0,0,20,163,1,0,0,0,22,165,1,0,0,0,24,177,1,0,0,0,26,230,1,0,
        0,0,28,232,1,0,0,0,30,249,1,0,0,0,32,283,1,0,0,0,34,318,1,0,0,0,
        36,37,5,4,0,0,37,38,5,42,0,0,38,39,4,0,0,1,39,44,5,31,0,0,40,41,
        5,5,0,0,41,43,5,30,0,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,
        44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,5,31,0,0,48,51,3,
        2,1,0,49,50,5,31,0,0,50,52,3,4,2,0,51,49,1,0,0,0,51,52,1,0,0,0,52,
        54,1,0,0,0,53,55,5,31,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,1,0,
        0,0,56,57,5,0,0,1,57,1,1,0,0,0,58,59,5,3,0,0,59,60,5,42,0,0,60,61,
        4,1,1,1,61,62,5,32,0,0,62,64,5,33,0,0,63,65,3,12,6,0,64,63,1,0,0,
        0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,5,31,0,0,67,66,1,0,0,0,67,68,
        1,0,0,0,68,69,1,0,0,0,69,71,5,34,0,0,70,72,5,31,0,0,71,70,1,0,0,
        0,71,72,1,0,0,0,72,73,1,0,0,0,73,75,3,8,4,0,74,76,5,31,0,0,75,74,
        1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,35,0,0,78,3,1,0,0,0,
        79,82,3,6,3,0,80,81,5,31,0,0,81,83,3,4,2,0,82,80,1,0,0,0,82,83,1,
        0,0,0,83,84,1,0,0,0,84,85,6,2,-1,0,85,5,1,0,0,0,86,87,5,3,0,0,87,
        88,5,42,0,0,88,90,5,32,0,0,89,91,3,10,5,0,90,89,1,0,0,0,90,91,1,
        0,0,0,91,92,1,0,0,0,92,94,5,33,0,0,93,95,3,12,6,0,94,93,1,0,0,0,
        94,95,1,0,0,0,95,97,1,0,0,0,96,98,5,31,0,0,97,96,1,0,0,0,97,98,1,
        0,0,0,98,99,1,0,0,0,99,101,5,34,0,0,100,102,5,31,0,0,101,100,1,0,
        0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,105,3,8,4,0,104,106,5,31,
        0,0,105,104,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,35,
        0,0,108,109,6,3,-1,0,109,7,1,0,0,0,110,111,3,14,7,0,111,112,5,31,
        0,0,112,114,1,0,0,0,113,110,1,0,0,0,113,114,1,0,0,0,114,118,1,0,
        0,0,115,117,5,31,0,0,116,115,1,0,0,0,117,120,1,0,0,0,118,116,1,0,
        0,0,118,119,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,121,123,3,18,
        9,0,122,121,1,0,0,0,122,123,1,0,0,0,123,9,1,0,0,0,124,125,5,42,0,
        0,125,131,3,12,6,0,126,127,5,36,0,0,127,128,5,42,0,0,128,130,3,12,
        6,0,129,126,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,
        0,0,132,11,1,0,0,0,133,131,1,0,0,0,134,135,7,0,0,0,135,13,1,0,0,
        0,136,137,3,16,8,0,137,138,5,31,0,0,138,139,3,14,7,0,139,142,1,0,
        0,0,140,142,3,16,8,0,141,136,1,0,0,0,141,140,1,0,0,0,142,15,1,0,
        0,0,143,144,5,1,0,0,144,145,5,42,0,0,145,146,3,12,6,0,146,147,5,
        39,0,0,147,148,3,32,16,0,148,17,1,0,0,0,149,150,3,20,10,0,150,151,
        5,31,0,0,151,152,3,18,9,0,152,155,1,0,0,0,153,155,3,20,10,0,154,
        149,1,0,0,0,154,153,1,0,0,0,155,19,1,0,0,0,156,164,3,24,12,0,157,
        164,3,22,11,0,158,164,3,26,13,0,159,164,3,28,14,0,160,164,3,30,15,
        0,161,162,5,2,0,0,162,164,3,32,16,0,163,156,1,0,0,0,163,157,1,0,
        0,0,163,158,1,0,0,0,163,159,1,0,0,0,163,160,1,0,0,0,163,161,1,0,
        0,0,164,21,1,0,0,0,165,167,5,34,0,0,166,168,5,31,0,0,167,166,1,0,
        0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,171,3,18,9,0,170,169,1,0,
        0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,174,5,31,0,0,173,172,1,0,
        0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,176,5,35,0,0,176,23,1,0,
        0,0,177,178,5,42,0,0,178,179,5,39,0,0,179,180,3,32,16,0,180,25,1,
        0,0,0,181,182,5,6,0,0,182,184,3,32,16,0,183,185,5,31,0,0,184,183,
        1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,188,5,34,0,0,187,189,
        5,31,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,192,
        3,18,9,0,191,190,1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,195,
        5,31,0,0,194,193,1,0,0,0,194,195,1,0,0,0,195,196,1,0,0,0,196,198,
        5,35,0,0,197,199,5,31,0,0,198,197,1,0,0,0,198,199,1,0,0,0,199,200,
        1,0,0,0,200,202,5,7,0,0,201,203,5,31,0,0,202,201,1,0,0,0,202,203,
        1,0,0,0,203,204,1,0,0,0,204,206,5,34,0,0,205,207,5,31,0,0,206,205,
        1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,210,3,18,9,0,209,208,
        1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,213,5,31,0,0,212,211,
        1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,215,5,35,0,0,215,231,
        1,0,0,0,216,217,5,6,0,0,217,219,3,32,16,0,218,220,5,31,0,0,219,218,
        1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,223,5,34,0,0,222,224,
        5,31,0,0,223,222,1,0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,225,227,
        3,18,9,0,226,225,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,228,229,
        5,35,0,0,229,231,1,0,0,0,230,181,1,0,0,0,230,216,1,0,0,0,231,27,
        1,0,0,0,232,233,5,8,0,0,233,235,3,32,16,0,234,236,5,31,0,0,235,234,
        1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,0,237,239,5,34,0,0,238,240,
        5,31,0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,243,
        3,18,9,0,242,241,1,0,0,0,242,243,1,0,0,0,243,245,1,0,0,0,244,246,
        5,31,0,0,245,244,1,0,0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,248,
        5,35,0,0,248,29,1,0,0,0,249,254,5,42,0,0,250,251,5,37,0,0,251,253,
        5,42,0,0,252,250,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,
        1,0,0,0,255,257,1,0,0,0,256,254,1,0,0,0,257,258,5,32,0,0,258,263,
        3,32,16,0,259,260,5,36,0,0,260,262,3,32,16,0,261,259,1,0,0,0,262,
        265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,266,1,0,0,0,265,
        263,1,0,0,0,266,267,5,33,0,0,267,31,1,0,0,0,268,269,6,16,-1,0,269,
        284,5,42,0,0,270,284,3,30,15,0,271,272,3,34,17,0,272,273,6,16,-1,
        0,273,284,1,0,0,0,274,275,5,32,0,0,275,276,3,32,16,0,276,277,5,33,
        0,0,277,278,6,16,-1,0,278,284,1,0,0,0,279,280,7,1,0,0,280,281,3,
        32,16,5,281,282,6,16,-1,0,282,284,1,0,0,0,283,268,1,0,0,0,283,270,
        1,0,0,0,283,271,1,0,0,0,283,274,1,0,0,0,283,279,1,0,0,0,284,307,
        1,0,0,0,285,286,10,4,0,0,286,287,7,2,0,0,287,288,3,32,16,5,288,289,
        6,16,-1,0,289,306,1,0,0,0,290,291,10,3,0,0,291,292,7,3,0,0,292,293,
        3,32,16,4,293,294,6,16,-1,0,294,306,1,0,0,0,295,296,10,2,0,0,296,
        297,7,4,0,0,297,298,3,32,16,3,298,299,6,16,-1,0,299,306,1,0,0,0,
        300,301,10,1,0,0,301,302,7,5,0,0,302,303,3,32,16,2,303,304,6,16,
        -1,0,304,306,1,0,0,0,305,285,1,0,0,0,305,290,1,0,0,0,305,295,1,0,
        0,0,305,300,1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,307,308,1,0,
        0,0,308,33,1,0,0,0,309,307,1,0,0,0,310,311,5,27,0,0,311,319,6,17,
        -1,0,312,313,5,30,0,0,313,319,6,17,-1,0,314,315,5,28,0,0,315,319,
        6,17,-1,0,316,317,5,29,0,0,317,319,6,17,-1,0,318,310,1,0,0,0,318,
        312,1,0,0,0,318,314,1,0,0,0,318,316,1,0,0,0,319,35,1,0,0,0,46,44,
        51,54,64,67,71,75,82,90,94,97,101,105,113,118,122,131,141,154,163,
        167,170,173,184,188,191,194,198,202,206,209,212,219,223,226,230,
        235,239,242,245,254,263,283,305,307,318
    ]

class GoParser ( GoASTParser ):

    grammarFileName = "GoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'return'", "'func'", "'package'", 
                     "'import'", "'if'", "'else'", "'for'", "'int'", "'float64'", 
                     "'bool'", "'string'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", 
                     "'||'", "'!'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "','", "'.'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "VAR", "RETURN", "FUNC", "PACKAGE", "IMPORT", 
                      "IF", "ELSE", "FOR", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "STRING_TYPE", "PLUS", "MINUS", "STAR", "DIVISON", 
                      "MODULO", "EQUALS", "UNEQUAL", "LESS", "GREATER", 
                      "LESSEQUAL", "GREATEREQUAL", "AND", "OR", "NOT", "INTEGER", 
                      "FLOAT", "BOOL", "STRING", "NL", "LB", "RB", "CLB", 
                      "CRB", "COMMA", "DOT", "SEMICOLON", "ASSIGN", "WHITESPACE", 
                      "COMMENT", "IDENTIFIER" ]

    RULE_program = 0
    RULE_main_function = 1
    RULE_functions = 2
    RULE_function = 3
    RULE_body = 4
    RULE_func_args = 5
    RULE_type = 6
    RULE_declarations = 7
    RULE_declaration = 8
    RULE_statements = 9
    RULE_statement = 10
    RULE_block_stmt = 11
    RULE_assignment = 12
    RULE_if_control = 13
    RULE_for_control = 14
    RULE_func_call = 15
    RULE_expr = 16
    RULE_literals = 17

    ruleNames =  [ "program", "main_function", "functions", "function", 
                   "body", "func_args", "type", "declarations", "declaration", 
                   "statements", "statement", "block_stmt", "assignment", 
                   "if_control", "for_control", "func_call", "expr", "literals" ]

    EOF = Token.EOF
    VAR=1
    RETURN=2
    FUNC=3
    PACKAGE=4
    IMPORT=5
    IF=6
    ELSE=7
    FOR=8
    INT_TYPE=9
    FLOAT_TYPE=10
    BOOL_TYPE=11
    STRING_TYPE=12
    PLUS=13
    MINUS=14
    STAR=15
    DIVISON=16
    MODULO=17
    EQUALS=18
    UNEQUAL=19
    LESS=20
    GREATER=21
    LESSEQUAL=22
    GREATEREQUAL=23
    AND=24
    OR=25
    NOT=26
    INTEGER=27
    FLOAT=28
    BOOL=29
    STRING=30
    NL=31
    LB=32
    RB=33
    CLB=34
    CRB=35
    COMMA=36
    DOT=37
    SEMICOLON=38
    ASSIGN=39
    WHITESPACE=40
    COMMENT=41
    IDENTIFIER=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self._IDENTIFIER = None # Token

        def PACKAGE(self):
            return self.getToken(GoParser.PACKAGE, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def main_function(self):
            return self.getTypedRuleContext(GoParser.Main_functionContext,0)


        def EOF(self):
            return self.getToken(GoParser.EOF, 0)

        def IMPORT(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IMPORT)
            else:
                return self.getToken(GoParser.IMPORT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.STRING)
            else:
                return self.getToken(GoParser.STRING, i)

        def functions(self):
            return self.getTypedRuleContext(GoParser.FunctionsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(GoParser.PACKAGE)
            self.state = 37
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 38
            if not (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == "main" :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$IDENTIFIER.text == \"main\" ")
            self.state = 39
            self.match(GoParser.NL)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 40
                self.match(GoParser.IMPORT)
                self.state = 41
                self.match(GoParser.STRING)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(GoParser.NL)
            self.state = 48
            self.main_function()
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 49
                self.match(GoParser.NL)
                self.state = 50
                self.functions()


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 53
                self.match(GoParser.NL)


            self.state = 56
            self.match(GoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._IDENTIFIER = None # Token

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(GoParser.LB, 0)

        def RB(self):
            return self.getToken(GoParser.RB, 0)

        def CLB(self):
            return self.getToken(GoParser.CLB, 0)

        def body(self):
            return self.getTypedRuleContext(GoParser.BodyContext,0)


        def CRB(self):
            return self.getToken(GoParser.CRB, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.TypeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def getRuleIndex(self):
            return GoParser.RULE_main_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_function" ):
                listener.enterMain_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_function" ):
                listener.exitMain_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function" ):
                return visitor.visitMain_function(self)
            else:
                return visitor.visitChildren(self)




    def main_function(self):

        localctx = GoParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(GoParser.FUNC)
            self.state = 59
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 60
            if not (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == "main" :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$IDENTIFIER.text == \"main\" ")
            self.state = 61
            self.match(GoParser.LB)
            self.state = 62
            self.match(GoParser.RB)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0:
                self.state = 63
                self.type_()


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 66
                self.match(GoParser.NL)


            self.state = 69
            self.match(GoParser.CLB)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 70
                self.match(GoParser.NL)


            self.state = 73
            self.body()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 74
                self.match(GoParser.NL)


            self.state = 77
            self.match(GoParser.CRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._function = None # FunctionContext
            self.funcs = None # FunctionsContext

        def function(self):
            return self.getTypedRuleContext(GoParser.FunctionContext,0)


        def NL(self):
            return self.getToken(GoParser.NL, 0)

        def functions(self):
            return self.getTypedRuleContext(GoParser.FunctionsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = GoParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            localctx._function = self.function()
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 80
                self.match(GoParser.NL)
                self.state = 81
                localctx.funcs = self.functions()


            localctx.node = self.func_Nodes(localctx._function.node, localctx.funcs.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._IDENTIFIER = None # Token
            self._type = None # TypeContext
            self._body = None # BodyContext

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(GoParser.LB, 0)

        def RB(self):
            return self.getToken(GoParser.RB, 0)

        def CLB(self):
            return self.getToken(GoParser.CLB, 0)

        def body(self):
            return self.getTypedRuleContext(GoParser.BodyContext,0)


        def CRB(self):
            return self.getToken(GoParser.CRB, 0)

        def func_args(self):
            return self.getTypedRuleContext(GoParser.Func_argsContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.TypeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def getRuleIndex(self):
            return GoParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = GoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(GoParser.FUNC)
            self.state = 87
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 88
            self.match(GoParser.LB)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 89
                self.func_args()


            self.state = 92
            self.match(GoParser.RB)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0:
                self.state = 93
                localctx._type = self.type_()


            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 96
                self.match(GoParser.NL)


            self.state = 99
            self.match(GoParser.CLB)
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(GoParser.NL)


            self.state = 103
            localctx._body = self.body()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 104
                self.match(GoParser.NL)


            self.state = 107
            self.match(GoParser.CRB)
            localctx.node = self.funcNodes((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),(None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)),localctx._body.node)
            		
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None

        def declarations(self):
            return self.getTypedRuleContext(GoParser.DeclarationsContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def statements(self):
            return self.getTypedRuleContext(GoParser.StatementsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = GoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 110
                self.declarations()
                self.state = 111
                self.match(GoParser.NL)


            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 115
                    self.match(GoParser.NL) 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 121
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.TypeContext)
            else:
                return self.getTypedRuleContext(GoParser.TypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_func_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_args" ):
                listener.enterFunc_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_args" ):
                listener.exitFunc_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_args" ):
                return visitor.visitFunc_args(self)
            else:
                return visitor.visitChildren(self)




    def func_args(self):

        localctx = GoParser.Func_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(GoParser.IDENTIFIER)
            self.state = 125
            self.type_()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 126
                self.match(GoParser.COMMA)
                self.state = 127
                self.match(GoParser.IDENTIFIER)
                self.state = 128
                self.type_()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(GoParser.INT_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(GoParser.BOOL_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(GoParser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(GoParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return GoParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = GoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(GoParser.DeclarationContext,0)


        def NL(self):
            return self.getToken(GoParser.NL, 0)

        def declarations(self):
            return self.getTypedRuleContext(GoParser.DeclarationsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = GoParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declarations)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.declaration()
                self.state = 137
                self.match(GoParser.NL)
                self.state = 138
                self.declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = GoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(GoParser.VAR)
            self.state = 144
            self.match(GoParser.IDENTIFIER)
            self.state = 145
            self.type_()
            self.state = 146
            self.match(GoParser.ASSIGN)
            self.state = 147
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(GoParser.StatementContext,0)


        def NL(self):
            return self.getToken(GoParser.NL, 0)

        def statements(self):
            return self.getTypedRuleContext(GoParser.StatementsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = GoParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statements)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.statement()
                self.state = 150
                self.match(GoParser.NL)
                self.state = 151
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(GoParser.AssignmentContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(GoParser.Block_stmtContext,0)


        def if_control(self):
            return self.getTypedRuleContext(GoParser.If_controlContext,0)


        def for_control(self):
            return self.getTypedRuleContext(GoParser.For_controlContext,0)


        def func_call(self):
            return self.getTypedRuleContext(GoParser.Func_callContext,0)


        def RETURN(self):
            return self.getToken(GoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.if_control()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.for_control()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 160
                self.func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 161
                self.match(GoParser.RETURN)
                self.state = 162
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLB(self):
            return self.getToken(GoParser.CLB, 0)

        def CRB(self):
            return self.getToken(GoParser.CRB, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def statements(self):
            return self.getTypedRuleContext(GoParser.StatementsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_block_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_stmt" ):
                listener.enterBlock_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_stmt" ):
                listener.exitBlock_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = GoParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(GoParser.CLB)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 166
                self.match(GoParser.NL)


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 169
                self.statements()


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 172
                self.match(GoParser.NL)


            self.state = 175
            self.match(GoParser.CRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = GoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(GoParser.IDENTIFIER)
            self.state = 178
            self.match(GoParser.ASSIGN)
            self.state = 179
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_controlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GoParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def CLB(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.CLB)
            else:
                return self.getToken(GoParser.CLB, i)

        def CRB(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.CRB)
            else:
                return self.getToken(GoParser.CRB, i)

        def ELSE(self):
            return self.getToken(GoParser.ELSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.StatementsContext)
            else:
                return self.getTypedRuleContext(GoParser.StatementsContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_if_control

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_control" ):
                listener.enterIf_control(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_control" ):
                listener.exitIf_control(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_control" ):
                return visitor.visitIf_control(self)
            else:
                return visitor.visitChildren(self)




    def if_control(self):

        localctx = GoParser.If_controlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_control)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(GoParser.IF)
                self.state = 182
                self.expr(0)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 183
                    self.match(GoParser.NL)


                self.state = 186
                self.match(GoParser.CLB)
                self.state = 188
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 187
                    self.match(GoParser.NL)


                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 190
                    self.statements()


                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 193
                    self.match(GoParser.NL)


                self.state = 196
                self.match(GoParser.CRB)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 197
                    self.match(GoParser.NL)


                self.state = 200
                self.match(GoParser.ELSE)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 201
                    self.match(GoParser.NL)


                self.state = 204
                self.match(GoParser.CLB)
                self.state = 206
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 205
                    self.match(GoParser.NL)


                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 208
                    self.statements()


                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 211
                    self.match(GoParser.NL)


                self.state = 214
                self.match(GoParser.CRB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(GoParser.IF)
                self.state = 217
                self.expr(0)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 218
                    self.match(GoParser.NL)


                self.state = 221
                self.match(GoParser.CLB)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 222
                    self.match(GoParser.NL)


                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 225
                    self.statements()


                self.state = 228
                self.match(GoParser.CRB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_controlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def CLB(self):
            return self.getToken(GoParser.CLB, 0)

        def CRB(self):
            return self.getToken(GoParser.CRB, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def statements(self):
            return self.getTypedRuleContext(GoParser.StatementsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_for_control

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_control" ):
                listener.enterFor_control(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_control" ):
                listener.exitFor_control(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_control" ):
                return visitor.visitFor_control(self)
            else:
                return visitor.visitChildren(self)




    def for_control(self):

        localctx = GoParser.For_controlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_control)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(GoParser.FOR)
            self.state = 233
            self.expr(0)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 234
                self.match(GoParser.NL)


            self.state = 237
            self.match(GoParser.CLB)
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 238
                self.match(GoParser.NL)


            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 241
                self.statements()


            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 244
                self.match(GoParser.NL)


            self.state = 247
            self.match(GoParser.CRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def LB(self):
            return self.getToken(GoParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExprContext)
            else:
                return self.getTypedRuleContext(GoParser.ExprContext,i)


        def RB(self):
            return self.getToken(GoParser.RB, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.DOT)
            else:
                return self.getToken(GoParser.DOT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = GoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(GoParser.IDENTIFIER)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 250
                self.match(GoParser.DOT)
                self.state = 251
                self.match(GoParser.IDENTIFIER)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self.match(GoParser.LB)
            self.state = 258
            self.expr(0)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 259
                self.match(GoParser.COMMA)
                self.state = 260
                self.expr(0)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self.match(GoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.left = None # ExprContext
            self._literals = None # LiteralsContext
            self._expr = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(GoParser.Func_callContext,0)


        def literals(self):
            return self.getTypedRuleContext(GoParser.LiteralsContext,0)


        def LB(self):
            return self.getToken(GoParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExprContext)
            else:
                return self.getTypedRuleContext(GoParser.ExprContext,i)


        def RB(self):
            return self.getToken(GoParser.RB, 0)

        def NOT(self):
            return self.getToken(GoParser.NOT, 0)

        def PLUS(self):
            return self.getToken(GoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoParser.MINUS, 0)

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def DIVISON(self):
            return self.getToken(GoParser.DIVISON, 0)

        def MODULO(self):
            return self.getToken(GoParser.MODULO, 0)

        def UNEQUAL(self):
            return self.getToken(GoParser.UNEQUAL, 0)

        def EQUALS(self):
            return self.getToken(GoParser.EQUALS, 0)

        def LESS(self):
            return self.getToken(GoParser.LESS, 0)

        def GREATER(self):
            return self.getToken(GoParser.GREATER, 0)

        def LESSEQUAL(self):
            return self.getToken(GoParser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(GoParser.GREATEREQUAL, 0)

        def OR(self):
            return self.getToken(GoParser.OR, 0)

        def AND(self):
            return self.getToken(GoParser.AND, 0)

        def getRuleIndex(self):
            return GoParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 269
                self.match(GoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 270
                self.func_call()
                pass

            elif la_ == 3:
                self.state = 271
                localctx._literals = self.literals()
                localctx.node = localctx._literals.node
                pass

            elif la_ == 4:
                self.state = 274
                self.match(GoParser.LB)
                self.state = 275
                localctx._expr = self.expr(0)
                self.state = 276
                self.match(GoParser.RB)
                localctx.node = localctx._expr.node
                pass

            elif la_ == 5:
                self.state = 279
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 67133440) != 0):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 280
                localctx._expr = self.expr(5)
                localctx.node = self.unaryNode((None if localctx.op is None else localctx.op.text), localctx._expr.node)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 305
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 285
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 286
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 287
                        localctx.right = localctx._expr = self.expr(5)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 2:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 290
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 291
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 292
                        localctx.right = localctx._expr = self.expr(4)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 3:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 295
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 296
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 297
                        localctx.right = localctx._expr = self.expr(3)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 4:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 301
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 302
                        localctx.right = localctx._expr = self.expr(2)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

             
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._INTEGER = None # Token
            self._STRING = None # Token
            self._FLOAT = None # Token
            self._BOOL = None # Token

        def INTEGER(self):
            return self.getToken(GoParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(GoParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(GoParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(GoParser.BOOL, 0)

        def getRuleIndex(self):
            return GoParser.RULE_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiterals" ):
                listener.enterLiterals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiterals" ):
                listener.exitLiterals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = GoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literals)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                localctx._INTEGER = self.match(GoParser.INTEGER)
                localctx.node =self.atomNode(int((None if localctx._INTEGER is None else localctx._INTEGER.text)))
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                localctx._STRING = self.match(GoParser.STRING)
                localctx.node = self.atomNode((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                localctx._FLOAT = self.match(GoParser.FLOAT)
                localctx.node = self.atomNode(float((None if localctx._FLOAT is None else localctx._FLOAT.text)))
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 316
                localctx._BOOL = self.match(GoParser.BOOL)
                localctx.node = self.atomNode((None if localctx._BOOL is None else localctx._BOOL.text) != 'false')
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.program_sempred
        self._predicates[1] = self.main_function_sempred
        self._predicates[16] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def program_sempred(self, localctx:ProgramContext, predIndex:int):
            if predIndex == 0:
                return (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == "main" 
         

    def main_function_sempred(self, localctx:Main_functionContext, predIndex:int):
            if predIndex == 1:
                return (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == "main" 
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




