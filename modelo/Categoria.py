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

    def esOperadorComparacion(cadena):
        caracterActual = cadena[0]
        if caracterActual == '>':
            pass
        elif caracterActual == '<':
            pass
        elif caracterActual == '=':
            pass
        elif caracterActual == '!':
            pass
        else:
            return False

        if len(cadena) == 2 and cadena[1] == '=':
            return True
        else:
            return False

    def esOperadorIncDec(cadena):
        caracterActual = cadena[0]
        opc = None
        if caracterActual == '+':
            opc = 0
        elif caracterActual == '-':
            opc = 1
        else:
            return False
        if len(cadena) == 2:
            if cadena[1] == '+' and opc == 0:
                return True
            elif cadena[1] == '-' and opc == 1:
                return True
        return False

    def esParentesis(cadena):
        if len(cadena) == 1:
            if cadena[0] == '(' or cadena[0] == ')':
                return True
        return False

    def esLlave(cadena):
        if len(cadena) == 1:
            if cadena[0] == '{' or cadena[0] == '}':
                return True
        return False

    def esTerminal(cadena):
        if len(cadena) == 1:
            if cadena[0] == '.':
                return True
        return False

    def esTerminal(cadena):
        if len(cadena) == 1:
            if cadena[0] == ',':
                return True
        return False

    def esComentario(cadena):
        opcion = 0
        if cadena[0] == '/':
            if cadena[-1] == '/' and cadena[-2] == '*' and len(cadena) >= 4:
                opcion = 1
        else:
            return False
        if cadena[1] == '/' and opcion == 0:
            return True
        elif cadena[1] == '*' and opcion == 1:
            return True
        return False

    def esHexadecimal(cadena):
        hexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        entero = 0
        for i in range(len(cadena)):
            caracterActual = cadena[i]
            esHexadecimal = False
            for valor in hexadecimal:
                if entero >= 2:
                    return False
                if caracterActual == valor:
                    esHexadecimal = True
                    break
            entero += 1
            if not esHexadecimal:
                return False
        return True

    def esCadena(cadena):
        if cadena[0] == '1' and cadena[-1] == '1':
            for i in range(1, len(cadena)-1):
                if cadena[i] == '1':
                    return False
            return True
        return False

    def esOperadorAsignacion(cadena):
        caracterActual = cadena[0]
        if caracterActual == '+':
            pass
        elif caracterActual == '-':
            pass
        elif caracterActual == '*':
            pass
        elif caracterActual == '/':
            pass
        elif caracterActual == '%':
            pass
        elif caracterActual == '=':
            if len(cadena) == 1:
                return True
        else:
            return False

        if len(cadena) == 2:
            if cadena[1] == '=':
                return True

        return False

    def esNumeroReal(cadena):
        punto = 0
        numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(cadena)):
            caracterActual = cadena[i]
            esDigito = False
            if punto > 1:
                return False
            if cadena[i] == '.' and i != 0:
                punto += 1
                esDigito = True
            for digito in numeros:
                if caracterActual == digito:
                    esDigito = True
                    break
            if not esDigito:
                return False
        return True

    def esIdentificador(cadena):
        contador = 0
        caracteres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q",
                      "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                      "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z", "-", "0", "1", "2", "3", "4", "5",
                      "6", "7", "8", "9"]
        for i in range(len(cadena)):
            esDigito = False
            if contador >= 10:
                return False
            for j in range(len(caracteres)):
                if cadena[i] == caracteres[j]:
                    esDigito = True
                    break
            if not esDigito:
                return False
            contador += 1
        return True



