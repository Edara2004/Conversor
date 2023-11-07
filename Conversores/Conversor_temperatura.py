import tkinter as tk # noqa
from tkinter import ttk
from tkinter import * # noqa


# Creamos la funcion para convertir
def borrar_cajas(caja_temp_cel, caja_temp_kelvin, caja_temp_farenheit):
        caja_temp_cel.delete(0, "") # noqa
        caja_temp_kelvin.delete(0, "")
        caja_temp_farenheit.delete(0, "")


def create_temperaturas_widget(ventana):
    """
    Crear todos los componentes y asociar las acciones.
    """

    frame = Frame(ventana) # noqa

    # Definimos el texto del boton

    etiqueta_temp_celsius = ttk.Label(frame, text="Ingresar temperatura en °C")
    # Definimos el lugar donde va el boton

    etiqueta_temp_celsius.place(x=20, y=25)

    # Definimos donde va el input

    caja_temp_cel = ttk.Entry(frame)

    # Definimos donde va el input

    caja_temp_cel.place(x=170, y=25, width=75)

    # Definimos las etiquetas Kelvin

    etiqueta_temp_kelvin = ttk.Label(frame, text="Temperatura en K: ")
    etiqueta_temp_kelvin.place(x=20, y=50)
    caja_temp_kelvin = ttk.Entry(frame)
    caja_temp_kelvin.place(x=170, y=50, width=75)

    # Definimos los Farenheits

    etiqueta_temp_farenheit = ttk.Label(frame, text="Temperatura en F: ")
    etiqueta_temp_farenheit.place(x=20, y=75)
    caja_temp_farenheit = ttk.Entry(frame)
    caja_temp_farenheit.place(x=170, y=75, width=75)

    # Creamos el boton borrar
    boton_borrar = ttk.Button(frame, text="Borrar", command=lambda: borrar_cajas(caja_temp_cel, caja_temp_kelvin, caja_temp_farenheit)) # noqa
    boton_borrar.place(x=100, y=350)

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

    # Definimos el buttom

    boton_convertir = ttk.Button(frame, text="Convertir", command=lambda: convertir() # noqa
                                if caja_temp_cel.get() # noqa
                                else convertir_kelvin() # noqa
                                if caja_temp_kelvin.get() # noqa
                                else convertir_fahrenheit()) # noqa

    # Definimos el lugar del boton

    boton_convertir.place(x=20, y=350)

    return frame
