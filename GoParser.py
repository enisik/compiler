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
        4,1,42,423,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,1,0,1,
        0,1,0,1,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,0,1,0,1,0,1,
        0,3,0,57,8,0,1,0,3,0,60,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,71,8,1,1,1,1,1,3,1,75,8,1,1,1,1,1,3,1,79,8,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,3,2,89,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,99,
        8,3,1,3,1,3,1,3,1,3,3,3,105,8,3,1,3,3,3,108,8,3,1,3,1,3,3,3,112,
        8,3,1,3,1,3,3,3,116,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,125,8,4,
        1,4,5,4,128,8,4,10,4,12,4,131,9,4,1,4,1,4,1,4,3,4,136,8,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,148,8,5,10,5,12,5,151,9,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,161,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,3,7,171,8,7,1,8,1,8,1,8,1,8,1,8,3,8,178,8,8,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,192,8,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,3,10,213,8,10,1,10,3,10,216,8,10,1,11,1,11,3,11,
        220,8,11,1,11,3,11,223,8,11,1,11,3,11,226,8,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,239,8,13,1,13,1,13,3,
        13,243,8,13,1,13,1,13,1,13,3,13,248,8,13,1,13,3,13,251,8,13,1,13,
        1,13,3,13,255,8,13,1,13,1,13,3,13,259,8,13,1,13,1,13,3,13,263,8,
        13,1,13,1,13,1,13,3,13,268,8,13,1,13,3,13,271,8,13,1,13,1,13,3,13,
        275,8,13,1,13,1,13,1,13,1,13,1,13,3,13,282,8,13,1,13,1,13,3,13,286,
        8,13,1,13,1,13,1,13,3,13,291,8,13,1,13,3,13,294,8,13,1,13,1,13,3,
        13,298,8,13,1,13,1,13,3,13,302,8,13,1,14,1,14,1,14,3,14,307,8,14,
        1,14,1,14,3,14,311,8,14,1,14,1,14,1,14,3,14,316,8,14,1,14,3,14,319,
        8,14,1,14,1,14,3,14,323,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,
        5,15,332,8,15,10,15,12,15,335,9,15,1,15,1,15,3,15,339,8,15,1,15,
        1,15,1,15,3,15,344,8,15,1,15,1,15,3,15,348,8,15,1,15,1,15,1,15,3,
        15,353,8,15,5,15,355,8,15,10,15,12,15,358,9,15,3,15,360,8,15,1,15,
        3,15,363,8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,386,
        8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,408,8,16,10,16,12,16,
        411,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,421,8,17,1,
        17,0,1,32,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,
        5,2,0,13,14,26,26,1,0,15,17,1,0,13,14,1,0,18,23,1,0,24,25,476,0,
        37,1,0,0,0,2,64,1,0,0,0,4,83,1,0,0,0,6,92,1,0,0,0,8,124,1,0,0,0,
        10,139,1,0,0,0,12,160,1,0,0,0,14,170,1,0,0,0,16,172,1,0,0,0,18,191,
        1,0,0,0,20,215,1,0,0,0,22,217,1,0,0,0,24,230,1,0,0,0,26,301,1,0,
        0,0,28,303,1,0,0,0,30,326,1,0,0,0,32,385,1,0,0,0,34,420,1,0,0,0,
        36,38,5,31,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,
        4,0,0,40,41,5,42,0,0,41,42,4,0,0,1,42,47,5,31,0,0,43,44,5,5,0,0,
        44,46,5,30,0,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,
        0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,31,0,0,51,56,3,2,1,0,52,
        53,5,31,0,0,53,54,3,4,2,0,54,55,6,0,-1,0,55,57,1,0,0,0,56,52,1,0,
        0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,5,31,0,0,59,58,1,0,0,0,59,
        60,1,0,0,0,60,61,1,0,0,0,61,62,5,0,0,1,62,63,6,0,-1,0,63,1,1,0,0,
        0,64,65,5,3,0,0,65,66,5,42,0,0,66,67,4,1,1,1,67,68,5,32,0,0,68,70,
        5,33,0,0,69,71,5,31,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,
        0,72,74,5,34,0,0,73,75,5,31,0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,
        1,0,0,0,76,78,3,8,4,0,77,79,5,31,0,0,78,77,1,0,0,0,78,79,1,0,0,0,
        79,80,1,0,0,0,80,81,5,35,0,0,81,82,6,1,-1,0,82,3,1,0,0,0,83,88,3,
        6,3,0,84,85,5,31,0,0,85,86,3,4,2,0,86,87,6,2,-1,0,87,89,1,0,0,0,
        88,84,1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,91,6,2,-1,0,91,5,1,
        0,0,0,92,93,5,3,0,0,93,94,5,42,0,0,94,98,5,32,0,0,95,96,3,10,5,0,
        96,97,6,3,-1,0,97,99,1,0,0,0,98,95,1,0,0,0,98,99,1,0,0,0,99,100,
        1,0,0,0,100,104,5,33,0,0,101,102,3,12,6,0,102,103,6,3,-1,0,103,105,
        1,0,0,0,104,101,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,108,
        5,31,0,0,107,106,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,111,
        5,34,0,0,110,112,5,31,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,
        1,0,0,0,113,115,3,8,4,0,114,116,5,31,0,0,115,114,1,0,0,0,115,116,
        1,0,0,0,116,117,1,0,0,0,117,118,5,35,0,0,118,119,6,3,-1,0,119,7,
        1,0,0,0,120,121,3,14,7,0,121,122,5,31,0,0,122,123,6,4,-1,0,123,125,
        1,0,0,0,124,120,1,0,0,0,124,125,1,0,0,0,125,129,1,0,0,0,126,128,
        5,31,0,0,127,126,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,
        1,0,0,0,130,135,1,0,0,0,131,129,1,0,0,0,132,133,3,18,9,0,133,134,
        6,4,-1,0,134,136,1,0,0,0,135,132,1,0,0,0,135,136,1,0,0,0,136,137,
        1,0,0,0,137,138,6,4,-1,0,138,9,1,0,0,0,139,140,5,42,0,0,140,141,
        3,12,6,0,141,149,6,5,-1,0,142,143,5,36,0,0,143,144,5,42,0,0,144,
        145,3,12,6,0,145,146,6,5,-1,0,146,148,1,0,0,0,147,142,1,0,0,0,148,
        151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,11,1,0,0,0,151,149,
        1,0,0,0,152,153,5,9,0,0,153,161,6,6,-1,0,154,155,5,11,0,0,155,161,
        6,6,-1,0,156,157,5,10,0,0,157,161,6,6,-1,0,158,159,5,12,0,0,159,
        161,6,6,-1,0,160,152,1,0,0,0,160,154,1,0,0,0,160,156,1,0,0,0,160,
        158,1,0,0,0,161,13,1,0,0,0,162,163,3,16,8,0,163,164,5,31,0,0,164,
        165,3,14,7,0,165,166,6,7,-1,0,166,171,1,0,0,0,167,168,3,16,8,0,168,
        169,6,7,-1,0,169,171,1,0,0,0,170,162,1,0,0,0,170,167,1,0,0,0,171,
        15,1,0,0,0,172,173,5,1,0,0,173,177,5,42,0,0,174,175,3,12,6,0,175,
        176,6,8,-1,0,176,178,1,0,0,0,177,174,1,0,0,0,177,178,1,0,0,0,178,
        179,1,0,0,0,179,180,5,39,0,0,180,181,3,32,16,0,181,182,6,8,-1,0,
        182,17,1,0,0,0,183,184,3,20,10,0,184,185,5,31,0,0,185,186,3,18,9,
        0,186,187,6,9,-1,0,187,192,1,0,0,0,188,189,3,20,10,0,189,190,6,9,
        -1,0,190,192,1,0,0,0,191,183,1,0,0,0,191,188,1,0,0,0,192,19,1,0,
        0,0,193,194,3,24,12,0,194,195,6,10,-1,0,195,216,1,0,0,0,196,197,
        3,22,11,0,197,198,6,10,-1,0,198,216,1,0,0,0,199,200,3,26,13,0,200,
        201,6,10,-1,0,201,216,1,0,0,0,202,203,3,28,14,0,203,204,6,10,-1,
        0,204,216,1,0,0,0,205,206,3,30,15,0,206,207,6,10,-1,0,207,216,1,
        0,0,0,208,212,5,2,0,0,209,210,3,32,16,0,210,211,6,10,-1,0,211,213,
        1,0,0,0,212,209,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,216,
        6,10,-1,0,215,193,1,0,0,0,215,196,1,0,0,0,215,199,1,0,0,0,215,202,
        1,0,0,0,215,205,1,0,0,0,215,208,1,0,0,0,216,21,1,0,0,0,217,219,5,
        34,0,0,218,220,5,31,0,0,219,218,1,0,0,0,219,220,1,0,0,0,220,222,
        1,0,0,0,221,223,3,18,9,0,222,221,1,0,0,0,222,223,1,0,0,0,223,225,
        1,0,0,0,224,226,5,31,0,0,225,224,1,0,0,0,225,226,1,0,0,0,226,227,
        1,0,0,0,227,228,5,35,0,0,228,229,6,11,-1,0,229,23,1,0,0,0,230,231,
        5,42,0,0,231,232,5,39,0,0,232,233,3,32,16,0,233,234,6,12,-1,0,234,
        25,1,0,0,0,235,236,5,6,0,0,236,238,3,32,16,0,237,239,5,31,0,0,238,
        237,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,242,5,34,0,0,241,
        243,5,31,0,0,242,241,1,0,0,0,242,243,1,0,0,0,243,247,1,0,0,0,244,
        245,3,18,9,0,245,246,6,13,-1,0,246,248,1,0,0,0,247,244,1,0,0,0,247,
        248,1,0,0,0,248,250,1,0,0,0,249,251,5,31,0,0,250,249,1,0,0,0,250,
        251,1,0,0,0,251,252,1,0,0,0,252,254,5,35,0,0,253,255,5,31,0,0,254,
        253,1,0,0,0,254,255,1,0,0,0,255,256,1,0,0,0,256,258,5,7,0,0,257,
        259,5,31,0,0,258,257,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,0,260,
        262,5,34,0,0,261,263,5,31,0,0,262,261,1,0,0,0,262,263,1,0,0,0,263,
        267,1,0,0,0,264,265,3,18,9,0,265,266,6,13,-1,0,266,268,1,0,0,0,267,
        264,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,271,5,31,0,0,270,
        269,1,0,0,0,270,271,1,0,0,0,271,272,1,0,0,0,272,274,5,35,0,0,273,
        275,5,31,0,0,274,273,1,0,0,0,274,275,1,0,0,0,275,276,1,0,0,0,276,
        277,6,13,-1,0,277,302,1,0,0,0,278,279,5,6,0,0,279,281,3,32,16,0,
        280,282,5,31,0,0,281,280,1,0,0,0,281,282,1,0,0,0,282,283,1,0,0,0,
        283,285,5,34,0,0,284,286,5,31,0,0,285,284,1,0,0,0,285,286,1,0,0,
        0,286,290,1,0,0,0,287,288,3,18,9,0,288,289,6,13,-1,0,289,291,1,0,
        0,0,290,287,1,0,0,0,290,291,1,0,0,0,291,293,1,0,0,0,292,294,5,31,
        0,0,293,292,1,0,0,0,293,294,1,0,0,0,294,295,1,0,0,0,295,297,5,35,
        0,0,296,298,5,31,0,0,297,296,1,0,0,0,297,298,1,0,0,0,298,299,1,0,
        0,0,299,300,6,13,-1,0,300,302,1,0,0,0,301,235,1,0,0,0,301,278,1,
        0,0,0,302,27,1,0,0,0,303,304,5,8,0,0,304,306,3,32,16,0,305,307,5,
        31,0,0,306,305,1,0,0,0,306,307,1,0,0,0,307,308,1,0,0,0,308,310,5,
        34,0,0,309,311,5,31,0,0,310,309,1,0,0,0,310,311,1,0,0,0,311,315,
        1,0,0,0,312,313,3,18,9,0,313,314,6,14,-1,0,314,316,1,0,0,0,315,312,
        1,0,0,0,315,316,1,0,0,0,316,318,1,0,0,0,317,319,5,31,0,0,318,317,
        1,0,0,0,318,319,1,0,0,0,319,320,1,0,0,0,320,322,5,35,0,0,321,323,
        5,31,0,0,322,321,1,0,0,0,322,323,1,0,0,0,323,324,1,0,0,0,324,325,
        6,14,-1,0,325,29,1,0,0,0,326,327,5,42,0,0,327,333,6,15,-1,0,328,
        329,5,37,0,0,329,330,5,42,0,0,330,332,6,15,-1,0,331,328,1,0,0,0,
        332,335,1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,336,1,0,0,0,
        335,333,1,0,0,0,336,359,5,32,0,0,337,339,5,31,0,0,338,337,1,0,0,
        0,338,339,1,0,0,0,339,340,1,0,0,0,340,341,3,32,16,0,341,343,6,15,
        -1,0,342,344,5,31,0,0,343,342,1,0,0,0,343,344,1,0,0,0,344,356,1,
        0,0,0,345,347,5,36,0,0,346,348,5,31,0,0,347,346,1,0,0,0,347,348,
        1,0,0,0,348,349,1,0,0,0,349,350,3,32,16,0,350,352,6,15,-1,0,351,
        353,5,31,0,0,352,351,1,0,0,0,352,353,1,0,0,0,353,355,1,0,0,0,354,
        345,1,0,0,0,355,358,1,0,0,0,356,354,1,0,0,0,356,357,1,0,0,0,357,
        360,1,0,0,0,358,356,1,0,0,0,359,338,1,0,0,0,359,360,1,0,0,0,360,
        362,1,0,0,0,361,363,5,31,0,0,362,361,1,0,0,0,362,363,1,0,0,0,363,
        364,1,0,0,0,364,365,5,33,0,0,365,366,6,15,-1,0,366,31,1,0,0,0,367,
        368,6,16,-1,0,368,369,5,42,0,0,369,386,6,16,-1,0,370,371,3,30,15,
        0,371,372,6,16,-1,0,372,386,1,0,0,0,373,374,3,34,17,0,374,375,6,
        16,-1,0,375,386,1,0,0,0,376,377,5,32,0,0,377,378,3,32,16,0,378,379,
        5,33,0,0,379,380,6,16,-1,0,380,386,1,0,0,0,381,382,7,0,0,0,382,383,
        3,32,16,5,383,384,6,16,-1,0,384,386,1,0,0,0,385,367,1,0,0,0,385,
        370,1,0,0,0,385,373,1,0,0,0,385,376,1,0,0,0,385,381,1,0,0,0,386,
        409,1,0,0,0,387,388,10,4,0,0,388,389,7,1,0,0,389,390,3,32,16,5,390,
        391,6,16,-1,0,391,408,1,0,0,0,392,393,10,3,0,0,393,394,7,2,0,0,394,
        395,3,32,16,4,395,396,6,16,-1,0,396,408,1,0,0,0,397,398,10,2,0,0,
        398,399,7,3,0,0,399,400,3,32,16,3,400,401,6,16,-1,0,401,408,1,0,
        0,0,402,403,10,1,0,0,403,404,7,4,0,0,404,405,3,32,16,2,405,406,6,
        16,-1,0,406,408,1,0,0,0,407,387,1,0,0,0,407,392,1,0,0,0,407,397,
        1,0,0,0,407,402,1,0,0,0,408,411,1,0,0,0,409,407,1,0,0,0,409,410,
        1,0,0,0,410,33,1,0,0,0,411,409,1,0,0,0,412,413,5,27,0,0,413,421,
        6,17,-1,0,414,415,5,30,0,0,415,421,6,17,-1,0,416,417,5,28,0,0,417,
        421,6,17,-1,0,418,419,5,29,0,0,419,421,6,17,-1,0,420,412,1,0,0,0,
        420,414,1,0,0,0,420,416,1,0,0,0,420,418,1,0,0,0,421,35,1,0,0,0,59,
        37,47,56,59,70,74,78,88,98,104,107,111,115,124,129,135,149,160,170,
        177,191,212,215,219,222,225,238,242,247,250,254,258,262,267,270,
        274,281,285,290,293,297,301,306,310,315,318,322,333,338,343,347,
        352,356,359,362,385,407,409,420
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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 36
                self.match(GoParser.NL)


            self.state = 39
            self.match(GoParser.PACKAGE)
            self.state = 40
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 41
            if not (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == "main" :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$IDENTIFIER.text == \"main\" ")
            self.state = 42
            self.match(GoParser.NL)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 43
                self.match(GoParser.IMPORT)
                self.state = 44
                self.match(GoParser.STRING)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(GoParser.NL)
            self.state = 51
            localctx._main_function = self.main_function()
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 52
                self.match(GoParser.NL)
                self.state = 53
                localctx._functions = self.functions()
                localctx.ast = localctx._functions.node


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 58
                self.match(GoParser.NL)


            self.state = 61
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
            self.state = 64
            self.match(GoParser.FUNC)
            self.state = 65
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 66
            if not (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == "main" :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$IDENTIFIER.text == \"main\" ")
            self.state = 67
            self.match(GoParser.LB)
            self.state = 68
            self.match(GoParser.RB)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 69
                self.match(GoParser.NL)


            self.state = 72
            self.match(GoParser.CLB)
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 73
                self.match(GoParser.NL)


            self.state = 76
            localctx._body = self.body()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 77
                self.match(GoParser.NL)


            self.state = 80
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
            self.state = 83
            localctx._function = self.function()
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 84
                self.match(GoParser.NL)
                self.state = 85
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
            self.state = 92
            self.match(GoParser.FUNC)
            self.state = 93
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 94
            self.match(GoParser.LB)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 95
                localctx._func_args = self.func_args()
                localctx.args = localctx._func_args.args


            self.state = 100
            self.match(GoParser.RB)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0:
                self.state = 101
                localctx._type = self.type_()
                localctx.ret = localctx._type.text


            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 106
                self.match(GoParser.NL)


            self.state = 109
            self.match(GoParser.CLB)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 110
                self.match(GoParser.NL)


            self.state = 113
            localctx._body = self.body()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 114
                self.match(GoParser.NL)


            self.state = 117
            self.match(GoParser.CRB)
            localctx.node = self.funcNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),localctx.ret,localctx._body.node)
            if (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) in global_scope:
                sys.exit(f"DUPLICATED FUNCTION DECLARATION\n{(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)}({localctx.args}) {localctx.ret}")
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
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 120
                localctx._declarations = self.declarations()
                self.state = 121
                self.match(GoParser.NL)
                localctx.decl = localctx._declarations.node


            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self.match(GoParser.NL) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 132
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
            self.state = 139
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 140
            localctx._type = self.type_()
            localctx.args = [((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),localctx._type.text)]
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 142
                self.match(GoParser.COMMA)
                self.state = 143
                localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
                self.state = 144
                localctx._type = self.type_()
                localctx.args.append(((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),localctx._type.text))
                self.state = 151
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(GoParser.INT_TYPE)
                localctx.text = 'INT'
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(GoParser.BOOL_TYPE)
                localctx.text = 'BOOL'
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(GoParser.FLOAT_TYPE)
                localctx.text = 'FLOAT'
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
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
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                localctx._declaration = self.declaration()
                self.state = 163
                self.match(GoParser.NL)
                self.state = 164
                localctx._declarations = self.declarations()
                localctx.node = self.blockNode(localctx._declaration.node, localctx._declarations.node, 'DECL')

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
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
            self.a = None
            self._IDENTIFIER = None # Token
            self._type = None # TypeContext
            self._expr = None # ExprContext

        def VAR(self):
            return self.getToken(GoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GoParser.ExprContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.TypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_declaration




    def declaration(self):

        localctx = GoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(GoParser.VAR)
            self.state = 173
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0:
                self.state = 174
                localctx._type = self.type_()
                localctx.a = localctx._type.text


            self.state = 179
            self.match(GoParser.ASSIGN)
            self.state = 180
            localctx._expr = self.expr(0)
            localctx.node = self.declNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx.a, localctx._expr.node)
            		
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
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                localctx._statement = self.statement()
                self.state = 184
                self.match(GoParser.NL)
                self.state = 185
                localctx._statements = self.statements()
                localctx.node = self.blockNode(localctx._statement.node, localctx._statements.node, 'STMT')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                localctx._assignment = self.assignment()
                localctx.node = localctx._assignment.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                localctx._block_stmt = self.block_stmt()
                localctx.node = localctx._block_stmt.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                localctx._if_control = self.if_control()
                localctx.node = localctx._if_control.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 202
                localctx._for_loop = self.for_loop()
                localctx.node = localctx._for_loop.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                localctx._func_call = self.func_call()
                localctx.node = localctx._func_call.node
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 208
                self.match(GoParser.RETURN)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4404421877760) != 0:
                    self.state = 209
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
            self.state = 217
            self.match(GoParser.CLB)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 218
                self.match(GoParser.NL)


            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 221
                localctx._statements = self.statements()


            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 224
                self.match(GoParser.NL)


            self.state = 227
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
            self.state = 230
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            self.state = 231
            self.match(GoParser.ASSIGN)
            self.state = 232
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
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(GoParser.IF)
                self.state = 236
                localctx._expr = self.expr(0)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 237
                    self.match(GoParser.NL)


                self.state = 240
                self.match(GoParser.CLB)
                self.state = 242
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 241
                    self.match(GoParser.NL)


                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 244
                    localctx._statements = self.statements()
                    localctx.stat1= localctx._statements.node


                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 249
                    self.match(GoParser.NL)


                self.state = 252
                self.match(GoParser.CRB)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 253
                    self.match(GoParser.NL)


                self.state = 256
                self.match(GoParser.ELSE)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 257
                    self.match(GoParser.NL)


                self.state = 260
                self.match(GoParser.CLB)
                self.state = 262
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 261
                    self.match(GoParser.NL)


                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 264
                    localctx._statements = self.statements()
                    localctx.stat2 = localctx._statements.node


                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 269
                    self.match(GoParser.NL)


                self.state = 272
                self.match(GoParser.CRB)
                self.state = 274
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 273
                    self.match(GoParser.NL)


                localctx.node= self.ifNode(localctx._expr.node, localctx.stat1, localctx.stat2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(GoParser.IF)
                self.state = 279
                localctx._expr = self.expr(0)
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 280
                    self.match(GoParser.NL)


                self.state = 283
                self.match(GoParser.CLB)
                self.state = 285
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 284
                    self.match(GoParser.NL)


                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                    self.state = 287
                    localctx._statements = self.statements()
                    localctx.stat1= localctx._statements.node


                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 292
                    self.match(GoParser.NL)


                self.state = 295
                self.match(GoParser.CRB)
                self.state = 297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 296
                    self.match(GoParser.NL)


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
            self.state = 303
            self.match(GoParser.FOR)
            self.state = 304
            localctx._expr = self.expr(0)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 305
                self.match(GoParser.NL)


            self.state = 308
            self.match(GoParser.CLB)
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 309
                self.match(GoParser.NL)


            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4415226380612) != 0:
                self.state = 312
                localctx._statements = self.statements()
                localctx.stat = localctx._statements.node


            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 317
                self.match(GoParser.NL)


            self.state = 320
            self.match(GoParser.CRB)
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 321
                self.match(GoParser.NL)


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


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NL)
            else:
                return self.getToken(GoParser.NL, i)

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
            self.state = 326
            localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
            localctx.id_ = (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 328
                self.match(GoParser.DOT)
                self.state = 329
                localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
                localctx.id_ += "." + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 336
            self.match(GoParser.LB)
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 337
                    self.match(GoParser.NL)


                self.state = 340
                localctx._expr = self.expr(0)
                localctx.args = [localctx._expr.node]
                self.state = 343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 342
                    self.match(GoParser.NL)


                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 345
                    self.match(GoParser.COMMA)
                    self.state = 347
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==31:
                        self.state = 346
                        self.match(GoParser.NL)


                    self.state = 349
                    localctx._expr = self.expr(0)
                    localctx.args.append(localctx._expr.node)
                    self.state = 352
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        self.state = 351
                        self.match(GoParser.NL)


                    self.state = 358
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 361
                self.match(GoParser.NL)


            self.state = 364
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
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 368
                localctx._IDENTIFIER = self.match(GoParser.IDENTIFIER)
                localctx.node= self.idNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text),None)
                pass

            elif la_ == 2:
                self.state = 370
                localctx._func_call = self.func_call()
                localctx.node = localctx._func_call.node
                pass

            elif la_ == 3:
                self.state = 373
                localctx._literals = self.literals()
                localctx.node = localctx._literals.node
                pass

            elif la_ == 4:
                self.state = 376
                self.match(GoParser.LB)
                self.state = 377
                localctx._expr = self.expr(0)
                self.state = 378
                self.match(GoParser.RB)
                localctx.node = localctx._expr.node
                pass

            elif la_ == 5:
                self.state = 381
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 67133440) != 0):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 382
                localctx._expr = self.expr(5)
                localctx.node = self.unaryNode((None if localctx.op is None else localctx.op.text), localctx._expr.node)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 407
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                    if la_ == 1:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 387
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 388
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 389
                        localctx.right = localctx._expr = self.expr(5)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 2:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 392
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 393
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 394
                        localctx.right = localctx._expr = self.expr(4)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 3:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 397
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 398
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 399
                        localctx.right = localctx._expr = self.expr(3)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

                    elif la_ == 4:
                        localctx = GoParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 402
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 403
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 404
                        localctx.right = localctx._expr = self.expr(2)
                        localctx.node = self.binaryNode(localctx.left.node, (None if localctx.op is None else localctx.op.text), localctx.right.node)
                                  		
                        pass

             
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                localctx._INTEGER = self.match(GoParser.INTEGER)
                localctx.node =self.atomNode((None if localctx._INTEGER is None else localctx._INTEGER.text),'INT')
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                localctx._STRING = self.match(GoParser.STRING)
                localctx.node = self.atomNode((None if localctx._STRING is None else localctx._STRING.text),'STRING')
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 416
                localctx._FLOAT = self.match(GoParser.FLOAT)
                localctx.node = self.atomNode((None if localctx._FLOAT is None else localctx._FLOAT.text), 'FLOAT')
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 418
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
         




