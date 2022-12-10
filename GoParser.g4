parser grammar GoParser;

options {
	tokenVocab = GoLexer;
	superClass = GoASTParser;
}

program
	returns[ast]:
	PACKAGE IDENTIFIER {$IDENTIFIER.text == "main" }? NL (
		IMPORT STRING
	)* NL main_function (NL functions)? NL? EOF;

main_function:
	FUNC IDENTIFIER {$IDENTIFIER.text == "main" }? LB RB type? NL? CLB NL? body NL? CRB;

functions
	returns[node]:
	function (NL funcs = functions)? {$node = self.func_Nodes($function.node, $funcs.node)};

function
	returns[node]:
	FUNC IDENTIFIER LB func_args? RB type? NL? CLB NL? body NL? CRB {$node = self.funcNodes($IDENTIFIER.text,$type.text,$body.node)
		};

body
	returns[node]: (declarations NL)? NL* statements?;

func_args: IDENTIFIER type (COMMA IDENTIFIER type)*;

type: INT_TYPE | BOOL_TYPE | FLOAT_TYPE | STRING_TYPE;

declarations: declaration NL declarations | declaration;
declaration: VAR IDENTIFIER type ASSIGN expr;

statements: statement NL statements | statement;

statement:
	assignment
	| block_stmt
	| if_control
	| for_control
	| func_call
	| RETURN expr;

block_stmt: CLB NL? statements? NL? CRB;

assignment: IDENTIFIER ASSIGN expr;

if_control:
	IF expr NL? CLB NL? statements? NL? CRB NL? ELSE NL? CLB NL? statements? NL? CRB
	| IF expr NL? CLB NL? statements? CRB;

for_control: FOR expr NL? CLB NL? statements? NL? CRB;

func_call
	returns[node]:
	IDENTIFIER (DOT IDENTIFIER)* LB expr (COMMA expr)* RB;

/*expr:
 expr (OR | AND) expr | expr ( UNEQUAL | EQUALS | LESS | GREATER | LESSEQUAL | GREATEREQUAL ) expr |
 expr (MINUS | PLUS) expr | expr (STAR | DIVISON | MODULO) expr | (NOT | PLUS | MINUS) expr | LB
 expr RB | IDENTIFIER LB expr RB | lit = literals | func_call | IDENTIFIER;
 */

// First has highest operator precedency and latest the lowest precedency
expr
	returns[node]:
	IDENTIFIER
	| func_call
	| literals {$node = $literals.node}
	| LB expr RB {$node = $expr.node}
	| op = (NOT | PLUS | MINUS) expr {$node = self.unaryNode($op.text, $expr.node)}
	| left = expr (STAR | DIVISON | MODULO) right = expr {$node = self.binaryNode($left.node, $op.text, $right.node)
		}
	| left = expr op = (MINUS | PLUS) right = expr {$node = self.binaryNode($left.node, $op.text, $right.node)
		}
	| left = expr op = (
		UNEQUAL
		| EQUALS
		| LESS
		| GREATER
		| LESSEQUAL
		| GREATEREQUAL
	) right = expr {$node = self.binaryNode($left.node, $op.text, $right.node)
		}
	| left = expr op = (OR | AND) right = expr {$node = self.binaryNode($left.node, $op.text, $right.node)
		};

literals
	returns[node]:
	INTEGER {$node =self.atomNode(int($INTEGER.text))}
	| STRING {$node = self.atomNode($STRING.text)}
	| FLOAT {$node = self.atomNode(float($FLOAT.text))}
	| BOOL {$node = self.atomNode($BOOL.text != 'false')};

