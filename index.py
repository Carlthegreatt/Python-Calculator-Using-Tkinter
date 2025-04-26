from tkinter import *
import tkinter as tk
import back_end


def on_click(num):
    return display_widget.insert(END, num)


window = Tk()
window.geometry("400x600")
window.title("Simple Calculator")
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.config(bg="#2C3E50")

top = Frame(window, bg="#2C3E50")
top.pack(side="top", pady=5)


display_widget = Text(top, height=5, width=40)
display_widget.pack(pady=5)


buttons = Frame(window, bg="#2C3E50")
buttons.pack()

btn1 = Button(buttons, text="1", width=5, height=2, command=on_click)
btn1.grid(row=1, column=10, padx=5, pady=5)
btn2 = Button(buttons, text="2", width=5, height=2, command=on_click)
btn2.grid(row=1, column=11)
btn3 = Button(buttons, text="3", width=5, height=2, command=on_click)
btn3.grid(row=1, column=12, padx=5, pady=5)
btn4 = Button(buttons, text="4", width=5, height=2, command=on_click)
btn4.grid(row=2, column=10)
btn5 = Button(buttons, text="5", width=5, height=2, command=on_click)
btn5.grid(row=2, column=11, padx=5, pady=5)
btn2 = Button(buttons, text="6", width=5, height=2, command=on_click)
btn2.grid(row=2, column=12)
btn3 = Button(buttons, text="7", width=5, height=2, command=on_click)
btn3.grid(row=3, column=10, padx=5, pady=5)
btn4 = Button(buttons, text="8", width=5, height=2, command=on_click)
btn4.grid(row=3, column=11)
btn3 = Button(buttons, text="9", width=5, height=2, command=on_click)
btn3.grid(row=3, column=12, padx=5, pady=5)
btn4 = Button(buttons, text="0", width=5, height=2, command=on_click)
btn4.grid(row=4, column=11)
window.mainloop()
