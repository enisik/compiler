# Version
    Python 3.10.8
    ANTLR: 4.11.1

# Generierung
    antlr4 -Dlanguage=Python3 GoLexer.g4
    antlr4 -no-listener -Dlanguage=Python3 GoParser.g4

# Aufruf
    python main.py -compile datei
    python main.py -liveness datei (not implemented yet)