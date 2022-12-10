parser grammar GoParser;

options {
	tokenVocab = GoLexer;
	superClass = GoASTParser;
}

program:
	PACKAGE MAIN NL (IMPORT STRING)* NL main_method (NL methods)? NL? EOF;

main_method: FUNC MAIN LB RB type? NL? CLB NL? body NL? CRB;

methods: method (NL methods)?;

method:
	FUNC IDENTIFIER LB func_args? RB type? NL? CLB NL? body NL? CRB;

body: declarations? statements?;

func_args: IDENTIFIER type (COMMA IDENTIFIER type)*;

type: INT_TYPE | BOOL_TYPE | FLOAT_TYPE | STRING_TYPE;

declarations: declaration NL declarations | declaration NL;
declaration: VAR IDENTIFIER type IS expr;

statements: statement NL statements | statement NL;

statement:
	assignment
	| block_stmt
	| if_control
	| for_control
	| func_call
	| RETURN expr;

block_stmt: CLB NL? statements NL? CRB;

assignment: IDENTIFIER IS expr;

if_control:
	IF expr NL? CLB NL? statements? NL? CRB NL? ELSE NL? CLB NL? statements? NL? CRB
	| IF expr NL? CLB NL? statements? CRB;

for_control: FOR expr NL? CLB NL? statements? NL? CRB;

func_call:
	IDENTIFIER (DOT IDENTIFIER)* LB expr (COMMA expr)* RB;

/*expr:
 expr (OR | AND) expr | expr ( UNEQUAL | EQUALS | LESS | GREATER | LESSEQUAL | GREATEREQUAL ) expr |
 expr (MINUS | PLUS) expr | expr (STAR | DIVISON | MODULO) expr | (NOT | PLUS | MINUS) expr | LB
 expr RB | IDENTIFIER LB expr RB | lit = literals | func_call | IDENTIFIER;
 */

// First has highest operator precedency and latest the lowest precedency
expr:
	IDENTIFIER
	| func_call
	| literals
	| LB expr RB
	| (NOT | PLUS | MINUS) expr
	| expr (STAR | DIVISON | MODULO) expr
	| expr (MINUS | PLUS) expr
	| expr (
		UNEQUAL
		| EQUALS
		| LESS
		| GREATER
		| LESSEQUAL
		| GREATEREQUAL
	) expr
	| expr (OR | AND) expr;

literals:
	INTEGER {print(self.node(int($INTEGER.text)))}
	| STRING {print(self.node($STRING.text))}
	| FLOAT {print(self.node(float($FLOAT.text)))}
	| BOOL {print(self.node($BOOL.text != 'false'))};

