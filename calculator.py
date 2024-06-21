import tkinter as tk

calculation = ""

# Function to update the expression on the screen
def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    input_field.delete(0.0, tk.END)
    input_field.insert(tk.END, calculation)

# Function to evaluate the calc
def evaluate():
    try:
        global calculation
        result = str(eval(calculation))
        calculation = result
        input_field.delete(0.0, tk.END)
        input_field.insert(tk.END, result)
    except:
        input_field.delete(0.0, tk.END)
        input_field.insert(tk.END, "Error")

# Function to clear the display
def clear():
    global calculation
    calculation = ""
    input_field.delete(0.0, tk.END)
    
    
root = tk.Tk()
root.title("Calculator")
root.geometry("300x320")

input_field = tk.Text(root, height=2, width=16, font=("Arial",24))
input_field.grid(columnspan=5)

# Defining colors
root.configure(bg="#F5F5F5")
number_color = "#FFFFFF"
operator_color = "#FFB84D"
clear_color = "#FF6347"
evaluate_color = "#3CB371"

# Creating buttons
button_7 = tk.Button(root, text="7", command=lambda: add_calculation(7), width=5, font=("Arial",14),bg= number_color)
button_7.grid(row=2, column=1)
button_8 = tk.Button(root, text="8", command=lambda: add_calculation(8), width=5, font=("Arial",14),bg=number_color)
button_8.grid(row=2, column=2)
button_9 = tk.Button(root, text="9", command=lambda: add_calculation(9), width=5, font=("Arial",14),bg=number_color)
button_9.grid(row=2, column=3)
button_div = tk.Button(root, text="/", command=lambda: add_calculation("/"), width=5, font=("Arial",14),bg=operator_color)
button_div.grid(row=2, column=4)

button_4 = tk.Button(root, text="4", command=lambda: add_calculation(4), width=5, font=("Arial",14),bg=number_color)
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text="5", command=lambda: add_calculation(5), width=5, font=("Arial",14),bg=number_color)
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text="6", command=lambda: add_calculation(6), width=5, font=("Arial",14),bg=number_color)
button_6.grid(row=3, column=3)
button_mul = tk.Button(root, text="*", command=lambda: add_calculation("*"), width=5, font=("Arial",14),bg=operator_color)
button_mul.grid(row=3, column=4)

button_1 = tk.Button(root, text="1", command=lambda: add_calculation(1), width=5, font=("Arial",14),bg=number_color)
button_1.grid(row=4, column=1)
button_2 = tk.Button(root, text="2", command=lambda: add_calculation(2), width=5, font=("Arial",14),bg=number_color)
button_2.grid(row=4, column=2)
button_3 = tk.Button(root, text="3", command=lambda: add_calculation(3), width=5, font=("Arial",14),bg=number_color)
button_3.grid(row=4, column=3)
button_sub = tk.Button(root, text="-", command=lambda: add_calculation("-"), width=5, font=("Arial",14),bg=operator_color)
button_sub.grid(row=4, column=4)

button_0 = tk.Button(root, text="0", command=lambda: add_calculation(0), width=5, font=("Arial",14),bg=number_color)
button_0.grid(row=5, column=1)
button_dot = tk.Button(root, text=".", command=lambda: add_calculation("."), width=5, font=("Arial",14),bg=number_color)
button_dot.grid(row=5, column=2)
button_add = tk.Button(root, text="+", command=lambda: add_calculation("+"), width=5, font=("Arial",14),bg=operator_color)
button_add.grid(row=5, column=4)

evaluate = tk.Button(root, text="=", command=evaluate, width=5, font=("Arial",14),bg=evaluate_color)
evaluate.grid(row=5, column=3)

clear = tk.Button(root, text="C", command=clear, width=11, font=("Arial",14),bg=clear_color)
clear.grid(row=6, columnspan=5)


root.mainloop()