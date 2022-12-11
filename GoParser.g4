parser grammar GoParser;

options {
	tokenVocab = GoLexer;
	superClass = GoASTParser;
}

@header {
global_scope = dict()
}

program
	returns[ast, global_scope]:
	PACKAGE IDENTIFIER {$IDENTIFIER.text == "main" }? NL (
		IMPORT STRING
	)* NL main_function (NL functions {$ast = $functions.node})? NL? EOF {$ast = self.ast($main_function.node, $ast)
$global_scope = global_scope};

main_function
	returns[node]:
	FUNC IDENTIFIER {$IDENTIFIER.text == "main" }? LB RB NL? CLB NL? body NL? CRB {$node = self.funcNode('main',None, $body.node)
global_scope['main'] = (None,'VOID')};

functions
	returns[node]:
	function (NL functions {$node = $functions.node})? {$node = self.blockNode($function.node, $node)
};

function
	returns[node, args]:
	FUNC IDENTIFIER LB (func_args {$args = $func_args.args})? RB type? NL? CLB NL? body NL? CRB {$node = self.funcNode($IDENTIFIER.text,$type.text,$body.node)
global_scope[$IDENTIFIER.text] = ($args,$type.text)};

body
	returns[node, decl, stat]: (
		declarations NL {$decl = $declarations.node}
	)? NL* (statements {$stat = $statements.node})? {$node = self.bodyNode($decl,$stat)
};

func_args
	returns[args]:
	IDENTIFIER type {$args = [($IDENTIFIER.text,$type.text)]} (
		COMMA IDENTIFIER type {$args.append(($IDENTIFIER.text,$type.text))}
	)*;

type
	returns[text]:
	INT_TYPE {$text = 'INT'}
	| BOOL_TYPE {$text = 'BOOL'}
	| FLOAT_TYPE {$text = 'FLOAT'}
	| STRING_TYPE {$text = 'STRING'};

declarations
	returns[node]:
	declaration NL declarations {$node = self.blockNode($declaration.node, $declarations.node, 'DECL')
}
	| declaration {$node = $declaration.node};

declaration
	returns[node]:
	VAR IDENTIFIER type ASSIGN expr {$node = self.declNode($IDENTIFIER.text, $type.text, $expr.node)
		};

statements
	returns[node]:
	statement NL statements {$node = self.blockNode($statement.node, $statements.node, 'STMT')}
	| statement {$node = $statement.node};

statement
	returns[node]:
	assignment {$node = $assignment.node}
	| block_stmt {$node = $block_stmt.node}
	| if_control {$node = $if_control.node}
	| for_loop {$node = $for_loop.node}
	| func_call {$node = $func_call.node}
	| RETURN expr {$node = self.returnNode($expr.node)};

block_stmt
	returns[node]:
	CLB NL? statements? NL? CRB {$node = $statements.node};

assignment
	returns[node]:
	IDENTIFIER ASSIGN expr {$node = self.assignNode($IDENTIFIER.text, $expr.node)};

if_control
	returns[node, stat1, stat2]:
	IF expr NL? CLB NL? (statements {$stat1= $statements.node})? NL? CRB NL? ELSE NL? CLB NL? (
		statements {$stat2 = $statements.node}
	)? NL? CRB {$node= self.ifNode($expr.node, $stat1, $stat2)}
	| IF expr NL? CLB NL? (statements {$stat1= $statements.node})? NL? CRB {$node= self.ifNode($expr.node, $stat1)
};

for_loop
	returns[node, stat]:
	FOR expr NL? CLB NL? (statements {$stat = $statements.node})? NL? CRB {$node = self.forNode($expr.node, $stat)
		};

func_call
	returns[node, id, args]:
	IDENTIFIER {$id = $IDENTIFIER.text} (
		DOT IDENTIFIER {$id += $IDENTIFIER.text}
	)* LB (
		expr {$args = [$expr.node]} (
			COMMA expr {$args.append($expr.node)}
		)*
	)? RB {$node=self.funcCallNode($id,$args)};

// First has highest operator precedency and latest the lowest precedency
expr
	returns[node]:
	IDENTIFIER {$node= self.atomNode($IDENTIFIER.text,None)}
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
	INTEGER {$node =self.atomNode($INTEGER.text,'INT')}
	| STRING {$node = self.atomNode($STRING.text,'STRING')}
	| FLOAT {$node = self.atomNode($FLOAT.text, 'FLOAT')}
	| BOOL {$node = self.atomNode($BOOL.text, 'BOOL')};

