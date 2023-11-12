from tkinter import *
from modelo.AnalizadorLexico import AnalizadorLexico
from modelo.Categoria import Categoria


def main():
    test = AnalizadorLexico("Julian")
    test.saludar()

    categoria = Categoria.ENTERO
    print(categoria.value)

    window = Tk()
    window.geometry("420x420")
    window.mainloop()


main()
