import tkinter as tk
from tkinter import *
import math

root = Tk()
root.title("PPK Technology Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""
trigo = 0

def show(value):
    global equation, trigo
    if value in ["sin", "cos", "tan"]:
        trigo = 1
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#3697f5", command=lambda: clear()).place(x=10, y=105)
Button(root, text="÷", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("÷")).place(x=150, y=105)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=105)
Button(root, text="×", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("×")).place(x=430, y=105)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=205)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=205)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=205)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=205)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=305)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=305)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=305)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=305)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=405)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=405)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=405)
Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=505)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=505)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#ffffff", bg="#fe9037", command=lambda: calculate()).place(x=430, y=410)

root.mainloop()
