import tkinter as tk
from tkinter import ttk
from tkinter import *
from Conversor_Cal import Kilogramos


#Creamos la funcion para convertir

def convertir():
    temp_celsius = float(caja_temp_cel.get())
    temp_kelvin = temp_celsius + 273.15
    temp_farenheit = temp_celsius * 1.8 + 32
    caja_temp_kelvin.insert(0, temp_kelvin)
    caja_temp_farenheit.insert(0, temp_farenheit)

def convertir_kelvin():
    temp_kelvin = float(caja_temp_kelvin.get())
    temp_celsius = temp_kelvin - 273.15
    temp_farenheit = ((temp_kelvin - 273.15) * 1.8) + 32
    caja_temp_cel.insert(0, temp_celsius)
    caja_temp_farenheit.insert(0, temp_farenheit)

def convertir_fahrenheit():
    temp_fahrenheit = float(caja_temp_farenheit.get())
    temp_kelvin = ((temp_fahrenheit - 32) / 1.8) + 273.15
    temp_celsius = (temp_fahrenheit - 32) / 1.8
    caja_temp_cel.insert(0, temp_celsius)
    caja_temp_kelvin.insert(0, temp_kelvin)

def borrar_cajas():
    caja_temp_cel.delete(0, "")
    caja_temp_kelvin.delete(0, "")
    caja_temp_farenheit.delete(0, "")




ventana = tk.Tk()
# Definimos tamaño
ventana.title("Conversor de temperatura")
ventana.config(width= 400, height= 400)

notebook = ttk.Notebook(ventana)
pestaña_peso = ttk.Frame(notebook)
#Crear Barra de menu

Barra_menu = Menu(ventana, background="#00ff00", foreground= "#ff0000", activebackground="White", activeforeground="Black")
file = Menu(Barra_menu, tearoff=0, background='#ffffff', foreground='Black')
file.add_command(label="Peso", command=Kilogramos)
file.add_command(label="Medidas")
file.add_command(label="Liquido")
file.add_command(label="Calculadora" )
file.add_separator()
file.add_command(label="Salir", command=ventana.quit)
Barra_menu.add_cascade(label="Conversiones", menu=file)



# Definimos el texto del boton

etiqueta_temp_celsius = ttk.Label(text= "Ingresar temperatura en °C")
# Definimos el lugar donde va el boton

etiqueta_temp_celsius.place(x=20, y=25)

# Definimos donde va el input

caja_temp_cel = ttk.Entry()

#Definimos donde va el input

caja_temp_cel.place(x= 170, y= 25, width= 60)

# Creamos el boton borrar

boton_borrar = ttk.Button(text="Borrar", command= borrar_cajas)
boton_borrar.place(x=100, y= 350)

# Definimos las etiquetas Kelvin

etiqueta_temp_kelvin = ttk.Label(text= "Temperatura en K: ")
etiqueta_temp_kelvin.place(x=20, y=50)
caja_temp_kelvin = ttk.Entry()
caja_temp_kelvin.place(x=170 , y=50, width=60)

# Definimos los Farenheits

etiqueta_temp_farenheit = ttk.Label(text="Temperatura en F: ")
etiqueta_temp_farenheit.place(x=20, y=75)
caja_temp_farenheit = ttk.Entry()
caja_temp_farenheit.place(x=170, y= 75, width=60)

#Definimos el buttom 

boton_convertir = ttk.Button(text="Convertir", command=lambda: convertir() 
                             if caja_temp_cel.get() 
                             else convertir_kelvin() 
                             if caja_temp_kelvin.get() 
                             else convertir_fahrenheit())

# Definimos el lugar del boton

boton_convertir.place(x=20, y= 350)

ventana.config(menu=Barra_menu)

ventana.mainloop()

