class Categoria:
    def esNumeroNatural(cadena):
        numerosNaturales = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        for caracterActual in cadena:
            if caracterActual not in numerosNaturales:
                return False

        return True

