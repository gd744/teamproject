"""

Our program will be a simple calculator program. This program will have three functions and a graphical user interface(GUI).
The first funtion will be where the user chooses a series of numbers to be calculated.
The second function will be where the calcuations will take place and express an error message if the calculation cannot happen, such as dividing by zero.
The third function will be a clear function, resetting all user input and being able to start over.
The GUI for the program will consist of the numbers 0-9, arithmetic operators; addition, subtraction, multiplication, and division, an equal sign, and the clear button.
Each button in the GUI will have a specific foreground/background color and box size that will house the number/operator.
The GUI will also be named "Calculator".

"""




"""
This is for the calculator only, not including the GUI.

# Funtion 1: Choose numbers.
    Set global expression.
    Set expression += str(num)

# Function 2: Pressing equal.
    try:
        Set global expression.
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("error") # This is when the calculation cannot happen.
        expression = ""

# Function 3: Clear
    Set global expression.
    expression = ""
    equation.set("")

"""




"""

This is for the GUI

Configure background/foreground color, title of GUI, dimension of GUI.

if __name__ == "__main__":
    gui.configure(background = "black")
    gui.title("Calculator")
    gui.geometry("300x175")
    equation = StringVar()
    expression_field = Entry(gui, textvariable = equation)
    expression_field.grid(columnspan = 4, ipadx = 88)

    Set the same parameters for each button using the following code, modifying as needed to accomodate each number and operator.

    button1 = Button(gui, text = ' 1 ', fg = 'black', bg = 'white',
        command = lambda: press(1), height = 1, width = 7)
    button1.grid(row = 2, column = 0)

gui.mainloop()

"""
