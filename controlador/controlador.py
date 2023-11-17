import tkinter as tk


class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def analizar_codigo(self):
        codigo = self.vista.area_codigo.get("1.0", tk.END)
        if codigo.isspace():  # Verify if the code is blank
            table = "The code is empty."
        else:
            self.modelo.establecer_codigo(codigo)
            self.modelo.analizar()
            results = self.modelo.tokens_a_string()
            table = "Lexeme | Category | Position\n" + results

        self.vista.actualizar_resultados(table)
