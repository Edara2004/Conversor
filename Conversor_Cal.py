import tkinter as tk
from tkinter import ttk
from tkinter import *

class Kilogramos():

    


    def Kilogramo():
        etiqueta_peso_kilo= ttk.Label(text="Peso en Kilos")
        etiqueta_peso_kilo.place(x=20, y= 25)
        caja_peso_kilo= ttk.Entry()
        caja_peso_kilo.place(x=170, y=25, width=60)


    def Libra():       
        etiqueta_peso_libra= ttk.Label(text="Peso en Libras")
        etiqueta_peso_libra.place(x=20, y= 50)
        caja_peso_libras = ttk.Entry()
        caja_peso_libras.place(x=170, y= 150, width=60)

    

    