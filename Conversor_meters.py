import tkinter as tk # noqa
from tkinter import ttk
from tkinter import * # noqa


def clear_box(box_meter, box_centimeter, box_feet, box_inch, box_mile, box_kilometer, box_yard, box_milimeter): # noqa
    box_centimeter.delete(0, "")
    box_feet.delete(0, "")
    box_inch.delete(0, "")
    box_kilometer.delete(0, "")
    box_mile.delete(0, "")
    box_yard.delete(0, "")
    box_mile.delete(0, "")
    box_meter.delete(0, "")
    box_milimeter.delete(0, "")


def conversor_meters(ventana):

    frame = Frame(ventana) # noqa

    Widget_meter = ttk.Label(frame, text="Metro:")
    Widget_meter.place(x=20, y=25)
    box_meter = ttk.Entry(frame)
    box_meter.place(x=170, y=25, width=75)

    Widget_centimeter = ttk.Label(frame, text="Centimetros:")
    Widget_centimeter.place(x=20, y=50)
    box_centimeter = ttk.Entry(frame)
    box_centimeter.place(x=170, y=50, width=75)

    Widget_milimeter = ttk.Label(frame, text="Milimetros:")
    Widget_milimeter.place(x=20, y=75)
    box_milimeter = ttk.Entry(frame)
    box_milimeter.place(x=170, y=75, width=75)

    Widget_feet = ttk.Label(frame, text="Pies:")
    Widget_feet.place(x=20, y=100)
    box_feet = ttk.Entry(frame)
    box_feet.place(x=170, y=100, width=75)

    Widget_inch = ttk.Label(frame, text="Pulgadas")
    Widget_inch.place(x=20, y=125)
    box_inch = ttk.Entry(frame)
    box_inch.place(x=170, y=125, width=75)

    Widget_mile = ttk.Label(frame, text="Millas:")
    Widget_mile.place(x=20, y=150)
    box_mile = ttk.Entry(frame)
    box_mile.place(x=170, y=150, width=75)

    Widget_kilometer = ttk.Label(frame, text="Kilometros:")
    Widget_kilometer.place(x=20, y=175)
    box_kilometer = ttk.Entry(frame)
    box_kilometer.place(x=170, y=175, width=75)

    Widget_Yard = ttk.Label(frame, text="Yarda:")
    Widget_Yard.place(x=20, y=200)
    box_yard = ttk.Entry(frame)
    box_yard.place(x=170, y=200, width=75)

    def conversion_meter():
        meters = float(box_meter.get())
        centimeter = meters * 100
        milimeter = meters * 1000
        kilometer = meters / 1000
        inch = meters * 39.3701
        feet = meters * 3.28
        yard = meters * 1.094
        mile = meters / 1609.34
        box_centimeter.insert(0, round(centimeter, 7))
        box_milimeter.insert(0, round(milimeter, 8))
        box_kilometer.insert(0, round(kilometer, 7))
        box_inch.insert(0, round(inch, 7))
        box_feet.insert(0, round(feet, 7))
        box_yard.insert(0, round(yard, 7))
        box_mile.insert(0, round(mile, 7))

    def conversion_centimeter():
        centimeter = float(box_centimeter.get())
        meter = centimeter / 100
        milimeter = centimeter * 10
        kilometer = centimeter / 100000
        inch = centimeter * 0.394
        feet = centimeter / 30.48
        yard = centimeter / 91.44
        mile = centimeter / 160934400
        box_milimeter.insert(0, round(milimeter, 7))
        box_kilometer.insert(0, round(kilometer, 7))
        box_inch.insert(0, round(inch, 7))
        box_feet.insert(0, round(feet, 7))
        box_yard.insert(0, round(yard, 7))
        box_mile.insert(0, round(mile, 8))
        box_meter.insert(0, round(meter, 7))

    def conversion_milimeter():
        milimeter = float(box_milimeter.get())
        meter = milimeter / 1000
        centimeter = milimeter / 10
        kilometer = milimeter / 1000000
        inch = milimeter / 25.4
        feet = milimeter / 304.8
        yard = milimeter / 914.4
        mile = milimeter / 1609344
        box_centimeter.insert(0, round(centimeter, 7))
        box_kilometer.insert(0, round(kilometer, 7))
        box_inch.insert(0, round(inch, 7))
        box_feet.insert(0, round(feet, 7))
        box_yard.insert(0, round(yard, 7))
        box_mile.insert(0, round(mile, 8))
        box_meter.insert(0, round(meter, 7))

    def conversion_kilometer():
        kilometer = float(box_kilometer.get())
        centimeter = kilometer * 100000
        meter = kilometer * 1000
        milimeter = kilometer * 1000000
        inch = kilometer * 39370.079
        feet = kilometer * 3280.84
        yard = kilometer * 1093.613
        mile = kilometer * 0.621371192
        box_centimeter.insert(0, round(centimeter, 7))
        box_milimeter.insert(0, round(milimeter, 7))
        box_inch.insert(0, round(inch, 7))
        box_feet.insert(0, round(feet, 7))
        box_yard.insert(0, round(yard, 7))
        box_mile.insert(0, round(mile, 7))
        box_meter.insert(0, round(meter, 7))

    def conversion_inch():
        inch = float(box_inch.get())
        centimeter = inch * 2.54
        meter = inch * 0.0254
        milimeter = inch * 25.4
        kilometer = inch * 0.0000254
        feet = inch / 12
        yard = inch / 36
        mile = inch / 63360
        box_centimeter.insert(0, round(centimeter, 7))
        box_milimeter.insert(0, round(milimeter, 7))
        box_kilometer.insert(0, round(kilometer, 7))
        box_feet.insert(0, round(feet, 7))
        box_yard.insert(0, round(yard, 7))
        box_mile.insert(0, round(mile, 7))
        box_meter.insert(0, round(meter, 7))

    def conversion_feet():
        feet = float(box_feet.get())
        centimeter = feet * 30.48
        meter = feet / 3.28
        milimeter = feet * 304.8
        kilometer = feet * 0.0003048
        inch = feet * 12
        yard = feet / 3
        mile = feet / 5280
        box_centimeter.insert(0, round(centimeter, 7))
        box_milimeter.insert(0, round(milimeter, 7))
        box_kilometer.insert(0, round(kilometer, 7))
        box_inch.insert(0, round(inch, 7))
        box_yard.insert(0, round(yard, 7))
        box_mile.insert(0, round(mile, 7))
        box_meter.insert(0, round(meter, 7))

    def conversion_yard():
        yard = float(box_yard.get())
        centimeter = yard * 91.44
        meter = yard * 0.9144
        milimeter = yard * 914.4
        kilometer = yard / 1093.61
        inch = yard * 36
        feet = yard * 3
        mile = yard / 1760
        box_centimeter.insert(0, round(centimeter, 7))
        box_milimeter.insert(0, round(milimeter, 7))
        box_kilometer.insert(0, round(kilometer, 5))
        box_inch.insert(0, round(inch, 7))
        box_feet.insert(0, round(feet, 7))
        box_mile.insert(0, round(mile, 7))
        box_meter.insert(0, round(meter, 7))

    def conversion_mile():
        mile = float(box_mile.get())
        centimeter = mile * 160934.4
        meter = mile * 1609.344
        milimeter = mile * 1609344.000
        kilometer = mile * 1.609344
        inch = mile * 63360
        feet = mile * 5280
        yard = mile * 1760
        box_centimeter.insert(0, round(centimeter, 7))
        box_milimeter.insert(0, round(milimeter, 7))
        box_kilometer.insert(0, round(kilometer, 7))
        box_inch.insert(0, round(inch, 7))
        box_feet.insert(0, round(feet, 7))
        box_yard.insert(0, round(yard, 7))
        box_meter.insert(0, round(meter, 7))

    button = ttk.Button(frame, text="Convertir", command=lambda: conversion_meter() # noqa
                        if box_meter.get()
                        else conversion_centimeter()
                        if box_centimeter.get()
                        else conversion_feet()
                        if box_feet.get()
                        else conversion_inch()
                        if box_inch.get()
                        else conversion_kilometer()
                        if box_kilometer.get()
                        else conversion_yard()
                        if box_yard.get()
                        else conversion_milimeter()
                        if box_milimeter.get()
                        else conversion_mile())

    button.place(x=20, y=350)

    button_clear = ttk.Button(frame, text="Borrar", command=lambda: clear_box(box_meter, box_centimeter, box_feet, box_inch, box_mile, box_kilometer, box_yard, box_milimeter)) # noqa
    button_clear.place(x=100, y=350)

    return frame
