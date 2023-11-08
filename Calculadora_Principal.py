from tkinter import ttk, Label, Frame, Button, Entry # noqa


def Calculadora_principal1(ventana):

    frame = Frame(ventana)

    Boton1 = ttk.Button(frame, text="Hola")
    Boton1.place(x=120, y=25)
    caja = ttk.Entry(frame)
    caja.place(x=25, y=25, width=60)
    Texto = Label(frame, text="Hola Gente")
    Texto.place(x=50, y=50)

    return frame
