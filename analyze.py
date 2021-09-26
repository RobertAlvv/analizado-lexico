import re
from punct import operador
from keywords import palabra_reservada
from ID import letra_numero

mi_entrada = input()

try:
    archivo = open(mi_entrada, 'r')

except:
    print("El archivo de entrada %s no existe" % mi_entrada)
    quit(0)

lineas = archivo.readlines()

if len(lineas) <= 0:
    print("El archivo de entrada %s esta vacio" % mi_entrada)
    quit(0)

#tokenizo la linea que recibo por parametro, para saber cuando es una palabra o algun signo como !@{}[]()=+, etc
def tokenizador(linea):
    palabras = linea.split()
    nuevas_palabras = []
    for i in range(len(palabras)):
        #valida si la palabra tiene comillas al inicio y al final de esta
        if palabras[i][0] in ("'", '"') and palabras[i][-1] in ("'", '"'):
            nuevas_palabras.append(palabras[i])
        else:
        # crea una nueva lista donde los caracteres como (){}[]%& lo separa de la palabra misma
            t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", palabras[i])
            nuevas_palabras.extend(t)
    return nuevas_palabras

#en esta funcion se determina cuando la linea que se está leyendo es un string con comillas al inicio y final
#o es una sentencia de codigo.
def get_strings(palabras):
    nuevas_palabras = []
    adding = False
    tmpstring = ''
    skip = False
    for p in palabras:
        if ('"' in p or "'" in p) and (p.count('"') < 2 and p.count("'") < 2):
            # valido si la palabra es una comilla
            adding = not adding
        if not adding:
            #si entro aqui es porque aun no he encontrado la comilla de cierre
            nuevas_palabras.append(tmpstring + p)
            tmpstring = ''
            skip = True
        if adding:
            #si entro aqui entonces es porque ya encontre mi comilla de cierre
            tmpstring += p + ' '
        else:
            if skip:
                skip = False
            else:
                nuevas_palabras.append(p)
    return nuevas_palabras

#aqui se ejecuta cada linea y se determina en que renglon se ubicara cada palabra
skip = False
for linea in lineas:
    if '#' in linea:
        # Si la linea es un comentario, la omite.
        linea = linea[:linea.index('#')]
    tokens = tokenizador(linea)
    linea_depurada = get_strings(tokens)
    for c, item in enumerate(linea_depurada):
        if not skip:
            if operador(item):
                try:
                    if operador(item + linea_depurada[c + 1]):
                        print('(OPERADOR "%s")' % str(item + linea_depurada[c + 1]))
                        skip = True
                    else:
                        print('(OPERADOR "%s")' % item)
                except:
                    print('(OPERADOR "%s")' % item)
            elif palabra_reservada(item):
                pass
            elif letra_numero(item):
                pass
            else:
                print("(NO IDENTIFICADO %s)" % item)
        else:
            skip = False
print("(Fin de la lectura)")
