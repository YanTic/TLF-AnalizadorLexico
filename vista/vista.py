# vista.py
import tkinter as tk
import tkinter.scrolledtext


class Vista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.root.title("Analizador Léxico")
        self.root.minsize(500, 400)

        self.descripcion = tk.Label(root, text="Ingresa a continuación el código del lenguaje de programación:")
        self.descripcion.pack(pady=10)

        self.area_codigo = tk.scrolledtext.ScrolledText(root, width=40, height=10)
        self.area_codigo.pack(pady=10)

        self.boton_analizar = tk.Button(root, text="Analizar", command=self.controlador.analizar_codigo)
        self.boton_analizar.pack(pady=10)

        self.resultados_texto = tk.scrolledtext.ScrolledText(root, width=40, height=10, state=tk.DISABLED)
        self.resultados_texto.pack(pady=10)

    def actualizar_resultados(self, resultados):
        self.resultados_texto.configure(state=tk.NORMAL)
        self.resultados_texto.delete("1.0", tk.END)
        self.resultados_texto.insert(tk.END, resultados)
        self.resultados_texto.configure(state=tk.DISABLED)
