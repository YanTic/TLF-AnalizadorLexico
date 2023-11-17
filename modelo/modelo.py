import re


RE_NUEVA_LINEA = r"\n+"  # Constante para la expresión regular que elimina las líneas vacías


def normalizar_cadena(cadena):
    """
    Elimina las líneas vacías y los espacios en blanco al inicio y al final de una cadena.
    """
    cadena = re.sub(RE_NUEVA_LINEA, "\n", cadena)
    cadena = cadena.strip()
    return cadena


def reconocer_numeros(caracter, palabra_actual, categoria):
    if caracter.isdigit():
        if categoria == Categoria.NO_RECONOCIDO or categoria == Categoria.ENTERO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.ENTERO
        if categoria == Categoria.DECIMAL:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.DECIMAL
    elif caracter == ".":
        if categoria == Categoria.ENTERO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.DECIMAL
        if categoria == Categoria.DECIMAL:
            return False, palabra_actual, categoria

    return False, palabra_actual, categoria


def reconocer_aritmeticos(caracter, palabra_actual, categoria):
    operadores_aritmeticos = ["+", "-", "*", "/", "%"]
    if caracter in operadores_aritmeticos:
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.OPERADOR_ARITMETICO
    return False, palabra_actual, categoria


def reconocer_incremento_decremento(caracter, palabra_actual, categoria):
    operadores_incremento_decremento = ["+", "-"]
    if caracter in operadores_incremento_decremento:
        if categoria == Categoria.OPERADOR_ARITMETICO:
            if caracter == "+" and palabra_actual == "+":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_INCREMENTO
            if caracter == "-" and palabra_actual == "-":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_DECREMENTO
    return False, palabra_actual, categoria


def reconocer_operadores_asignacion(caracter, palabra_actual, categoria):
    operador_asignacion = ["="]
    if caracter in operador_asignacion:
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.OPERADOR_ASIGNACION
        if categoria == Categoria.OPERADOR_ARITMETICO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.OPERADOR_ASIGNACION
    return False, palabra_actual, categoria


def reconocer_operadores_logicos(caracter, palabra_actual, categoria):
    operadores_logicos = ["&", "|", "!"]  # &&, || y !
    if caracter in operadores_logicos:
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.OPERADOR_LOGICO
        if categoria == Categoria.OPERADOR_LOGICO:
            if palabra_actual == "&" and caracter == "&":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_LOGICO
            if palabra_actual == "|" and caracter == "|":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_LOGICO
    return False, palabra_actual, categoria


def reconocer_operadores_comparacion(caracter, palabra_actual, categoria):
    operadores_comparacion = ["<", ">", "=", "!"]  # <, >, ==, !=, <=, >=
    if caracter in operadores_comparacion:
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.OPERADOR_COMPARACION
        if categoria == Categoria.OPERADOR_ASIGNACION:
            if palabra_actual == "=" and caracter == "=":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_COMPARACION
        if categoria == Categoria.OPERADOR_LOGICO:
            if palabra_actual == "!" and caracter == "=":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_COMPARACION
        if categoria == Categoria.OPERADOR_COMPARACION:
            if palabra_actual == "<" and caracter == "=":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_COMPARACION
            if palabra_actual == ">" and caracter == "=":
                palabra_actual += caracter
                return True, palabra_actual, Categoria.OPERADOR_COMPARACION
    return False, palabra_actual, categoria


def reconocer_cadenas(caracter, palabra_actual, categoria):
    if caracter == '"':
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.CADENA_CARACTERES
        if categoria == Categoria.CADENA_CARACTERES:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.CADENA_CARACTERES
    else:
        if categoria == Categoria.CADENA_CARACTERES:
            if len(palabra_actual) > 1 and palabra_actual[0] == '"' and palabra_actual[-1] == '"':
                return False, palabra_actual, categoria
            palabra_actual += caracter
            return True, palabra_actual, Categoria.CADENA_CARACTERES

    return False, palabra_actual, categoria


def reconocer_llaves(caracter, palabra_actual, categoria):
    if caracter == "{":
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.LLAVES
    if caracter == "}":
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.LLAVES
    return False, palabra_actual, categoria


def reconocer_parentesis(caracter, palabra_actual, categoria):
    if caracter == "(":
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PARENTESIS
    if caracter == ")":
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PARENTESIS
    return False, palabra_actual, categoria


def reconocer_terminal(caracter, palabra_actual, categoria):
    if caracter == ";":
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.TERMINAL
    return False, palabra_actual, categoria


def reconocer_separador(caracter, palabra_actual, categoria):
    if caracter == ",":
        if categoria == Categoria.NO_RECONOCIDO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.SEPARADOR
    return False, palabra_actual, categoria


def reconocer_comentario_linea(caracter, palabra_actual, categoria):  # // comentario \n
    if caracter == "/":
        if categoria == Categoria.OPERADOR_ARITMETICO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.COMENTARIO_LINEA
        if categoria == Categoria.COMENTARIO_LINEA:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.COMENTARIO_LINEA
    else:
        if categoria == Categoria.COMENTARIO_LINEA:
            if palabra_actual[-1] == "\n":
                return False, palabra_actual, categoria
            palabra_actual += caracter
            return True, palabra_actual, Categoria.COMENTARIO_LINEA

    return False, palabra_actual, categoria


def reconocer_comentario_bloque(caracter, palabra_actual, categoria):
    if caracter == "*":
        if categoria == Categoria.OPERADOR_ARITMETICO:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.COMENTARIO_BLOQUE
        if categoria == Categoria.COMENTARIO_BLOQUE:
            palabra_actual += caracter
            return True, palabra_actual, Categoria.COMENTARIO_BLOQUE
    else:
        if categoria == Categoria.COMENTARIO_BLOQUE:
            if (len(palabra_actual) > 4 and palabra_actual[0:2] == "/*" and
                    palabra_actual[-2:len(palabra_actual)] == "*/"):
                return False, palabra_actual, categoria
            palabra_actual += caracter
            return True, palabra_actual, Categoria.COMENTARIO_BLOQUE
    return False, palabra_actual, categoria


def reconocer_identificador(caracter, palabra_actual, categoria):
    if caracter.isalpha() or caracter.isdigit():
        if categoria == Categoria.NO_RECONOCIDO and caracter.isalpha():
            palabra_actual += caracter
            return True, palabra_actual, Categoria.IDENTIFICADOR
        if categoria == Categoria.IDENTIFICADOR:
            if len(palabra_actual) < 10:
                palabra_actual += caracter
                return True, palabra_actual, Categoria.IDENTIFICADOR
            else:
                return False, palabra_actual, categoria
    return False, palabra_actual, categoria


def reconocer_hexadecimal(caracter, palabra_actual, categoria):
    h = {"#", "A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    if caracter in h:
        if categoria == Categoria.NO_RECONOCIDO and caracter == "#":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.HEXADECIMAL
        if categoria == Categoria.HEXADECIMAL and caracter != "#":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.HEXADECIMAL
    else:
        if categoria == Categoria.HEXADECIMAL:
            return False, palabra_actual, categoria  # TODO: crear token inválido
    return False, palabra_actual, categoria


def reconocer_palabras_reservadas(caracter, palabra_actual, categoria):
    # ^ (SI ∪ FUNC ∪ ENT ∪ VAR ∪ CAD ∪ BOOL)
    if caracter == "^" and categoria == Categoria.NO_RECONOCIDO:
        palabra_actual += caracter
        return True, palabra_actual, Categoria.PALABRA_RESERVADA
    if categoria == Categoria.PALABRA_RESERVADA:
        if palabra_actual == "^" and (caracter == "S" or caracter == "F" or caracter == "E" or caracter == "V" or
                                      caracter == "C" or caracter == "B"):
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^S" and caracter == "I":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^F" and caracter == "U":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^FU" and caracter == "N":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^FUN" and caracter == "C":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^E" and caracter == "N":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^V" and caracter == "A":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^VA" and caracter == "R":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^C" and caracter == "A":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^CA" and caracter == "D":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^B" and caracter == "O":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^BO" and caracter == "O":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
        if palabra_actual == "^BOO" and caracter == "L":
            palabra_actual += caracter
            return True, palabra_actual, Categoria.PALABRA_RESERVADA
    return False, palabra_actual, categoria


def crear_token(palabra, categoria, linea, columna):
    return Token(palabra, categoria, (linea, columna))


class AnalizadorLexico:
    """Clase que representa un analizador léxico para un lenguaje de programación.

    Atributos:
    codigo_fuente -- la cadena que contiene el código fuente a analizar
    lista_tokens -- la lista de objetos de tipo Token generados por el análisis
    """

    def __init__(self):
        self.codigo_fuente = ""
        self.lista_tokens = []

    def establecer_codigo(self, codigo):
        """Establece el código fuente a analizar y lo normaliza."""
        self.codigo_fuente = normalizar_cadena(codigo)

    def analizar(self):
        """Analiza el código fuente línea por línea y genera los tokens correspondientes."""
        linea = 1
        columna = 0
        palabra_actual = ""
        i = 0
        categoria = Categoria.NO_RECONOCIDO
        while i <= len(self.codigo_fuente):

            if i == len(self.codigo_fuente):
                token = crear_token(palabra_actual, categoria, linea, columna - len(palabra_actual))
                self.lista_tokens.append(token)
                palabra_actual = ""
                i += 1
                columna += 1
                continue

            caracter_actual = self.codigo_fuente[i]

            # Llamadas a los autómatas
            resultado, palabra_actual, categoria = reconocer_numeros(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_aritmeticos(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_incremento_decremento(caracter_actual, palabra_actual,
                                                                                   categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_operadores_asignacion(caracter_actual, palabra_actual,
                                                                                   categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_operadores_logicos(caracter_actual, palabra_actual,
                                                                                categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_operadores_comparacion(caracter_actual, palabra_actual,
                                                                                    categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_cadenas(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_llaves(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_parentesis(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_terminal(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_separador(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_comentario_linea(caracter_actual, palabra_actual,
                                                                              categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_comentario_bloque(caracter_actual, palabra_actual,
                                                                               categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_identificador(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_hexadecimal(caracter_actual, palabra_actual, categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            resultado, palabra_actual, categoria = reconocer_palabras_reservadas(caracter_actual, palabra_actual,
                                                                                 categoria)
            if resultado:
                i += 1
                columna += 1
                continue

            # Si ningún autómata acepta el carácter
            if not resultado and palabra_actual == "":
                if caracter_actual == "\n" or caracter_actual == " ":
                    if caracter_actual == "\n":
                        linea += 1
                        columna = 0
                    i += 1
                    columna += 1
                    continue
                token = crear_token(caracter_actual, Categoria.NO_RECONOCIDO, linea,
                                    (columna - len(palabra_actual)))
                self.lista_tokens.append(token)
                categoria = Categoria.NO_RECONOCIDO
                palabra_actual = ""
                i += 1
                columna += 1
            else:  # Ya no es aceptado en ningún autómata, pero ya generó una palabra
                token = crear_token(palabra_actual, categoria, linea, columna - len(palabra_actual))
                self.lista_tokens.append(token)
                categoria = Categoria.NO_RECONOCIDO
                palabra_actual = ""

    def tokens_a_string(self):
        """Convierte la lista de tokens en una cadena con el formato adecuado.

        Retorna:
        cadena -- la cadena que contiene la información de los tokens
        """
        return "\n".join(f"{token.palabra} | {token.categoria} | {token.position[0]}-{token.position[1]}" for token in
                         self.lista_tokens)


class Token:
    """Clase que representa un token o unidad léxica de un lenguaje de programación.

    Atributos:
    palabra -- la palabra que representa el token
    categoria -- la categoría que representa el token
    position -- la posición donde se encuentra el token
    """

    def __init__(self, palabra, categoria, posicion):
        self.palabra = palabra
        self.categoria = categoria
        self.position = posicion


class Categoria:
    """Clase que representa las posibles categorías de los tokens de un lenguaje de programación."""

    NO_RECONOCIDO = 1  # IMPLEMENTED
    ENTERO = 2  # IMPLEMENTED
    DECIMAL = 3  # IMPLEMENTED
    IDENTIFICADOR = 4  # IMPLEMENTED
    PALABRA_RESERVADA = 5  # IMPLEMENTED
    OPERADOR_ARITMETICO = 6  # IMPLEMENTED
    OPERADOR_COMPARACION = 7  # IMPLEMENTED
    OPERADOR_LOGICO = 8  # IMPLEMENTED
    OPERADOR_ASIGNACION = 9  # IMPLEMENTED
    OPERADOR_INCREMENTO = 10  # IMPLEMENTED
    OPERADOR_DECREMENTO = 11  # IMPLEMENTED
    PARENTESIS = 12  # IMPLEMENTED
    LLAVES = 13  # IMPLEMENTED
    TERMINAL = 14  # IMPLEMENTED
    SEPARADOR = 15  # IMPLEMENTED
    HEXADECIMAL = 16 # IMPLEMENTED
    CADENA_CARACTERES = 17  # IMPLEMENTED
    COMENTARIO_LINEA = 18  # IMPLEMENTED
    COMENTARIO_BLOQUE = 19  # IMPLEMENTED
