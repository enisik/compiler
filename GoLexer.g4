lexer grammar GoLexer;

// Math
PLUS: '+';
MINUS: '-';
STAR: '*';
DIVISON: '/';
MODULO: '%';

// Comparison
EQUALS: '==';
UNEQUAL: '!=';
LESS: '<';
GREATER: '>';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';

// Logic
AND: '&&';
OR: '||';
NOT: '!';

// Types
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
BOOL_TYPE: 'bool';
STRING_TYPE: 'string';

// Control
IF: 'if';
ELSE: 'else';
FOR: 'for';

// Literals
INTEGER: [0-9]+;
FLOAT: [0-9]+ .[0-9]+;
BOOL: 'true' | 'false';
STRING: '"' [.]* '"';

VAR: 'var';
RETURN: 'return';

FUNC: 'func';
PACKAGE: 'package main';
IMPORT: 'import "fmt"';
MAIN: 'main';

PRINT: 'fmt.Println';

NL: [\r\n]+;
LB: '(';
RB: ')';
CLB: '{';
CRB: '}';
COMMA: ',';
SEMICOLON: ';';
IS: '=';

WHITESPACE: [ ]+ -> skip;
IDENTIFIER: [a-zA-Z][_a-zA-Z0-9]*;
COMMENT: '//' [.]* '\n' | '/*' [.]* '*/';
