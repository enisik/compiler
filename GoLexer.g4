lexer grammar GoLexer;

// KEYWORDS

VAR: 'var';
RETURN: 'return';
FUNC: 'func';
PACKAGE: 'package';
IMPORT: 'import';

// OTHER KEYWORDS

// Control
IF: 'if';
ELSE: 'else';
FOR: 'for';

// Types
INT_TYPE: 'int';
FLOAT_TYPE: 'float64';
BOOL_TYPE: 'bool';
STRING_TYPE: 'string';

// OPERATORS

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

// Literals
INTEGER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' .+? '"' | '""';

NL: [\r\n]+;
LB: '(';
RB: ')';
CLB: '{';
CRB: '}';
COMMA: ',';
DOT: '.';
SEMICOLON: ';';
ASSIGN: '=';

WHITESPACE: [ \t]+ -> skip;
COMMENT: ('//' .*? '\n' | '/*' .*? '*/') -> skip;
IDENTIFIER: [a-zA-Z][_a-zA-Z0-9]*;