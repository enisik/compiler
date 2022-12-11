# Generated from GoParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


global_scope = dict()

if __name__ is not None and "." in __name__:
    from .GoASTParser import GoASTParser
else:
    from GoASTParser import GoASTParser

def serializedATN():
    return [
        4,1,42,393,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,1,0,
        5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,54,8,0,1,
        0,3,0,57,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,68,8,1,1,1,
        1,1,3,1,72,8,1,1,1,1,1,3,1,76,8,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,3,2,86,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,96,8,3,1,3,1,3,
        1,3,1,3,3,3,102,8,3,1,3,3,3,105,8,3,1,3,1,3,3,3,109,8,3,1,3,1,3,
        3,3,113,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,122,8,4,1,4,5,4,125,
        8,4,10,4,12,4,128,9,4,1,4,1,4,1,4,3,4,133,8,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,5,5,145,8,5,10,5,12,5,148,9,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,158,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,168,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,185,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,206,8,10,
        1,10,3,10,209,8,10,1,11,1,11,3,11,213,8,11,1,11,3,11,216,8,11,1,
        11,3,11,219,8,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,3,13,232,8,13,1,13,1,13,3,13,236,8,13,1,13,1,13,1,13,3,13,
        241,8,13,1,13,3,13,244,8,13,1,13,1,13,3,13,248,8,13,1,13,1,13,3,
        13,252,8,13,1,13,1,13,3,13,256,8,13,1,13,1,13,1,13,3,13,261,8,13,
        1,13,3,13,264,8,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,272,8,13,1,
        13,1,13,3,13,276,8,13,1,13,1,13,1,13,3,13,281,8,13,1,13,3,13,284,
        8,13,1,13,1,13,1,13,3,13,289,8,13,1,14,1,14,1,14,3,14,294,8,14,1,
        14,1,14,3,14,298,8,14,1,14,1,14,1,14,3,14,303,8,14,1,14,3,14,306,
        8,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,5,15,316,8,15,10,15,
        12,15,319,9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,328,8,15,
        10,15,12,15,331,9,15,3,15,333,8,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,356,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,
        378,8,16,10,16,12,16,381,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,391,8,17,1,17,0,1,32,18,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,0,5,2,0,13,14,26,26,1,0,15,17,1,0,13,14,1,0,18,
        23,1,0,24,25,436,0,36,1,0,0,0,2,61,1,0,0,0,4,80,1,0,0,0,6,89,1,0,
        0,0,8,121,1,0,0,0,10,136,1,0,0,0,12,157,1,0,0,0,14,167,1,0,0,0,16,
        169,1,0,0,0,18,184,1,0,0,0,20,208,1,0,0,0,22,210,1,0,0,0,24,223,
        1,0,0,0,26,288,1,0,0,0,28,290,1,0,0,0,30,310,1,0,0,0,32,355,1,0,
        0,0,34,390,1,0,0,0,36,37,5,4,0,0,37,38,5,42,0,0,38,39,4,0,0,1,39,
        44,5,31,0,0,40,41,5,5,0,0,41,43,5,30,0,0,42,40,1,0,0,0,43,46,1,0,
        0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,
        5,31,0,0,48,53,3,2,1,0,49,50,5,31,0,0,50,51,3,4,2,0,51,52,6,0,-1,
        0,52,54,1,0,0,0,53,49,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,57,
        5,31,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,0,0,1,
        59,60,6,0,-1,0,60,1,1,0,0,0,61,62,5,3,0,0,62,63,5,42,0,0,63,64,4,
        1,1,1,64,65,5,32,0,0,65,67,5,33,0,0,66,68,5,31,0,0,67,66,1,0,0,0,
        67,68,1,0,0,0,68,69,1,0,0,0,69,71,5,34,0,0,70,72,5,31,0,0,71,70,
        1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,75,3,8,4,0,74,76,5,31,0,0,
        75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,35,0,0,78,79,6,
        1,-1,0,79,3,1,0,0,0,80,85,3,6,3,0,81,82,5,31,0,0,82,83,3,4,2,0,83,
        84,6,2,-1,0,84,86,1,0,0,0,85,81,1,0,0,0,85,86,1,0,0,0,86,87,1,0,
        0,0,87,88,6,2,-1,0,88,5,1,0,0,0,89,90,5,3,0,0,90,91,5,42,0,0,91,
        95,5,32,0,0,92,93,3,10,5,0,93,94,6,3,-1,0,94,96,1,0,0,0,95,92,1,
        0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,101,5,33,0,0,98,99,3,12,6,0,
        99,100,6,3,-1,0,100,102,1,0,0,0,101,98,1,0,0,0,101,102,1,0,0,0,102,
        104,1,0,0,0,103,105,5,31,0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,
        106,1,0,0,0,106,108,5,34,0,0,107,109,5,31,0,0,108,107,1,0,0,0,108,
        109,1,0,0,0,109,110,1,0,0,0,110,112,3,8,4,0,111,113,5,31,0,0,112,
        111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,35,0,0,115,
        116,6,3,-1,0,116,7,1,0,0,0,117,118,3,14,7,0,118,119,5,31,0,0,119,
        120,6,4,-1,0,120,122,1,0,0,0,121,117,1,0,0,0,121,122,1,0,0,0,122,
        126,1,0,0,0,123,125,5,31,0,0,124,123,1,0,0,0,125,128,1,0,0,0,126,
        124,1,0,0,0,126,127,1,0,0,0,127,132,1,0,0,0,128,126,1,0,0,0,129,
        130,3,18,9,0,130,131,6,4,-1,0,131,133,1,0,0,0,132,129,1,0,0,0,132,
        133,1,0,0,0,133,134,1,0,0,0,134,135,6,4,-1,0,135,9,1,0,0,0,136,137,
        5,42,0,0,137,138,3,12,6,0,138,146,6,5,-1,0,139,140,5,36,0,0,140,
        141,5,42,0,0,141,142,3,12,6,0,142,143,6,5,-1,0,143,145,1,0,0,0,144,
        139,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,
        11,1,0,0,0,148,146,1,0,0,0,149,150,5,9,0,0,150,158,6,6,-1,0,151,
        152,5,11,0,0,152,158,6,6,-1,0,153,154,5,10,0,0,154,158,6,6,-1,0,
        155,156,5,12,0,0,156,158,6,6,-1,0,157,149,1,0,0,0,157,151,1,0,0,
        0,157,153,1,0,0,0,157,155,1,0,0,0,158,13,1,0,0,0,159,160,3,16,8,
        0,160,161,5,31,0,0,161,162,3,14,7,0,162,163,6,7,-1,0,163,168,1,0,
        0,0,164,165,3,16,8,0,165,166,6,7,-1,0,166,168,1,0,0,0,167,159,1,
        0,0,0,167,164,1,0,0,0,168,15,1,0,0,0,169,170,5,1,0,0,170,171,5,42,
        0,0,171,172,3,12,6,0,172,173,5,39,0,0,173,174,3,32,16,0,174,175,
        6,8,-1,0,175,17,1,0,0,0,176,177,3,20,10,0,177,178,5,31,0,0,178,179,
        3,18,9,0,179,180,6,9,-1,0,180,185,1,0,0,0,181,182,3,20,10,0,182,
        183,6,9,-1,0,183,185,1,0,0,0,184,176,1,0,0,0,184,181,1,0,0,0,185,
        19,1,0,0,0,186,187,3,24,12,0,187,188,6,10,-1,0,188,209,1,0,0,0,189,
        190,3,22,11,0,190,191,6,10,-1,0,191,209,1,0,0,0,192,193,3,26,13,
        0,193,194,6,10,-1,0,194,209,1,0,0,0,195,196,3,28,14,0,196,197,6,
        10,-1,0,197,209,1,0,0,0,198,199,3,30,15,0,199,200,6,10,-1,0,200,
        209,1,0,0,0,201,205,5,2,0,0,202,203,3,32,16,0,203,204,6,10,-1,0,
        204,206,1,0,0,0,205,202,1,0,0,0,205,206,1,0,0,0,206,207,1,0,0,0,
        207,209,6,10,-1,0,208,186,1,0,0,0,208,189,1,0,0,0,208,192,1,0,0,
        0,208,195,1,0,0,0,208,198,1,0,0,0,208,201,1,0,0,0,209,21,1,0,0,0,
        210,212,5,34,0,0,211,213,5,31,0,0,212,211,1,0,0,0,212,213,1,0,0,
        0,213,215,1,0,0,0,214,216,3,18,9,0,215,214,1,0,0,0,215,216,1,0,0,
        0,216,218,1,0,0,0,217,219,5,31,0,0,218,217,1,0,0,0,218,219,1,0,0,
        0,219,220,1,0,0,0,220,221,5,35,0,0,221,222,6,11,-1,0,222,23,1,0,
        0,0,223,224,5,42,0,0,224,225,5,39,0,0,225,226,3,32,16,0,226,227,
        6,12,-1,0,227,25,1,0,0,0,228,229,5,6,0,0,229,231,3,32,16,0,230,232,
        5,31,0,0,231,230,1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,0,233,235,
        5,34,0,0,234,236,5,31,0,0,235,234,1,0,0,0,235,236,1,0,0,0,236,240,
        1,0,0,0,237,238,3,18,9,0,238,239,6,13,-1,0,239,241,1,0,0,0,240,237,
        1,0,0,0,240,241,1,0,0,0,241,243,1,0,0,0,242,244,5,31,0,0,243,242,
        1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,0,245,247,5,35,0,0,246,248,
        5,31,0,0,247,246,1,0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,251,
        5,7,0,0,250,252,5,31,0,0,251,250,1,0,0,0,251,252,1,0,0,0,252,253,
        1,0,0,0,253,255,5,34,0,0,254,256,5,31,0,0,255,254,1,0,0,0,255,256,
        1,0,0,0,256,260,1,0,0,0,257,258,3,18,9,0,258,259,6,13,-1,0,259,261,
        1,0,0,0,260,257,1,0,0,0,260,261,1,0,0,0,261,263,1,0,0,0,262,264,
        5,31,0,0,263,262,1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,
        5,35,0,0,266,267,6,13,-1,0,267,289,1,0,0,0,268,269,5,6,0,0,269,271,
        3,32,16,0,270,272,5,31,0,0,271,270,1,0,0,0,271,272,1,0,0,0,272,273,
        1,0,0,0,273,275,5,34,0,0,274,276,5,31,0,0,275,274,1,0,0,0,275,276,
        1,0,0,0,276,280,1,0,0,0,277,278,3,18,9,0,278,279,6,13,-1,0,279,281,
        1,0,0,0,280,277,1,0,0,0,280,281,1,0,0,0,281,283,1,0,0,0,282,284,
        5,31,0,0,283,282,1,0,0,0,283,284,1,0,0,0,284,285,1,0,0,0,285,286,
        5,35,0,0,286,287,6,13,-1,0,287,289,1,0,0,0,288,228,1,0,0,0,288,268,
        1,0,0,0,289,27,1,0,0,0,290,291,5,8,0,0,291,293,3,32,16,0,292,294,
        5,31,0,0,293,292,1,0,0,0,293,294,1,0,0,0,294,295,1,0,0,0,295,297,
        5,34,0,0,296,298,5,31,0,0,297,296,1,0,0,0,297,298,1,0,0,0,298,302,
        1,0,0,0,299,300,3,18,9,0,300,301,6,14,-1,0,301,303,1,0,0,0,302,299,
        1,0,0,0,302,303,1,0,0,0,303,305,1,0,0,0,304,306,5,31,0,0,305,304,
        1,0,0,0,305,306,1,0,0,0,306,307,1,0,0,0,307,308,5,35,0,0,308,309,
        6,14,-1,0,309,29,1,0,0,0,310,311,5,42,0,0,311,317,6,15,-1,0,312,
        313,5,37,0,0,313,314,5,42,0,0,314,316,6,15,-1,0,315,312,1,0,0,0,
        316,319,1,0,0,0,317,315,1,0,0,0,317,318,1,0,0,0,318,320,1,0,0,0,
        319,317,1,0,0,0,320,332,5,32,0,0,321,322,3,32,16,0,322,329,6,15,
        -1,0,323,324,5,36,0,0,324,325,3,32,16,0,325,326,6,15,-1,0,326,328,
        1,0,0,0,327,323,1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,330,
        1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,0,332,321,1,0,0,0,332,333,
        1,0,0,0,333,334,1,0,0,0,334,335,5,33,0,0,335,336,6,15,-1,0,336,31,
        1,0,0,0,337,338,6,16,-1,0,338,339,5,42,0,0,339,356,6,16,-1,0,340,
        341,3,30,15,0,341,342,6,16,-1,0,342,356,1,0,0,0,343,344,3,34,17,
        0,344,345,6,16,-1,0,345,356,1,0,0,0,346,347,5,32,0,0,347,348,3,32,
        16,0,348,349,5,33,0,0,349,350,6,16,-1,0,350,356,1,0,0,0,351,352,
        7,0,0,0,352,353,3,32,16,5,353,354,6,16,-1,0,354,356,1,0,0,0,355,
        337,1,0,0,0,355,340,1,0,0,0,355,343,1,0,0,0,355,346,1,0,0,0,355,
        351,1,0,0,0,356,379,1,0,0,0,357,358,10,4,0,0,358,359,7,1,0,0,359,
        360,3,32,16,5,360,361,6,16,-1,0,361,378,1,0,0,0,362,363,10,3,0,0,
        363,364,7,2,0,0,364,365,3,32,16,4,365,366,6,16,-1,0,366,378,1,0,
        0,0,367,368,10,2,0,0,368,369,7,3,0,0,369,370,3,32,16,3,370,371,6,
        16,-1,0,371,378,1,0,0,0,372,373,10,1,0,0,373,374,7,4,0,0,374,375,
        3,32,16,2,375,376,6,16,-1,0,376,378,1,0,0,0,377,357,1,0,0,0,377,
        362,1,0,0,0,377,367,1,0,0,0,377,372,1,0,0,0,378,381,1,0,0,0,379,
        377,1,0,0,0,379,380,1,0,0,0,380,33,1,0,0,0,381,379,1,0,0,0,382,383,
        5,27,0,0,383,391,6,17,-1,0,384,385,5,30,0,0,385,391,6,17,-1,0,386,
        387,5,28,0,0,387,391,6,17,-1,0,388,389,5,29,0,0,389,391,6,17,-1,
        0,390,382,1,0,0,0,390,384,1,0,0,0,390,386,1,0,0,0,390,388,1,0,0,
        0,391,35,1,0,0,0,49,44,53,56,67,71,75,85,95,101,104,108,112,121,
        126,132,146,157,167,184,205,208,212,215,218,231,235,240,243,247,
        251,255,260,263,271,275,280,283,288,293,297,302,305,317,329,332,
        355,377,379,390
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
    RULE_for_loop = 14
    RULE_func_call = 15
    RULE_expr = 16
    RULE_literals = 17

    ruleNames =  [ "program", "main_function", "functions", "function", 
                   "body", "func_args", "type", "declarations", "declaration", 
                   "statements", "statement", "block_stmt", "assignment", 
                   "if_control", "for_loop", "func_call", "expr", "literals" ]

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
            self.global_scope = None
            self._IDENTIFIER = None # Token
            self._main_function = None # Main_functionContext
            self._functions = None # FunctionsContext

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
            localctx._main_function = self.main_function()
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 49
                self.match(GoParser.NL)
                self.state = 50
                localctx._functions = self.functions()
                localctx.ast = localctx._functions.node


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 55
                self.match(GoParser.NL)


            self.state = 58
            self.match(GoParser.EOF)
            localctx.ast = self.ast(localctx._main_function.node, localctx.ast)
            localctx.global_scope = global_scope
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
            self.node = None
            self._IDENTIFIER = None # Token
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

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

        def getRuleIndex(self):
            return GoParser.RULE_main_function




    def main_function(self):

        localctx = GoParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(GoParser.FUNC)
            self.state = 62
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 63
            if not (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == "main" :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$IDENTIFIER.text == \"main\" ")
            self.state = 64
            self.match(GoParser.LB)
            self.state = 65
            self.match(GoParser.RB)
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
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 70
                self.match(GoParser.NL)


            self.state = 73
            localctx._body = self.body()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 74
                self.match(GoParser.NL)


            self.state = 77
            self.match(GoParser.CRB)
            localctx.node = self.funcNode('main',None, localctx._body.node)
            global_scope['main'] = (None,None)
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
            self._functions = None # FunctionsContext

        def function(self):
            return self.getTypedRuleContext(GoParser.FunctionContext,0)


        def NL(self):
            return self.getToken(GoParser.NL, 0)

        def functions(self):
            return self.getTypedRuleContext(GoParser.FunctionsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functions




    def functions(self):

        localctx = GoParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            localctx._function = self.function()
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 81
                self.match(GoParser.NL)
                self.state = 82
                localctx._functions = self.functions()
                localctx.node = localctx._functions.node


            localctx.node = self.blockNode(localctx._function.node, localctx.node)

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
            self.args = None
            self.ret = None
            self._IDENTIFIER = None # Token
            self._func_args = None # Func_argsContext
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




    def function(self):

        localctx = GoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(GoParser.FUNC)
            self.state = 90
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 91
            self.match(GoParser.LB)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 92
                localctx._func_args = self.func_args()
                localctx.args = localctx._func_args.args


            self.state = 97
            self.match(GoParser.RB)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0:
                self.state = 98
                localctx._type = self.type_()
                localctx.ret = localctx._type.text


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 103
                self.match(GoParser.NL)


            self.state = 106
            self.match(GoParser.CLB)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 107
                self.match(GoParser.NL)


            self.state = 110
            localctx._body = self.body()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 111
                self.match(GoParser.NL)


            self.state = 114
            self.match(GoParser.CRB)
            localctx.node = self.funcNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),localctx.ret,localctx._body.node)
            global_scope[(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)] = (localctx.args,localctx.ret)
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
            self.decl = None
            self.stat = None
            self._declarations = None # DeclarationsContext
            self._statements = None # StatementsContext

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




    def body(self):

        localctx = GoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 117
                localctx._declarations = self.declarations()
                self.state = 118
                self.match(GoParser.NL)
                localctx.decl = localctx._declarations.node


            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 123
                    self.match(GoParser.NL) 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 129
                localctx._statements = self.statements()
                localctx.stat = localctx._statements.node


            localctx.node = self.bodyNode(localctx.decl,localctx.stat)

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
            self.args = None
            self._IDENTIFIER = None # Token
            self._type = None # TypeContext

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




    def func_args(self):

        localctx = GoParser.Func_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 137
            localctx._type = self.type_()
            localctx.args = [((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),localctx._type.text)]
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 139
                self.match(GoParser.COMMA)
                self.state = 140
                localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
                self.state = 141
                localctx._type = self.type_()
                localctx.args.append(((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),localctx._type.text))
                self.state = 148
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
            self.text = None

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




    def type_(self):

        localctx = GoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(GoParser.INT_TYPE)
                localctx.text = 'INT'
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(GoParser.BOOL_TYPE)
                localctx.text = 'BOOL'
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(GoParser.FLOAT_TYPE)
                localctx.text = 'FLOAT'
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 155
                self.match(GoParser.STRING_TYPE)
                localctx.text = 'STRING'
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


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._declaration = None # DeclarationContext
            self._declarations = None # DeclarationsContext

        def declaration(self):
            return self.getTypedRuleContext(GoParser.DeclarationContext,0)


        def NL(self):
            return self.getToken(GoParser.NL, 0)

        def declarations(self):
            return self.getTypedRuleContext(GoParser.DeclarationsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_declarations




    def declarations(self):

        localctx = GoParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declarations)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                localctx._declaration = self.declaration()
                self.state = 160
                self.match(GoParser.NL)
                self.state = 161
                localctx._declarations = self.declarations()
                localctx.node = self.blockNode(localctx._declaration.node, localctx._declarations.node, 'DECL')

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                localctx._declaration = self.declaration()
                localctx.node = self.blockNode(localctx._declaration.node, None, 'DECL')
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
            self.node = None
            self._IDENTIFIER = None # Token
            self._type = None # TypeContext
            self._expr = None # ExprContext

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




    def declaration(self):

        localctx = GoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GoParser.VAR)
            self.state = 170
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 171
            localctx._type = self.type_()
            self.state = 172
            self.match(GoParser.ASSIGN)
            self.state = 173
            localctx._expr = self.expr(0)
            localctx.node = self.declNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._type.text, localctx._expr.node)
            		
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
            self.node = None
            self._statement = None # StatementContext
            self._statements = None # StatementsContext

        def statement(self):
            return self.getTypedRuleContext(GoParser.StatementContext,0)


        def NL(self):
            return self.getToken(GoParser.NL, 0)

        def statements(self):
            return self.getTypedRuleContext(GoParser.StatementsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_statements




    def statements(self):

        localctx = GoParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statements)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                localctx._statement = self.statement()
                self.state = 177
                self.match(GoParser.NL)
                self.state = 178
                localctx._statements = self.statements()
                localctx.node = self.blockNode(localctx._statement.node, localctx._statements.node, 'STMT')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                localctx._statement = self.statement()
                localctx.node = self.blockNode(localctx._statement.node, None, 'STMT')
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
            self.node = None
            self._assignment = None # AssignmentContext
            self._block_stmt = None # Block_stmtContext
            self._if_control = None # If_controlContext
            self._for_loop = None # For_loopContext
            self._func_call = None # Func_callContext
            self._expr = None # ExprContext

        def assignment(self):
            return self.getTypedRuleContext(GoParser.AssignmentContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(GoParser.Block_stmtContext,0)


        def if_control(self):
            return self.getTypedRuleContext(GoParser.If_controlContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(GoParser.For_loopContext,0)


        def func_call(self):
            return self.getTypedRuleContext(GoParser.Func_callContext,0)


        def RETURN(self):
            return self.getToken(GoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_statement




    def statement(self):

        localctx = GoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                localctx._assignment = self.assignment()
                localctx.node = localctx._assignment.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                localctx._block_stmt = self.block_stmt()
                localctx.node = localctx._block_stmt.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                localctx._if_control = self.if_control()
                localctx.node = localctx._if_control.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                localctx._for_loop = self.for_loop()
                localctx.node = localctx._for_loop.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                localctx._func_call = self.func_call()
                localctx.node = localctx._func_call.node
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 201
                self.match(GoParser.RETURN)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4404421877760) != 0:
                    self.state = 202
                    localctx._expr = self.expr(0)
                    localctx.node= localctx._expr.node


                localctx.node = self.returnNode(localctx.node)
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
            self.node = None
            self._statements = None # StatementsContext

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




    def block_stmt(self):

        localctx = GoParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(GoParser.CLB)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 211
                self.match(GoParser.NL)


            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 214
                localctx._statements = self.statements()


            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 217
                self.match(GoParser.NL)


            self.state = 220
            self.match(GoParser.CRB)
            localctx.node = localctx._statements.node
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
            self.node = None
            self._IDENTIFIER = None # Token
            self._expr = None # ExprContext

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_assignment




    def assignment(self):

        localctx = GoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 224
            self.match(GoParser.ASSIGN)
            self.state = 225
            localctx._expr = self.expr(0)
            localctx.node = self.assignNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expr.node)
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
            self.node = None
            self.stat1 = None
            self.stat2 = None
            self._expr = None # ExprContext
            self._statements = None # StatementsContext

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




    def if_control(self):

        localctx = GoParser.If_controlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_control)
        self._la = 0 # Token type
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(GoParser.IF)
                self.state = 229
                localctx._expr = self.expr(0)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 230
                    self.match(GoParser.NL)


                self.state = 233
                self.match(GoParser.CLB)
                self.state = 235
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 234
                    self.match(GoParser.NL)


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 237
                    localctx._statements = self.statements()
                    localctx.stat1= localctx._statements.node


                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 242
                    self.match(GoParser.NL)


                self.state = 245
                self.match(GoParser.CRB)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 246
                    self.match(GoParser.NL)


                self.state = 249
                self.match(GoParser.ELSE)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 250
                    self.match(GoParser.NL)


                self.state = 253
                self.match(GoParser.CLB)
                self.state = 255
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 254
                    self.match(GoParser.NL)


                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 257
                    localctx._statements = self.statements()
                    localctx.stat2 = localctx._statements.node


                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 262
                    self.match(GoParser.NL)


                self.state = 265
                self.match(GoParser.CRB)
                localctx.node= self.ifNode(localctx._expr.node, localctx.stat1, localctx.stat2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(GoParser.IF)
                self.state = 269
                localctx._expr = self.expr(0)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 270
                    self.match(GoParser.NL)


                self.state = 273
                self.match(GoParser.CLB)
                self.state = 275
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 274
                    self.match(GoParser.NL)


                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 277
                    localctx._statements = self.statements()
                    localctx.stat1= localctx._statements.node


                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 282
                    self.match(GoParser.NL)


                self.state = 285
                self.match(GoParser.CRB)
                localctx.node= self.ifNode(localctx._expr.node, localctx.stat1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.stat = None
            self._expr = None # ExprContext
            self._statements = None # StatementsContext

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
            return GoParser.RULE_for_loop




    def for_loop(self):

        localctx = GoParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(GoParser.FOR)
            self.state = 291
            localctx._expr = self.expr(0)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 292
                self.match(GoParser.NL)


            self.state = 295
            self.match(GoParser.CLB)
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 296
                self.match(GoParser.NL)


            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 299
                localctx._statements = self.statements()
                localctx.stat = localctx._statements.node


            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 304
                self.match(GoParser.NL)


            self.state = 307
            self.match(GoParser.CRB)
            localctx.node = self.forNode(localctx._expr.node, localctx.stat)
            		
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
            self.node = None
            self.id_ = None
            self.args = None
            self._IDENTIFIER = None # Token
            self._expr = None # ExprContext

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def LB(self):
            return self.getToken(GoParser.LB, 0)

        def RB(self):
            return self.getToken(GoParser.RB, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.DOT)
            else:
                return self.getToken(GoParser.DOT, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExprContext)
            else:
                return self.getTypedRuleContext(GoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_func_call




    def func_call(self):

        localctx = GoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            localctx.id_ = (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 312
                self.match(GoParser.DOT)
                self.state = 313
                localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
                localctx.id_ += "." + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 320
            self.match(GoParser.LB)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4404421877760) != 0:
                self.state = 321
                localctx._expr = self.expr(0)
                localctx.args = [localctx._expr.node]
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 323
                    self.match(GoParser.COMMA)
                    self.state = 324
                    localctx._expr = self.expr(0)
                    localctx.args.append(localctx._expr.node)
                    self.state = 331
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 334
            self.match(GoParser.RB)
            localctx.node=self.funcCallNode(localctx.id_,localctx.args)
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
            self._IDENTIFIER = None # Token
            self._func_call = None # Func_callContext
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
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 338
                localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
                localctx.node= self.idNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),None)
                pass

            elif la_ == 2:
                self.state = 340
                localctx._func_call = self.func_call()
                localctx.node = localctx._func_call.node
                pass

            elif la_ == 3:
                self.state = 343
                localctx._literals = self.literals()
                localctx.node = localctx._literals.node
                pass

            elif la_ == 4:
                self.state = 346
                self.match(GoParser.LB)
                self.state = 347
                localctx._expr = self.expr(0)
                self.state = 348
                self.match(GoParser.RB)
                localctx.node = localctx._expr.node
                pass

            elif la_ == 5:
                self.state = 351
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 67133440) != 0):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 352
                localctx._expr = self.expr(5)
                localctx.node = self.unaryNode((None if localctx.op is None else localctx.op.text), localctx._expr.node)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 377
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 357
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 358
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 359
                        localctx.right = localctx._expr = self.expr(5)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 2:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 362
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 363
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 364
                        localctx.right = localctx._expr = self.expr(4)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 3:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 367
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 368
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 369
                        localctx.right = localctx._expr = self.expr(3)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 4:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 372
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 373
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 374
                        localctx.right = localctx._expr = self.expr(2)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

             
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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




    def literals(self):

        localctx = GoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literals)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                localctx._INTEGER = self.match(GoParser.INTEGER)
                localctx.node =self.atomNode((None if localctx._INTEGER is None else localctx._INTEGER.text),'INT')
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                localctx._STRING = self.match(GoParser.STRING)
                localctx.node = self.atomNode((None if localctx._STRING is None else localctx._STRING.text),'STRING')
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                localctx._FLOAT = self.match(GoParser.FLOAT)
                localctx.node = self.atomNode((None if localctx._FLOAT is None else localctx._FLOAT.text), 'FLOAT')
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 388
                localctx._BOOL = self.match(GoParser.BOOL)
                localctx.node = self.atomNode((None if localctx._BOOL is None else localctx._BOOL.text), 'BOOL')
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
         




