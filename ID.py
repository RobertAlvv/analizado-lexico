minisculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t", "u", "v", "w", "x", "z"]

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
             "S", "T", "U", "V", "W", "X", "Y", "Z"]

digitos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_"]


# pass in a string, if all characters are found in 3 arrays above it will be true
def letra_numero(a):
    try:
        a.index('"')
        return False
    except:
        pass
    try:
        a.index("'")
        return False
    except:
        pass
    try:
        int(a[0])
        return False
    except:
        pass

    k = all(i in digitos or mayusculas or minisculas for i in a)
    if k:
        print('(ID "%s")' % a)
    return k
