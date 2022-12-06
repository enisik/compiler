parser grammar GoParser;

options {
	tokenVocab = GoLexer;
}
program: PACKAGE NL IMPORT NL main_method (NL methods)? NL? EOF;

main_method: FUNC MAIN LB RB type? NL? CLB NL? body NL? CRB;

methods:
	FUNC IDENTIFIER LB func_args? RB type? NL? CLB NL? body NL? CRB (
		NL methods
	)?;

body: declarations? statements? opt_return?;
func_args: IDENTIFIER type | IDENTIFIER type COMMA func_args;
type: INT_TYPE | BOOL_TYPE | FLOAT_TYPE | STRING_TYPE;

declarations: declaration NL | declaration NL declaration;
declaration: VAR IDENTIFIER type IS expr | IDENTIFIER IS expr;

statements:
	statement NL statements
	| CLB statements CRB NL
	| statement NL;

statement:
	VAR IS expr
	| IF expr CLB NL? body CRB
	| PRINT LB expr RB;

expr:
	expr OR expr
	| expr AND expr
	| expr UNEQUAL expr
	| expr EQUALS expr
	| expr LESS expr
	| expr GREATER expr
	| expr LESSEQUAL expr
	| expr GREATEREQUAL expr
	| expr MINUS expr
	| expr PLUS expr
	| expr STAR expr
	| expr DIVISON expr
	| expr MODULO expr
	| NOT expr
	| PLUS expr
	| MINUS expr
	| LB expr RB
	| IDENTIFIER LB expr RB
	| literals
	| IDENTIFIER;

opt_return: RETURN expr;

literals: INTEGER | STRING | FLOAT | BOOL;

if_control:
	IF expr CLB NL? body CRB NL? ELSE NL? CLB NL? body CRB
	| IF expr CLB NL? body CRB;

for_control: FOR expr CLB statements CRB;