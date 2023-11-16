class Categoria:
    def esNumeroEntero(cadena):
        numerosNaturales = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        inicio = 0
        negativo = cadena[0]
        if negativo == "-":
            inicio = 1
        for i in range(inicio, len(cadena)):
            caracterActual = cadena[i]
            esDigitoNatural = False
            for digito in numerosNaturales:
                if caracterActual == digito:
                    esDigitoNatural = True
                    break
            if not esDigitoNatural:
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
                if caracterActual == 'I' and i == len(cadena) -1:
                    return True
                else:
                    return False
            elif opc == 1:
                if i == 1 and caracterActual == 'U':
                    continue
                elif i == 2 and caracterActual == 'N':
                    continue
                elif i == 3 and caracterActual == 'C' and i == len(cadena) -1:
                    return True
                else:
                    return False
            elif opc == 2:
                if i == 1 and caracterActual == 'N':
                    continue
                elif i == 2 and caracterActual == 'T' and i == len(cadena) -1:
                    return True
                else:
                    return False
            elif opc == 3:
                if i == 1 and caracterActual == 'A':
                    continue
                elif i == 2 and caracterActual == 'R' and i == len(cadena) -1:
                    return True
                else:
                    return False
            elif opc == 4:
                if i == 1 and caracterActual == 'A':
                    continue
                elif i == 2 and caracterActual == 'D' and i == len(cadena) -1:
                    return True
                else:
                    return False
            elif opc == 5:
                if i == 1 and caracterActual == 'O':
                    continue
                elif i == 2 and caracterActual == 'O':
                    continue
                elif i == 3 and caracterActual == 'L' and i == len(cadena) -1:
                    return True
                else:
                    return False

        return False

    def esOperadorLogico(cadena):
        opc = 0
        caracterActual = cadena[0]
        if caracterActual == 'A':
            opc = 0
        elif caracterActual == 'O':
            opc = 1
        elif caracterActual == 'N':
            opc = 2
        else:
            return False

        for i in range(1, len(cadena)):
            caracterActual = cadena[i]
            if opc == 0:
                if i == 1 and caracterActual == 'N':
                    continue
                if i == 2 and caracterActual == 'D' and i == len(cadena) -1:
                    return True
                else:
                    return False
            if opc == 1:
                if i == 1 and caracterActual == 'R' and i == len(cadena) -1:
                    return True
                else:
                    return False
            if opc == 2:
                if i == 1 and caracterActual == 'O':
                    continue
                if i == 2 and caracterActual == 'T' and i == len(cadena) -1:
                    return True
                else:
                    return False

        return False

    def esOperadorAritmetico(cadena):
        caracterActual = cadena[0]
        if len(cadena) == 1:
            if caracterActual == '+':
                return True
            elif caracterActual == '-':
                return True
            elif caracterActual == '*':
                return True
            elif caracterActual == '/':
                return True
            elif caracterActual == '%':
                return True
        return False




