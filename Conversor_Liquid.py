import tkinter as tk # noqa
from tkinter import ttk
from tkinter import * # noqa


def clear_box(box_liters, box_gal, box_mililiters, box_ounces):
    box_liters.delete(0, "")
    box_gal.delete(0, "")
    box_mililiters.delete(0, "")
    box_ounces.delete(0, "")


def Liquid_Conversion(ventana):

    frame = Frame(ventana) # noqa

    widget_liters = ttk.Label(frame, text="Litros")
    widget_liters.place(x=20, y=25)
    box_liters = ttk.Entry(frame)
    box_liters.place(x=170, y=25, width=60)

    widget_gal = ttk.Label(frame, text="Galones")
    widget_gal.place(x=20, y=50)
    box_gal = ttk.Entry(frame)
    box_gal.place(x=170, y=50, width=60)

    widget_mililiters = ttk.Label(frame, text="Mililitros")
    widget_mililiters.place(x=20, y=75)
    box_mililiters = ttk.Entry(frame)
    box_mililiters.place(x=170, y=75, width=60)

    widget_ounces = ttk.Label(frame, text="Onzas")
    widget_ounces.place(x=20, y=100)
    box_ounces = ttk.Entry(frame)
    box_ounces.place(x=170, y=100, width=60)

    button_delete = ttk.Button(frame, text="Borrar")
    button_delete.place(x=100, y=350)

    def conversion_liters():
        liters = float(box_liters.get())
        gal = liters * 0.264
        mililiters = liters * 1000
        ounces = liters * 33.814
        box_gal.insert(0, round(gal, 4))
        box_mililiters.insert(0, round(mililiters, 4))
        box_ounces.insert(0, round(ounces, 4))

    def conversion_gal():
        gal = float(box_gal.get())
        liters = gal / 0.264
        mililiters = gal / 0.000264
        ounces = gal / 0.00781
        box_liters.insert(0, round(liters, 4))
        box_mililiters.insert(0, round(mililiters, 4))
        box_ounces.insert(0, round(ounces, 4))

    def conversion_mililiter():
        mililiters = float(box_mililiters.get())
        liters = mililiters / 1000
        gal = mililiters * 0.000264
        ounces = mililiters * 0.0338
        box_liters.insert(0, round(liters, 4))
        box_gal.insert(0, round(gal, 4))
        box_ounces.insert(0, round(ounces, 4))

    def conversion_ounces():
        ounces = float(box_ounces.get())
        liters = ounces / 33.814
        gal = ounces * 0.00781
        mililiters = ounces / 0.0338
        box_liters.insert(0, round(liters, 4))
        box_gal.insert(0, round(gal, 4))
        box_mililiters.insert(0, round(mililiters, 4))

    button = ttk.Button(frame, text="Convertir", command=lambda: conversion_liters() # noqa
                        if box_liters.get()
                        else conversion_gal()
                        if box_gal.get()
                        else conversion_mililiter()
                        if box_mililiters.get()
                        else conversion_ounces())
    button.place(x=20, y= 350)

    button_clear_all = ttk.Button(frame, text="Borrar", command=lambda: clear_box(box_liters, box_gal, box_ounces, box_mililiters))  # noqa
    button_clear_all.place(x=100, y=350)
    return frame
