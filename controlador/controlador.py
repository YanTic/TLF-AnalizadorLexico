import tkinter as tk


# controlador.py
class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def analizar_codigo(self):
        codigo = self.vista.area_codigo.get("1.0", tk.END)
        self.modelo.establecer_codigo(codigo)

        # Lógica del analizador léxico (simplificada)
        resultados = "Ejemplo de resultado:\nLexema | Categoría | Posición\nif     | Palabra Reservada | 1-2\n"

        self.vista.actualizar_resultados(resultados)
