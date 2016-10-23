#!/usr/bin/env python

# Fin de la entrada (input). End Of Input.
EOF = ""

# Valor por defecto para el token.
DEFAULT_TOKEN_VALUE = EOF

# Tipo de token.
TOKEN_NONE = 0
TOKEN_EQUAL = 1
TOKEN_PLUS = 2
TOKEN_MINUS = 3
TOKEN_TIMES = 4
TOKEN_OVER = 5
TOKEN_LPAREN = 6
TOKEN_RPAREN = 7
TOKEN_NUMBER = 8
TOKEN_X = 9
TOKEN_Y = 10
TOKEN_ERROR = 11
TOKEN_EOF = 12

# Estado en el que se encuentra la construccion del token.
STATE_START = 0
STATE_DONE = 1
STATE_INNUMBER = 2
