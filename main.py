import tkinter as tk

calcul = ""

def add_to_calc(symbol):
    global calcul
    calcul += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0 , calcul)

def eval_calc():
    global calcul
    try:
        result = str(eval(calcul))
        calcul = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")
        pass


def clear_field():
    global calcul
    calcul = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("480x640")


text_result = tk.Text(root, height = 2, width = 16, font = ("Arial", 24))
text_result.grid(columnspan=5)

no1 = tk.Button(root, text = "1", command = lambda:add_to_calc(1), width = 5, font=("Arial",14))
no1.grid(row = 2, column = 1)

no2 = tk.Button(root, text = "2", command = lambda:add_to_calc(2), width = 5, font=("Arial",14))
no2.grid(row = 2, column = 2)
no3 = tk.Button(root, text = "3", command = lambda:add_to_calc(3), width = 5, font=("Arial",14))
no3.grid(row = 2, column = 3)
no4 = tk.Button(root, text = "4", command = lambda:add_to_calc(4), width = 5, font=("Arial",14))
no4.grid(row = 3, column = 1)
no5 = tk.Button(root, text = "5", command = lambda:add_to_calc(5), width = 5, font=("Arial",14))
no5.grid(row = 3, column = 2)
no6 = tk.Button(root, text = "6", command = lambda:add_to_calc(6), width = 5, font=("Arial",14))
no6.grid(row = 3, column = 3)
no7 = tk.Button(root, text = "7", command = lambda:add_to_calc(7), width = 5, font=("Arial",14))
no7.grid(row = 4, column = 1)
no8 = tk.Button(root, text = "8", command = lambda:add_to_calc(8), width = 5, font=("Arial",14))
no8.grid(row = 4, column = 2)
no9 = tk.Button(root, text = "9", command = lambda:add_to_calc(9), width = 5, font=("Arial",14))
no9.grid(row = 4, column = 3)

no0 = tk.Button(root, text = "0", command = lambda:add_to_calc(0), width = 5, font=("Arial",14))
no0.grid(row = 5, column = 2)

plus = tk.Button(root, text = "+", command = lambda:add_to_calc("+"), width = 5, font=("Arial",14))
plus.grid(row = 2, column = 4)

minus = tk.Button(root, text = "-", command = lambda:add_to_calc("-"), width = 5, font=("Arial",14))
minus.grid(row = 3, column = 4)

mult = tk.Button(root, text = "*", command = lambda:add_to_calc("*"), width = 5, font=("Arial",14))
mult.grid(row = 4, column = 4)

divide = tk.Button(root, text = "/", command = lambda:add_to_calc("/"), width = 5, font=("Arial",14))
divide.grid(row = 5, column = 4)

open_bracket = tk.Button(root, text = "(", command = lambda:add_to_calc("("), width = 5, font=("Arial",14))
open_bracket.grid(row = 5, column = 1)

close_bracket = tk.Button(root, text = ")", command = lambda:add_to_calc(")"), width = 5, font=("Arial",14))
close_bracket.grid(row = 5, column = 3)


button_clear = tk.Button(root, text = "C", command = lambda:clear_field(), width = 11, font=("Arial",14))
button_clear.grid(row = 6, column = 1, columnspan = 2)

button_equals = tk.Button(root, text = "=", command = eval_calc, width = 11, font=("Arial",14))
button_equals.grid(row = 6, column = 3, columnspan = 2)

root.mainloop()

