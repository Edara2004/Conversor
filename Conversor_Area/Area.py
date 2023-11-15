from tkinter import ttk, Label, Frame


def clear_box(box_square_meter, box_square_hectometer, box_square_decameter, box_square_decimeter, box_square_centimeter, box_square_kilometer, box_square_milimeter, box_square_yard, box_square_feet, box_square_inch, box_square_mile): # noqa
    box_square_centimeter.delete(0, "")
    box_square_meter.delete(0, "")
    box_square_hectometer.delete(0, "")
    box_square_decameter.delete(0, "")
    box_square_decimeter.delete(0, "")
    box_square_kilometer.delete(0, "")
    box_square_milimeter.delete(0, "")
    box_square_yard.delete(0, "")
    box_square_feet.delete(0, "")
    box_square_inch.delete(0, "")
    box_square_mile.delete(0, "")


def Area_conversion(ventana):

    frame = Frame(ventana)

    widget_square_meter = Label(frame, text="Metro Cuadrado")
    widget_square_meter.place(x=20, y=25)
    box_square_meter = ttk.Entry(frame)
    box_square_meter.place(x=170, y=25, width=75)
    Abbreviation_square_meter = Label(frame, text="m²", width=2)
    Abbreviation_square_meter.place(x=250, y=25)

    widget_square_hectometer = Label(frame, text="Hectómetro Cuadrado")
    widget_square_hectometer.place(x=20, y=50)
    box_square_hectometer = ttk.Entry(frame)
    box_square_hectometer.place(x=170, y=50, width=75)
    Abbreviation_square_hectometer = Label(frame, text="hm²", width=3)
    Abbreviation_square_hectometer.place(x=250, y=50)

    widget_square_decameter = Label(frame, text="Decámetro Cuadrado")
    widget_square_decameter.place(x=20, y=75)
    box_square_decameter = ttk.Entry(frame)
    box_square_decameter.place(x=170, y=75, width=75)
    Abbreviation_square_decameter = Label(frame, text="dam²", width=4)
    Abbreviation_square_decameter.place(x=250, y=75)

    widget_square_decimeter = Label(frame, text="Decímetro Cuadrado")
    widget_square_decimeter.place(x=20, y=100)
    box_square_decimeter = ttk.Entry(frame)
    box_square_decimeter.place(x=170, y=100, width=75)
    Abbreviation_square_decimeter = Label(frame, text="dm²", width=3)
    Abbreviation_square_decimeter.place(x=250, y=100)

    widget_square_centimeter = Label(frame, text="Centímetro Cuadrado")
    widget_square_centimeter.place(x=20, y=125)
    box_square_centimeter = ttk.Entry(frame)
    box_square_centimeter.place(x=170, y=125, width=75)
    Abbreviation_square_centimeter = Label(frame, text="cm²", width=3)
    Abbreviation_square_centimeter.place(x=250, y=125)

    widget_square_kilometer = Label(frame, text="Kilómetro Cuadrado")
    widget_square_kilometer.place(x=20, y=150)
    box_square_kilometer = ttk.Entry(frame)
    box_square_kilometer.place(x=170, y=150, width=75)
    Abbreviation_square_kilometer = Label(frame, text="Km²", width=3)
    Abbreviation_square_kilometer.place(x=250, y=150)

    widget_square_milimeter = Label(frame, text="Milímetro Cuadrado")
    widget_square_milimeter.place(x=20, y=175)
    box_square_milimeter = ttk.Entry(frame)
    box_square_milimeter.place(x=170, y=175, width=75)
    Abbreviation_square_milimeter = Label(frame, text="mm²")
    Abbreviation_square_milimeter.place(x=250, y=175)

    widget_square_yard = Label(frame, text="Yarda Cuadrada")
    widget_square_yard.place(x=20, y=200)
    box_square_yard = ttk.Entry(frame)
    box_square_yard.place(x=170, y=200, width=75)
    Abbreviation_square_yard = Label(frame, text="yd²", width=2)
    Abbreviation_square_yard.place(x=250, y=200)

    widget_square_feet = Label(frame, text="Pies Cuadrados")
    widget_square_feet.place(x=20, y=225)
    box_square_feet = ttk.Entry(frame)
    box_square_feet.place(x=170, y=225, width=75)
    Abbreviation_square_feet = Label(frame, text="ft²", width=3)
    Abbreviation_square_feet.place(x=250, y=225)

    widget_square_inch = Label(frame, text="Pulgada Cuadrada")
    widget_square_inch.place(x=20, y=250)
    box_square_inch = ttk.Entry(frame)
    box_square_inch.place(x=170, y=250, width=75)
    Abbreviation_square_inch = Label(frame, text="in²", width=3)
    Abbreviation_square_inch.place(x=250, y=250)

    widget_square_mile = Label(frame, text="Milla Cuadrada")
    widget_square_mile.place(x=20, y=275)
    box_square_mile = ttk.Entry(frame)
    box_square_mile.place(x=170, y=275, width=75)
    Abbreviation_square_mile = Label(frame, text="mi²", width=3)
    Abbreviation_square_mile.place(x=250, y=275)

    def conversion_meter():
        square_meter = float(box_square_meter.get())
        square_hectometer = square_meter / 10000
        square_decameter = square_meter / 100
        square_decimeter = square_meter * 100
        square_centimeter = square_meter * 10000
        square_kilometer = square_meter / 1000000
        square_milimeter = square_meter * 1000000
        square_yard = square_meter * 1.196
        square_feet = square_meter * 10.764
        square_inch = square_meter * 1550.0003
        square_mile = square_meter / 259000
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_hectometer():
        square_hectometer = float(box_square_hectometer.get())
        square_meter = square_hectometer * 10000
        square_decameter = square_hectometer * 100
        square_decimeter = square_hectometer * 1000000
        square_centimeter = square_hectometer * 100000000
        square_kilometer = square_hectometer / 100
        square_milimeter = square_hectometer * 10000000000
        square_yard = square_hectometer * 11960
        square_feet = square_hectometer * 107640
        square_inch = square_hectometer * 15500003
        square_mile = square_hectometer / 25.90000
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_decameter():
        square_decameter = float(box_square_decameter.get())
        square_meter = square_decameter * 100
        square_hectometer = square_decameter / 100
        square_decimeter = square_decameter * 10000
        square_centimeter = square_decameter * 1000000
        square_kilometer = square_decameter / 10000
        square_milimeter = square_decameter * 100000000
        square_yard = square_decameter * 119.60
        square_feet = square_decameter * 1076.4
        square_inch = square_decameter * 155000.03
        square_mile = square_decameter / 2590
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_decimeter():
        square_decimeter = float(box_square_decimeter.get())
        square_meter = square_decimeter / 100
        square_hectometer = square_decimeter / 1000000
        square_decameter = square_decimeter / 10000
        square_centimeter = square_decimeter * 100
        square_kilometer = square_decimeter / 100000000
        square_milimeter = square_decimeter * 10000
        square_yard = square_decimeter * 0.01196
        square_feet = square_decimeter * 0.10764
        square_inch = square_decimeter * 15.500003
        square_mile = square_decimeter / 25900000
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_centimeter():
        square_centimeter = float(box_square_centimeter.get())
        square_meter = square_centimeter / 10000
        square_hectometer = square_centimeter / 100000000
        square_decimeter = square_centimeter / 100
        square_decameter = square_centimeter / 1000000
        square_kilometer = square_centimeter / 10000000000
        square_milimeter = square_centimeter * 100
        square_yard = square_centimeter * 0.0001196
        square_feet = square_centimeter * 0.0010764
        square_inch = square_centimeter * 0.1550003
        square_mile = square_centimeter / 2590000000
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_kilometer():
        square_kilometer = float(box_square_kilometer.get())
        square_meter = square_kilometer * 1000000
        square_hectometer = square_kilometer / 0.01
        square_decimeter = square_kilometer * 100000000
        square_centimeter = square_kilometer * 10000000000
        square_decameter = square_kilometer / 0.0001
        square_milimeter = square_kilometer * 1000000000000
        square_yard = square_kilometer * 1196000
        square_feet = square_kilometer * 10764000
        square_inch = square_kilometer * 155000300.00
        square_mile = square_kilometer * 3.8600
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_milimeter():
        square_milimeter = float(box_square_milimeter.get())
        square_meter = square_milimeter / 1000000
        square_hectometer = square_milimeter / 10000000000
        square_decimeter = square_milimeter / 10000
        square_centimeter = square_milimeter / 100
        square_kilometer = square_milimeter / (1000000 * 1000000)
        square_decameter = square_milimeter / 100000000
        square_yard = square_milimeter * 0.000001196
        square_feet = square_milimeter * 0.000010764
        square_inch = square_milimeter * 0.0015500003
        square_mile = square_milimeter / 259000000000
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_yard():
        square_yard = float(box_square_yard.get())
        square_meter = square_yard * 0.83612
        square_hectometer = square_yard * 0.00011959902
        square_decimeter = square_yard * 9.290304
        square_centimeter = square_yard * 929.0304
        square_kilometer = square_yard * 0.00000083612736
        square_milimeter = square_yard * 83612.7
        square_decameter = square_yard * 0.83612736
        square_feet = square_yard * 9
        square_inch = square_yard * 1296
        square_mile = square_yard /  0.25900
        box_square_meter.insert(0, round(square_meter, 6))
        box_square_hectometer.insert(0, round(square_hectometer, 4))
        box_square_decameter.insert(0, round(square_decameter, 6))
        box_square_decimeter.insert(0, round(square_decimeter, 6))
        box_square_centimeter.insert(0, round(square_centimeter, 6))
        box_square_kilometer.insert(0, round(square_kilometer, 6))
        box_square_milimeter.insert(0, round(square_milimeter, 6))
        box_square_feet.insert(0, round(square_feet, 6))
        box_square_inch.insert(0, round(square_inch, 6))
        box_square_mile.insert(0, round(square_mile, 6))

    def conversion_feet():
        square_feet = float(box_square_feet.get())
        square_meter = square_feet / 0.0929
        square_hectometer = square_feet / 929
        square_decimeter = square_feet * 100
        square_centimeter = square_feet * 929.03
        square_kilometer = square_feet / 929
        square_milimeter = square_feet * 92903
        square_yard = square_feet / 0.3048
        square_decameter = square_feet / 9.29
        square_inch = square_feet * 144
        square_mile = square_feet / 27878400
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_inch.insert(0, round(square_inch, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_inch():
        square_inch = float(box_square_inch.get())
        square_meter = square_inch * 0.00064516
        square_hectometer = square_inch * 0.00000064516
        square_decimeter = square_inch * 6.4516
        square_centimeter = square_inch * 645.16
        square_kilometer = square_inch / 9290000000
        square_milimeter = square_inch * 645.16
        square_yard = square_inch / 9.290304
        square_feet = square_inch / 144
        square_decameter = square_inch / 645.16
        square_mile = square_inch / (63360 * 63360)
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_mile.insert(0, round(square_mile, 8))

    def conversion_mile():
        square_mile = float(box_square_mile.get())
        square_meter = square_mile * 2590000
        square_hectometer = square_mile * 25.9
        square_decimeter = square_mile * (100 * 100 * 100 * 5280 * 5280)
        square_centimeter = square_mile * 2.589988110336
        square_kilometer = square_mile * 1.609344
        square_milimeter = square_mile * 258999846000000
        square_yard = square_mile / 0.00000000000003228
        square_feet = square_mile * 27878400
        square_inch = square_mile * (63360 * 63360)
        square_decameter = square_mile / 0.0000003861
        box_square_meter.insert(0, round(square_meter, 8))
        box_square_hectometer.insert(0, round(square_hectometer, 8))
        box_square_decameter.insert(0, round(square_decameter, 8))
        box_square_decimeter.insert(0, round(square_decimeter, 8))
        box_square_centimeter.insert(0, round(square_centimeter, 8))
        box_square_kilometer.insert(0, round(square_kilometer, 8))
        box_square_milimeter.insert(0, round(square_milimeter, 8))
        box_square_yard.insert(0, round(square_yard, 8))
        box_square_feet.insert(0, round(square_feet, 8))
        box_square_inch.insert(0, round(square_inch, 8))

    button_conversion = ttk.Button(frame, text="Convertir", command=lambda: conversion_meter() # noqa
                                   if box_square_meter.get()
                                   else conversion_hectometer()
                                   if box_square_hectometer.get()
                                   else conversion_decameter()
                                   if box_square_decameter.get()
                                   else conversion_decimeter()
                                   if box_square_decimeter.get()
                                   else conversion_centimeter()
                                   if box_square_centimeter.get()
                                   else conversion_kilometer()
                                   if box_square_kilometer.get()
                                   else conversion_milimeter()
                                   if box_square_milimeter.get()
                                   else conversion_yard()
                                   if box_square_yard.get()
                                   else conversion_feet()
                                   if box_square_feet.get()
                                   else conversion_inch()
                                   if box_square_inch.get()
                                   else conversion_mile()
                                   )

    button_clear = ttk.Button(frame, text="Borrar", command=lambda:clear_box(box_square_meter, box_square_hectometer, box_square_decameter, box_square_decimeter, box_square_centimeter, box_square_kilometer, box_square_milimeter, box_square_yard, box_square_feet, box_square_inch, box_square_mile)) # noqa
    button_clear.place(x=100, y=350)

    button_conversion.place(x=20, y=350)
    return frame
