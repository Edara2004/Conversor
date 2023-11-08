import tkinter as tk
from tkinter import * # noqa
from tkinter import ttk, Menu # noqa
from Conversores.Conversor_Cal import create_pesos_widget
from Conversores.Conversor_temperatura import create_temperaturas_widget
from Conversores.Conversor_Liquid import Liquid_Conversion
from Conversores.Conversor_meters import conversor_meters
from Calculadora_Principal import Calculadora_principal1
from Conversor_Area.Area import Area_conversion
root = tk.Tk() # noqa
root.title("Conversor")
root.geometry("400x400")
root.resizable(False, False)


def hide_main_widget(widget):
    widget.pack_forget()

def show_main_widget(widget): # noqa
    widget.pack(fill=BOTH, expand=YES) # noqa


def create_menu(root, mostrar_pesos_cb, mostrar_temperaturas_cb, mostrar_liquidos_cb, mostrar_medidas_cb, mostrar_metros_cuadrados): # noqa
    bmenu = Menu(root, background="#00ff00",
                 foreground="#ff0000",
                 activebackground="White",
                 activeforeground="Black")
    file = Menu(bmenu, tearoff=0, background='#ffffff', foreground='Black')
    file.add_command(label="Peso", command=mostrar_pesos_cb)
    file.add_command(label="Medidas", command=mostrar_medidas_cb)
    file.add_command(label="Liquido", command=mostrar_liquidos_cb)
    file.add_command(label="Calculadora")
    file.add_command(label="Temperatura", command=mostrar_temperaturas_cb)
    file.add_separator()
    file.add_command(label="Salir", command=root.quit)
    bmenu.add_cascade(label="Conversiones", menu=file)

    file_2 = Menu(bmenu, tearoff=0, background='#ffffff', foreground='Black')
    file_2.add_command(label="Area", command=mostrar_metros_cuadrados)
    bmenu.add_cascade(label="Area", menu=file_2)
    return bmenu


frame_pesos = create_pesos_widget(root)
frame_temperaturas = create_temperaturas_widget(root)
frame_liquid = Liquid_Conversion(root)
frame_meter = conversor_meters(root)
frame_calcu = Calculadora_principal1(root)
frame_Square_meter = Area_conversion(root)


def mostrar_pesos():
    show_main_widget(frame_pesos)
    frame_temperaturas.pack_forget()
    frame_liquid.pack_forget()
    frame_meter.pack_forget()
    frame_Square_meter.pack_forget()


def mostrar_temperaturas():
    show_main_widget(frame_temperaturas)
    frame_pesos.pack_forget()
    frame_liquid.pack_forget()
    frame_meter.pack_forget()
    frame_Square_meter.pack_forget()


def show_liquid():
    show_main_widget(frame_liquid)
    frame_pesos.pack_forget()
    frame_temperaturas.pack_forget()
    frame_meter.pack_forget()
    frame_Square_meter.pack_forget()


def show_meters():
    show_main_widget(frame_meter)
    frame_liquid.pack_forget()
    frame_pesos.pack_forget()
    frame_temperaturas.pack_forget()
    frame_Square_meter.pack_forget()


def show_square_meter():
    show_main_widget(frame_Square_meter)
    frame_pesos.pack_forget()
    frame_calcu.pack_forget()
    frame_liquid.pack_forget()
    frame_temperaturas.pack_forget()
    frame_meter.pack_forget()



root.config(menu=create_menu(root, mostrar_pesos, mostrar_temperaturas, show_liquid, show_meters, show_square_meter)) # noqa

frame_calcu.pack()

root.mainloop()
