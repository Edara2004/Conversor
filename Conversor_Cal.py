
from tkinter import ttk
from tkinter import * # noqa


def clear_box(caja_peso_kilo, caja_peso_gramos, caja_peso_onzas, caja_peso_libras, caja_peso_mil): # noqa
    caja_peso_gramos.delete(0, "")
    caja_peso_kilo.delete(0, "")
    caja_peso_onzas.delete(0, "")
    caja_peso_libras.delete(0, "")
    caja_peso_mil.delete(0, "")


def create_pesos_widget(ventana):
    frame = Frame(ventana) # noqa

    etiqueta_peso_kilo = ttk.Label(frame, text="Peso en Kilos:")
    etiqueta_peso_kilo.place(x=20, y=25)
    caja_peso_kilo = ttk.Entry(frame)
    caja_peso_kilo.place(x=170, y=25, width=75)

    etiqueta_peso_libra = ttk.Label(frame, text="Peso en Libras:")
    etiqueta_peso_libra.place(x=20, y=50)
    caja_peso_libras = ttk.Entry(frame)
    caja_peso_libras.place(x=170, y=50, width=75)

    etiqueta_peso_gramo = ttk.Label(frame, text="Peso en Gramos:")
    etiqueta_peso_gramo.place(x=20, y=75)
    caja_peso_gramos = ttk.Entry(frame)
    caja_peso_gramos.place(x=170, y=75, width=75)

    etiqueta_peso_onza = ttk.Label(frame, text="Peso en Onzas:")
    etiqueta_peso_onza.place(x=20, y=100)
    caja_peso_onzas = ttk.Entry(frame)
    caja_peso_onzas.place(x=170, y=100, width=75)

    etiqueta_peso_mil = ttk.Label(frame, text="Peso en Miligramos:")
    etiqueta_peso_mil.place(x=20, y=125)
    caja_peso_mil = ttk.Entry(frame)
    caja_peso_mil.place(x=170, y=125, width=75)

    def convertir_kilos():
        peso_kilos = float(caja_peso_kilo.get())
        peso_libras = peso_kilos * 2.20
        peso_gramos = peso_kilos * 1000
        peso_onzas = peso_kilos * 35.27
        peso_mil = peso_kilos * 1000000
        caja_peso_libras.insert(0, round(peso_libras, 3))
        caja_peso_gramos.insert(0, round(peso_gramos, 3))
        caja_peso_onzas.insert(0, round(peso_onzas, 3))
        caja_peso_mil.insert(0, round(peso_mil, 10))

    def convertir_libras():
        peso_libras = float(caja_peso_libras.get())
        peso_kilos = peso_libras / 2.2
        peso_gramos = peso_libras * 453.59
        peso_onzas = peso_libras * 16
        peso_mil = peso_libras * 453
        caja_peso_kilo.insert(0, round(peso_kilos, 3))
        caja_peso_gramos.insert(0, round(peso_gramos, 3))
        caja_peso_onzas.insert(0, round(peso_onzas, 3))
        caja_peso_mil.insert(0, round(peso_mil, 10))

    def convertir_gramos():
        peso_gramos = float(caja_peso_gramos.get())
        peso_kilos = peso_gramos / 1000
        peso_libras = peso_gramos / 2.2
        peso_onzas = peso_gramos / 28
        peso_mil = peso_gramos * 1000
        caja_peso_kilo.insert(0, round(peso_kilos, 3))
        caja_peso_libras.insert(0, round(peso_libras, 3))
        caja_peso_onzas.insert(0, round(peso_onzas, 3))
        caja_peso_mil.insert(0, round(peso_mil, 10))

    def convertir_onzas():
        peso_onzas = float(caja_peso_onzas.get())
        peso_kilos = peso_onzas * 0.028
        peso_gramos = peso_onzas * 28.34
        peso_libras = peso_onzas / 16
        peso_mil = peso_onzas * 28349.52
        caja_peso_kilo.insert(0, round(peso_kilos, 3))
        caja_peso_gramos.insert(0, round(peso_gramos, 3))
        caja_peso_libras.insert(0, round(peso_libras, 3))
        caja_peso_mil.insert(0, round(peso_mil, 10))

    def convertir_miligram():
        peso_miligram = float(caja_peso_mil.get())
        peso_kilos = peso_miligram / 1000000
        peso_libras = peso_miligram / 453
        peso_onzas = peso_miligram / 28.35
        peso_gramos = peso_miligram / 1000
        caja_peso_gramos.insert(0, round(peso_gramos, 3))
        caja_peso_kilo.insert(0, round(peso_kilos, 3))
        caja_peso_libras.insert(0, round(peso_libras, 3))
        caja_peso_onzas.insert(0, round(peso_onzas, 10))

    boton_convertir = ttk.Button(frame, text="Convertir", command= lambda: convertir_kilos() # noqa
                                 if caja_peso_kilo.get()
                                 else convertir_libras()
                                 if caja_peso_libras.get()
                                 else convertir_gramos()
                                 if caja_peso_gramos.get()
                                 else convertir_onzas()
                                 if caja_peso_onzas.get()
                                 else convertir_miligram())

    boton_borrar= ttk.Button(frame, text="Borrar", command=lambda:clear_box(caja_peso_kilo, caja_peso_libras, caja_peso_gramos, caja_peso_onzas, caja_peso_mil)) # noqa
    boton_borrar.place(x=100,  y=350)

    boton_convertir.place(x=20, y=350)

    return frame
