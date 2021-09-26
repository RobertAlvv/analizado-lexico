palabras_lista = ['and', 'as', 'assert', 'break', 'class', 'def', 'del', 'int', 'string', 'float'
           'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import',
           'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']


def palabra_reservada(a):
    if a in palabras_lista:
        print("(PALABRA RESERVADA %s)" % a)
    return a in palabras_lista
