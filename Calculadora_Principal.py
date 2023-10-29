import tkinter as tk
from tkinter import ttk
from tkinter import *
import Conversor_Cal
import Conversor_temperatura

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.config(width=400, height=400)

Barra_menu = Menu(ventana, background="#00ff00", foreground= "#ff0000", activebackground="White", activeforeground="Black")
file = Menu(Barra_menu, tearoff=0, background='#ffffff', foreground='Black')
file.add_command(label="Peso", command=lambda:(ventana, Conversor_Cal.Kilogramos()))
file.add_command(label="Medidas")
file.add_command(label="Liquido")
file.add_command(label="Calculadora" )
file.add_command(label="Temperatura", command=lambda:(ventana, Conversor_temperatura))
file.add_separator()
file.add_command(label="Salir", command=ventana.quit)
Barra_menu.add_cascade(label="Conversiones", menu=file)


ventana.config(menu=Barra_menu)

ventana.mainloop()