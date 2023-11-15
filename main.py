# main.py
import tkinter as tk
from modelo.modelo import Modelo
from vista.vista import Vista
from controlador.controlador import Controlador

if __name__ == "__main__":
    modelo = Modelo()
    root = tk.Tk()
    controlador = Controlador(modelo, None)  # No asociar la vista inicialmente
    vista = Vista(root, controlador)
    controlador.vista = vista  # Actualizar la vista en el controlador
    root.mainloop()

