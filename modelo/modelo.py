class Modelo:
    def __init__(self):
        self.codigo = ""

    def establecer_codigo(self, codigo):
        self.codigo = codigo

    def obtener_codigo(self):
        return self.codigo


class AnalizadorLexico:
    def __init__(self, codigo_fuente):
        self.codigo_fuente = codigo_fuente
        self.lista_tokens = []

    def analizar(self):
        i = 0
        while i < len(self.codigo_fuente):
            token = self.extraer_sgte_token(i)
            if token is not None:
                self.lista_tokens.append(token)
            else:
                i += 1

    def extraer_sgte_token(self, indice):
        token = self.extraer_entero(indice)
        if token is not None:
            return token

        # TODO: Llamar aquí todos los métodos de extraer, extraer_decimal, extraer_identificador, etc.

        token = self.extraer_no_reconocido(indice)
        return token

    def extraer_entero(self, indice):
        if indice < len(self.codigo_fuente) and self.codigo_fuente[indice].isdigit():
            posicion = indice
            while indice < len(self.codigo_fuente) and self.codigo_fuente[indice].isdigit():
                indice += 1
            return Token(self.codigo_fuente[posicion:indice], Categoria.ENTERO, indice)
        return None

    def extraer_no_reconocido(self, indice):
        lexema = self.codigo_fuente[indice:indice + 1]
        return Token(lexema, Categoria.NO_RECONOCIDO, indice + 1)

    def get_lista_tokens(self):
        return self.lista_tokens


class Token:
    def __init__(self, palabra, categoria, indice_siguiente):
        self.palabra = palabra
        self.categoria = categoria
        self.indice_siguiente = indice_siguiente


class Categoria:
    NO_RECONOCIDO = 1
    ENTERO = 2
    DECIMAL = 3
    IDENTIFICADOR = 4
    PALABRA_RESERVADA = 5
    OPERADOR_ARITMETICO = 6
    OPERADOR_COMPARACION = 7
    OPERADOR_LOGICO = 8
    OPERADOR_ASIGNACION = 9
    OPERADOR_INCREMENTO = 10
    OPERADOR_DECREMENTO = 11
    PARENTESIS_APERTURA = 12
    PARENTESIS_CIERRE = 13
    LLAVE_APERTURA = 14
    LLAVE_CIERRE = 15
    TERMINAL = 16
    SEPARADOR = 17
    HEXADECIMAL = 18
    CADENA_CARACTERES = 19
    COMENTARIO_LINEA = 20
    COMENTARIO_BLOQUE = 21
