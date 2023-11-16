class Categoria:
    def esNumeroNatural(cadena):
        numerosNaturales = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        for caracterActual in cadena:
            if caracterActual not in numerosNaturales:
                return False

        return True

    def esPalabraReservada(cadena):
        opc = 0
        caracterActual = cadena[0]
        if caracterActual == 'S':
            opc = 0
        elif caracterActual == 'F':
            opc = 1
        elif caracterActual == 'E':
            opc = 2
        elif caracterActual == 'V':
            opc = 3
        elif caracterActual == 'C':
            opc = 4
        elif caracterActual == 'B':
            opc = 5
        else:
            return False

        for i in range(1, len(cadena)):
            caracterActual = cadena[i]
            if opc == 0:
                if caracterActual == 'I':
                    return True
                else:
                    return False
            elif opc == 1:
                if i == 1 and caracterActual == 'U':
                    continue
                elif i == 2 and caracterActual == 'N':
                    continue
                elif i == 3 and caracterActual == 'C':
                    return True
                else:
                    return False
            elif opc == 2:
                if i == 1 and caracterActual == 'N':
                    continue
                elif i == 2 and caracterActual == 'T':
                    return True
                else:
                    return False
            elif opc == 3:
                if i == 1 and caracterActual == 'A':
                    continue
                elif i == 2 and caracterActual == 'R':
                    return True
                else:
                    return False
            elif opc == 4:
                if i == 1 and caracterActual == 'A':
                    continue
                elif i == 2 and caracterActual == 'D':
                    return True
                else:
                    return False
            elif opc == 5:
                if i == 1 and caracterActual == 'O':
                    continue
                elif i == 2 and caracterActual == 'O':
                    continue
                elif i == 3 and caracterActual == 'L':
                    return True
                else:
                    return False

        return False




