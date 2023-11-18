# main.py
import tkinter as tk
from modelo.modelo import AnalizadorLexico
from vista.vista import Vista
from controlador.controlador import Controlador

if __name__ == "__main__":
    modelo = AnalizadorLexico()
    root = tk.Tk()
    controlador = Controlador(modelo, None)
    vista = Vista(root, controlador)
    controlador.vista = vista
    root.mainloop()
