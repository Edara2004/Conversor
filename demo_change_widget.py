# Imports tkinter 
from tkinter import *
  

from tkinter import ttk
from Conversor_Cal import Kilogramos
from Conversor_temperatura import create_temperaturas_widget

# toplevel window 
root = Tk() 
root.geometry("500x500")

# Method to make Button(Widget) invisible from toplevel 
  
  
def hide_main_widget(widget): 
    # This will remove the widget from toplevel 
    widget.pack_forget() 
  
  
def show_main_widget(widget): 
    # This will recover the widget from toplevel 
    widget.pack(fill=BOTH, expand=YES)
 
  
def create_pesos_widget():
    """
    Crear todos los componentes y asociar las acciones.
    """
    frame = Frame(root, bg="blue")

    return frame







def create_menu(ventana, mostrar_pesos_cb, mostrar_temperaturas_cb):
    bmenu = Menu(ventana, background="#00ff00", foreground= "#ff0000", activebackground="White", activeforeground="Black")
    file = Menu(bmenu, tearoff=0, background='#ffffff', foreground='Black')
    file.add_command(label="Peso", command=mostrar_pesos_cb)
    file.add_command(label="Medidas")
    file.add_command(label="Liquido")
    file.add_command(label="Calculadora" )
    file.add_command(label="Temperatura", command=mostrar_temperaturas_cb)
    file.add_separator()
    file.add_command(label="Salir", command=ventana.quit)
    bmenu.add_cascade(label="Conversiones", menu=file)

    return bmenu


frame_pesos = create_pesos_widget()

frame_temperaturas = create_temperaturas_widget(root)


def mostar_pesos():
    """
    Poner en la ventana sólo el frame de Pesos y ocular el anterior (o todos los anteriores)
    """
    show_main_widget(frame_pesos)
    hide_main_widget(frame_temperaturas)


def mostrar_temperaturas():
    """
    Poner en la ventana sólo el frame de Temperatura y ocular el anterior (o todos los anteriores)
    """
    show_main_widget(frame_temperaturas)
    hide_main_widget(frame_pesos)


root.config(menu=create_menu(root, mostar_pesos, mostrar_temperaturas))

root.mainloop() 