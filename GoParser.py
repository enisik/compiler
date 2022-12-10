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
        4,1,43,297,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,5,0,
        42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,0,1,0,3,0,51,8,0,1,0,3,0,54,8,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,63,8,1,1,1,3,1,66,8,1,1,1,1,1,
        3,1,70,8,1,1,1,1,1,3,1,74,8,1,1,1,1,1,1,2,1,2,1,2,3,2,81,8,2,1,3,
        1,3,1,3,1,3,3,3,87,8,3,1,3,1,3,3,3,91,8,3,1,3,3,3,94,8,3,1,3,1,3,
        3,3,98,8,3,1,3,1,3,3,3,102,8,3,1,3,1,3,1,4,3,4,107,8,4,1,4,3,4,110,
        8,4,1,5,1,5,1,5,1,5,1,5,5,5,117,8,5,10,5,12,5,120,9,5,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,131,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,146,8,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,3,10,155,8,10,1,11,1,11,3,11,159,8,11,1,11,1,11,3,11,163,
        8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,174,8,13,
        1,13,1,13,3,13,178,8,13,1,13,3,13,181,8,13,1,13,3,13,184,8,13,1,
        13,1,13,3,13,188,8,13,1,13,1,13,3,13,192,8,13,1,13,1,13,3,13,196,
        8,13,1,13,3,13,199,8,13,1,13,3,13,202,8,13,1,13,1,13,1,13,1,13,1,
        13,3,13,209,8,13,1,13,1,13,3,13,213,8,13,1,13,3,13,216,8,13,1,13,
        1,13,3,13,220,8,13,1,14,1,14,1,14,3,14,225,8,14,1,14,1,14,3,14,229,
        8,14,1,14,3,14,232,8,14,1,14,3,14,235,8,14,1,14,1,14,1,15,1,15,1,
        15,5,15,242,8,15,10,15,12,15,245,9,15,1,15,1,15,1,15,1,15,5,15,251,
        8,15,10,15,12,15,254,9,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,268,8,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,5,16,282,8,16,10,16,12,16,285,9,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,295,8,17,1,17,0,1,32,
        18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,6,1,0,10,13,
        2,0,14,15,27,27,1,0,16,18,1,0,14,15,1,0,19,24,1,0,25,26,333,0,36,
        1,0,0,0,2,57,1,0,0,0,4,77,1,0,0,0,6,82,1,0,0,0,8,106,1,0,0,0,10,
        111,1,0,0,0,12,121,1,0,0,0,14,130,1,0,0,0,16,132,1,0,0,0,18,145,
        1,0,0,0,20,154,1,0,0,0,22,156,1,0,0,0,24,166,1,0,0,0,26,219,1,0,
        0,0,28,221,1,0,0,0,30,238,1,0,0,0,32,267,1,0,0,0,34,294,1,0,0,0,
        36,37,5,4,0,0,37,38,5,6,0,0,38,43,5,32,0,0,39,40,5,5,0,0,40,42,5,
        31,0,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,
        46,1,0,0,0,45,43,1,0,0,0,46,47,5,32,0,0,47,50,3,2,1,0,48,49,5,32,
        0,0,49,51,3,4,2,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,
        5,32,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,0,0,1,
        56,1,1,0,0,0,57,58,5,3,0,0,58,59,5,6,0,0,59,60,5,33,0,0,60,62,5,
        34,0,0,61,63,3,12,6,0,62,61,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,
        64,66,5,32,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,69,5,
        35,0,0,68,70,5,32,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,
        71,73,3,8,4,0,72,74,5,32,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,
        0,0,0,75,76,5,36,0,0,76,3,1,0,0,0,77,80,3,6,3,0,78,79,5,32,0,0,79,
        81,3,4,2,0,80,78,1,0,0,0,80,81,1,0,0,0,81,5,1,0,0,0,82,83,5,3,0,
        0,83,84,5,43,0,0,84,86,5,33,0,0,85,87,3,10,5,0,86,85,1,0,0,0,86,
        87,1,0,0,0,87,88,1,0,0,0,88,90,5,34,0,0,89,91,3,12,6,0,90,89,1,0,
        0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,94,5,32,0,0,93,92,1,0,0,0,93,
        94,1,0,0,0,94,95,1,0,0,0,95,97,5,35,0,0,96,98,5,32,0,0,97,96,1,0,
        0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,101,3,8,4,0,100,102,5,32,0,0,
        101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,36,0,0,
        104,7,1,0,0,0,105,107,3,14,7,0,106,105,1,0,0,0,106,107,1,0,0,0,107,
        109,1,0,0,0,108,110,3,18,9,0,109,108,1,0,0,0,109,110,1,0,0,0,110,
        9,1,0,0,0,111,112,5,43,0,0,112,118,3,12,6,0,113,114,5,37,0,0,114,
        115,5,43,0,0,115,117,3,12,6,0,116,113,1,0,0,0,117,120,1,0,0,0,118,
        116,1,0,0,0,118,119,1,0,0,0,119,11,1,0,0,0,120,118,1,0,0,0,121,122,
        7,0,0,0,122,13,1,0,0,0,123,124,3,16,8,0,124,125,5,32,0,0,125,126,
        3,14,7,0,126,131,1,0,0,0,127,128,3,16,8,0,128,129,5,32,0,0,129,131,
        1,0,0,0,130,123,1,0,0,0,130,127,1,0,0,0,131,15,1,0,0,0,132,133,5,
        1,0,0,133,134,5,43,0,0,134,135,3,12,6,0,135,136,5,40,0,0,136,137,
        3,32,16,0,137,17,1,0,0,0,138,139,3,20,10,0,139,140,5,32,0,0,140,
        141,3,18,9,0,141,146,1,0,0,0,142,143,3,20,10,0,143,144,5,32,0,0,
        144,146,1,0,0,0,145,138,1,0,0,0,145,142,1,0,0,0,146,19,1,0,0,0,147,
        155,3,24,12,0,148,155,3,22,11,0,149,155,3,26,13,0,150,155,3,28,14,
        0,151,155,3,30,15,0,152,153,5,2,0,0,153,155,3,32,16,0,154,147,1,
        0,0,0,154,148,1,0,0,0,154,149,1,0,0,0,154,150,1,0,0,0,154,151,1,
        0,0,0,154,152,1,0,0,0,155,21,1,0,0,0,156,158,5,35,0,0,157,159,5,
        32,0,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,0,160,162,3,
        18,9,0,161,163,5,32,0,0,162,161,1,0,0,0,162,163,1,0,0,0,163,164,
        1,0,0,0,164,165,5,36,0,0,165,23,1,0,0,0,166,167,5,43,0,0,167,168,
        5,40,0,0,168,169,3,32,16,0,169,25,1,0,0,0,170,171,5,7,0,0,171,173,
        3,32,16,0,172,174,5,32,0,0,173,172,1,0,0,0,173,174,1,0,0,0,174,175,
        1,0,0,0,175,177,5,35,0,0,176,178,5,32,0,0,177,176,1,0,0,0,177,178,
        1,0,0,0,178,180,1,0,0,0,179,181,3,18,9,0,180,179,1,0,0,0,180,181,
        1,0,0,0,181,183,1,0,0,0,182,184,5,32,0,0,183,182,1,0,0,0,183,184,
        1,0,0,0,184,185,1,0,0,0,185,187,5,36,0,0,186,188,5,32,0,0,187,186,
        1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,191,5,8,0,0,190,192,
        5,32,0,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,195,
        5,35,0,0,194,196,5,32,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,198,
        1,0,0,0,197,199,3,18,9,0,198,197,1,0,0,0,198,199,1,0,0,0,199,201,
        1,0,0,0,200,202,5,32,0,0,201,200,1,0,0,0,201,202,1,0,0,0,202,203,
        1,0,0,0,203,204,5,36,0,0,204,220,1,0,0,0,205,206,5,7,0,0,206,208,
        3,32,16,0,207,209,5,32,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,
        1,0,0,0,210,212,5,35,0,0,211,213,5,32,0,0,212,211,1,0,0,0,212,213,
        1,0,0,0,213,215,1,0,0,0,214,216,3,18,9,0,215,214,1,0,0,0,215,216,
        1,0,0,0,216,217,1,0,0,0,217,218,5,36,0,0,218,220,1,0,0,0,219,170,
        1,0,0,0,219,205,1,0,0,0,220,27,1,0,0,0,221,222,5,9,0,0,222,224,3,
        32,16,0,223,225,5,32,0,0,224,223,1,0,0,0,224,225,1,0,0,0,225,226,
        1,0,0,0,226,228,5,35,0,0,227,229,5,32,0,0,228,227,1,0,0,0,228,229,
        1,0,0,0,229,231,1,0,0,0,230,232,3,18,9,0,231,230,1,0,0,0,231,232,
        1,0,0,0,232,234,1,0,0,0,233,235,5,32,0,0,234,233,1,0,0,0,234,235,
        1,0,0,0,235,236,1,0,0,0,236,237,5,36,0,0,237,29,1,0,0,0,238,243,
        5,43,0,0,239,240,5,38,0,0,240,242,5,43,0,0,241,239,1,0,0,0,242,245,
        1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,246,1,0,0,0,245,243,
        1,0,0,0,246,247,5,33,0,0,247,252,3,32,16,0,248,249,5,37,0,0,249,
        251,3,32,16,0,250,248,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,
        253,1,0,0,0,253,255,1,0,0,0,254,252,1,0,0,0,255,256,5,34,0,0,256,
        31,1,0,0,0,257,258,6,16,-1,0,258,268,5,43,0,0,259,268,3,30,15,0,
        260,268,3,34,17,0,261,262,5,33,0,0,262,263,3,32,16,0,263,264,5,34,
        0,0,264,268,1,0,0,0,265,266,7,1,0,0,266,268,3,32,16,5,267,257,1,
        0,0,0,267,259,1,0,0,0,267,260,1,0,0,0,267,261,1,0,0,0,267,265,1,
        0,0,0,268,283,1,0,0,0,269,270,10,4,0,0,270,271,7,2,0,0,271,282,3,
        32,16,5,272,273,10,3,0,0,273,274,7,3,0,0,274,282,3,32,16,4,275,276,
        10,2,0,0,276,277,7,4,0,0,277,282,3,32,16,3,278,279,10,1,0,0,279,
        280,7,5,0,0,280,282,3,32,16,2,281,269,1,0,0,0,281,272,1,0,0,0,281,
        275,1,0,0,0,281,278,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,283,
        284,1,0,0,0,284,33,1,0,0,0,285,283,1,0,0,0,286,287,5,28,0,0,287,
        295,6,17,-1,0,288,289,5,31,0,0,289,295,6,17,-1,0,290,291,5,29,0,
        0,291,295,6,17,-1,0,292,293,5,30,0,0,293,295,6,17,-1,0,294,286,1,
        0,0,0,294,288,1,0,0,0,294,290,1,0,0,0,294,292,1,0,0,0,295,35,1,0,
        0,0,44,43,50,53,62,65,69,73,80,86,90,93,97,101,106,109,118,130,145,
        154,158,162,173,177,180,183,187,191,195,198,201,208,212,215,219,
        224,228,231,234,243,252,267,281,283,294
    ]

class GoParser ( GoASTParser ):

    grammarFileName = "GoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'return'", "'func'", "'package'", 
                     "'import'", "'main'", "'if'", "'else'", "'for'", "'int'", 
                     "'float64'", "'bool'", "'string'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'&&'", "'||'", "'!'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "','", "'.'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "VAR", "RETURN", "FUNC", "PACKAGE", "IMPORT", 
                      "MAIN", "IF", "ELSE", "FOR", "INT_TYPE", "FLOAT_TYPE", 
                      "BOOL_TYPE", "STRING_TYPE", "PLUS", "MINUS", "STAR", 
                      "DIVISON", "MODULO", "EQUALS", "UNEQUAL", "LESS", 
                      "GREATER", "LESSEQUAL", "GREATEREQUAL", "AND", "OR", 
                      "NOT", "INTEGER", "FLOAT", "BOOL", "STRING", "NL", 
                      "LB", "RB", "CLB", "CRB", "COMMA", "DOT", "SEMICOLON", 
                      "IS", "WHITESPACE", "COMMENT", "IDENTIFIER" ]

    RULE_program = 0
    RULE_main_method = 1
    RULE_methods = 2
    RULE_method = 3
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

    ruleNames =  [ "program", "main_method", "methods", "method", "body", 
                   "func_args", "type", "declarations", "declaration", "statements", 
                   "statement", "block_stmt", "assignment", "if_control", 
                   "for_control", "func_call", "expr", "literals" ]

    EOF = Token.EOF
    VAR=1
    RETURN=2
    FUNC=3
    PACKAGE=4
    IMPORT=5
    MAIN=6
    IF=7
    ELSE=8
    FOR=9
    INT_TYPE=10
    FLOAT_TYPE=11
    BOOL_TYPE=12
    STRING_TYPE=13
    PLUS=14
    MINUS=15
    STAR=16
    DIVISON=17
    MODULO=18
    EQUALS=19
    UNEQUAL=20
    LESS=21
    GREATER=22
    LESSEQUAL=23
    GREATEREQUAL=24
    AND=25
    OR=26
    NOT=27
    INTEGER=28
    FLOAT=29
    BOOL=30
    STRING=31
    NL=32
    LB=33
    RB=34
    CLB=35
    CRB=36
    COMMA=37
    DOT=38
    SEMICOLON=39
    IS=40
    WHITESPACE=41
    COMMENT=42
    IDENTIFIER=43

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

        def PACKAGE(self):
            return self.getToken(GoParser.PACKAGE, 0)

        def MAIN(self):
            return self.getToken(GoParser.MAIN, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def main_method(self):
            return self.getTypedRuleContext(GoParser.Main_methodContext,0)


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

        def methods(self):
            return self.getTypedRuleContext(GoParser.MethodsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = GoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(GoParser.PACKAGE)
            self.state = 37
            self.match(GoParser.MAIN)
            self.state = 38
            self.match(GoParser.NL)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 39
                self.match(GoParser.IMPORT)
                self.state = 40
                self.match(GoParser.STRING)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(GoParser.NL)
            self.state = 47
            self.main_method()
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(GoParser.NL)
                self.state = 49
                self.methods()


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 52
                self.match(GoParser.NL)


            self.state = 55
            self.match(GoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def MAIN(self):
            return self.getToken(GoParser.MAIN, 0)

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
            return GoParser.RULE_main_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_method" ):
                listener.enterMain_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_method" ):
                listener.exitMain_method(self)




    def main_method(self):

        localctx = GoParser.Main_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(GoParser.FUNC)
            self.state = 58
            self.match(GoParser.MAIN)
            self.state = 59
            self.match(GoParser.LB)
            self.state = 60
            self.match(GoParser.RB)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0:
                self.state = 61
                self.type_()


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 64
                self.match(GoParser.NL)


            self.state = 67
            self.match(GoParser.CLB)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 68
                self.match(GoParser.NL)


            self.state = 71
            self.body()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 72
                self.match(GoParser.NL)


            self.state = 75
            self.match(GoParser.CRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(GoParser.MethodContext,0)


        def NL(self):
            return self.getToken(GoParser.NL, 0)

        def methods(self):
            return self.getTypedRuleContext(GoParser.MethodsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_methods

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethods" ):
                listener.enterMethods(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethods" ):
                listener.exitMethods(self)




    def methods(self):

        localctx = GoParser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_methods)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.method()
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 78
                self.match(GoParser.NL)
                self.state = 79
                self.methods()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return GoParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)




    def method(self):

        localctx = GoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(GoParser.FUNC)
            self.state = 83
            self.match(GoParser.IDENTIFIER)
            self.state = 84
            self.match(GoParser.LB)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 85
                self.func_args()


            self.state = 88
            self.match(GoParser.RB)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0:
                self.state = 89
                self.type_()


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 92
                self.match(GoParser.NL)


            self.state = 95
            self.match(GoParser.CLB)
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 96
                self.match(GoParser.NL)


            self.state = 99
            self.body()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 100
                self.match(GoParser.NL)


            self.state = 103
            self.match(GoParser.CRB)
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

        def declarations(self):
            return self.getTypedRuleContext(GoParser.DeclarationsContext,0)


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




    def body(self):

        localctx = GoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 105
                self.declarations()


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 8830452761220) != 0:
                self.state = 108
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




    def func_args(self):

        localctx = GoParser.Func_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(GoParser.IDENTIFIER)
            self.state = 112
            self.type_()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 113
                self.match(GoParser.COMMA)
                self.state = 114
                self.match(GoParser.IDENTIFIER)
                self.state = 115
                self.type_()
                self.state = 120
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




    def type_(self):

        localctx = GoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0):
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




    def declarations(self):

        localctx = GoParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declarations)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.declaration()
                self.state = 124
                self.match(GoParser.NL)
                self.state = 125
                self.declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.declaration()
                self.state = 128
                self.match(GoParser.NL)
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


        def IS(self):
            return self.getToken(GoParser.IS, 0)

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




    def declaration(self):

        localctx = GoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(GoParser.VAR)
            self.state = 133
            self.match(GoParser.IDENTIFIER)
            self.state = 134
            self.type_()
            self.state = 135
            self.match(GoParser.IS)
            self.state = 136
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




    def statements(self):

        localctx = GoParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statements)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.statement()
                self.state = 139
                self.match(GoParser.NL)
                self.state = 140
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.statement()
                self.state = 143
                self.match(GoParser.NL)
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




    def statement(self):

        localctx = GoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.if_control()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.for_control()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 151
                self.func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 152
                self.match(GoParser.RETURN)
                self.state = 153
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

        def statements(self):
            return self.getTypedRuleContext(GoParser.StatementsContext,0)


        def CRB(self):
            return self.getToken(GoParser.CRB, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def getRuleIndex(self):
            return GoParser.RULE_block_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_stmt" ):
                listener.enterBlock_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_stmt" ):
                listener.exitBlock_stmt(self)




    def block_stmt(self):

        localctx = GoParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(GoParser.CLB)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 157
                self.match(GoParser.NL)


            self.state = 160
            self.statements()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 161
                self.match(GoParser.NL)


            self.state = 164
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

        def IS(self):
            return self.getToken(GoParser.IS, 0)

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




    def assignment(self):

        localctx = GoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(GoParser.IDENTIFIER)
            self.state = 167
            self.match(GoParser.IS)
            self.state = 168
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




    def if_control(self):

        localctx = GoParser.If_controlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_control)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(GoParser.IF)
                self.state = 171
                self.expr(0)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 172
                    self.match(GoParser.NL)


                self.state = 175
                self.match(GoParser.CLB)
                self.state = 177
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 176
                    self.match(GoParser.NL)


                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 8830452761220) != 0:
                    self.state = 179
                    self.statements()


                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 182
                    self.match(GoParser.NL)


                self.state = 185
                self.match(GoParser.CRB)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 186
                    self.match(GoParser.NL)


                self.state = 189
                self.match(GoParser.ELSE)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 190
                    self.match(GoParser.NL)


                self.state = 193
                self.match(GoParser.CLB)
                self.state = 195
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 194
                    self.match(GoParser.NL)


                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 8830452761220) != 0:
                    self.state = 197
                    self.statements()


                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 200
                    self.match(GoParser.NL)


                self.state = 203
                self.match(GoParser.CRB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(GoParser.IF)
                self.state = 206
                self.expr(0)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 207
                    self.match(GoParser.NL)


                self.state = 210
                self.match(GoParser.CLB)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 211
                    self.match(GoParser.NL)


                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 8830452761220) != 0:
                    self.state = 214
                    self.statements()


                self.state = 217
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




    def for_control(self):

        localctx = GoParser.For_controlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_control)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(GoParser.FOR)
            self.state = 222
            self.expr(0)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 223
                self.match(GoParser.NL)


            self.state = 226
            self.match(GoParser.CLB)
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 227
                self.match(GoParser.NL)


            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 8830452761220) != 0:
                self.state = 230
                self.statements()


            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 233
                self.match(GoParser.NL)


            self.state = 236
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




    def func_call(self):

        localctx = GoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(GoParser.IDENTIFIER)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 239
                self.match(GoParser.DOT)
                self.state = 240
                self.match(GoParser.IDENTIFIER)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self.match(GoParser.LB)
            self.state = 247
            self.expr(0)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 248
                self.match(GoParser.COMMA)
                self.state = 249
                self.expr(0)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(GoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 259
                self.func_call()
                pass

            elif la_ == 3:
                self.state = 260
                self.literals()
                pass

            elif la_ == 4:
                self.state = 261
                self.match(GoParser.LB)
                self.state = 262
                self.expr(0)
                self.state = 263
                self.match(GoParser.RB)
                pass

            elif la_ == 5:
                self.state = 265
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 134266880) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self.expr(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 281
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 269
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 270
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 271
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 272
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 273
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 274
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 275
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 276
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 277
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 278
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 279
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 280
                        self.expr(2)
                        pass

             
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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




    def literals(self):

        localctx = GoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literals)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                localctx._INTEGER = self.match(GoParser.INTEGER)
                print(self.node(int((None if localctx._INTEGER is None else localctx._INTEGER.text))))
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                localctx._STRING = self.match(GoParser.STRING)
                print(self.node((None if localctx._STRING is None else localctx._STRING.text)))
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                localctx._FLOAT = self.match(GoParser.FLOAT)
                print(self.node(float((None if localctx._FLOAT is None else localctx._FLOAT.text))))
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                localctx._BOOL = self.match(GoParser.BOOL)
                print(self.node((None if localctx._BOOL is None else localctx._BOOL.text) != 'false'))
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
        self._predicates[16] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




