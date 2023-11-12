from Token import Token


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


# Ejemplo de uso
codigo_fuente_ejemplo = "123 abc 45"
analizador = AnalizadorLexico(codigo_fuente_ejemplo)
analizador.analizar()

for token in analizador.get_lista_tokens():
    print(f"Palabra: {token.palabra}, Categoría: {token.categoria}, Índice Siguiente: {token.indice_sgte}")
