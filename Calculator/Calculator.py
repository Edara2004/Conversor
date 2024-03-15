from tkinter import ttk, Label, Frame, Button, Entry, StringVar, Grid # noqa


def Calculator_general(ventana):

    frame = Frame(ventana)

    def button_press(char):
        global expression
        expression = expression + str(char)
        display_var.set(expression)


    def button_equal():

        global expression
        try:
            result = eval(expression)
            expression = str(result)
            display_var.set(expression)
        
        except:
            display_var.set("Error")


    def button_clear():
        global expression
        expression = ""
        display_var.set("")

    expression = ""

    display_var = StringVar()
    display_label = Label(frame, textvariable=display_var, font=("Areal"), anchor="e", bg="white", padx= 10, pady= 10)
    display_label.grid(row= 0, columnspan= 4)

    #Create a button for numbers a operations

    button_list = [
        "7", "8", "9", "/"
        "4", "5", "6", "X"
        "3", "2", "1", "+"
        "0", ".", "=", "-"
    ]

    row = 1
    col = 0
    for button_text in button_list:
        button = Button(frame, text=button_text, font=("Arial", 15), padx= 5, pady= 5, command=lambda char= button_text: button_press(char))
        button.grid(row= row, column= col)
        col + 1
        if col > 3:
            col = 0
            row += 1

    #Create a clear button

    clear_button = Button(frame, text="C", font=("Arial", 15), padx= 5, pady= 5, command= button_clear)
    #widget_calculadora = ttk.Entry(frame)
    #widget_calculadora.place(x= 10, y= 5, width= 380, height= 80)

    return frame
