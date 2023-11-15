import tkinter as tk
from tkinter import scrolledtext


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resultados_texto = None
        self.area_codigo = None
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.title("Analizador Léxico")

        # Establecer tamaño mínimo
        self.minsize(500, 500)

        # Etiqueta de descripción
        descripcion = tk.Label(self, text="Ingresa a continuación el código del lenguaje de programación:")
        descripcion.pack(pady=10)

        # Área de texto para ingresar el código
        self.area_codigo = scrolledtext.ScrolledText(self, width=40, height=10)
        self.area_codigo.pack(pady=10)

        # Botón para analizar el código
        boton_analizar = tk.Button(self, text="Analizar", command=self.analizar_codigo)
        boton_analizar.pack(pady=10)

        # Resultados en una área de texto de solo lectura
        self.resultados_texto = scrolledtext.ScrolledText(self, width=40, height=10, state=tk.DISABLED)
        self.resultados_texto.pack(pady=10)

    def analizar_codigo(self):
        # Esta función debería realizar el análisis léxico y actualizar los resultados en la área de texto
        # Aquí, simplemente se agrega un mensaje de ejemplo
        self.resultados_texto.config(state=tk.NORMAL)
        self.resultados_texto.delete("1.0", tk.END)
        self.resultados_texto.insert(tk.END, "Ejemplo de resultado:\nLexema | Categoría | Posición\nif     | Palabra Reservada | 1-2\n")
        self.resultados_texto.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
