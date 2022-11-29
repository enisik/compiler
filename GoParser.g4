parser grammar GoParser;

options {
	tokenVocab = GoLexer;
}
prog: PACKAGE NEWLINE NEWLINE IMPORT main_method methods EOF;

main_method:
	FUNC MAIN '(' ')' INT_TYPE CLB func_body CRB methods;

methods:
	FUNC IDENTIFIER '(' func_args ')' return_type CLB func_body CRB;

func_body: IDENTIFIER |;
func_args: IDENTIFIER;
return_type: INT_TYPE | BOOL_TYPE | FLOAT_TYPE | STRING_TYPE |;