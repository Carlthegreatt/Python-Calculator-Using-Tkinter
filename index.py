from tkinter import *
import tkinter as tk
import back_end

stored_values = []
current_input = ""


def on_click(num):
    global current_input
    # Append the number to the current input string
    current_input += str(num)
    # Display the current input on the screen
    display_widget.delete(1.0, END)
    display_widget.insert(END, current_input)


def clear_input():
    global current_input
    current_input = ""
    display_widget.delete(1.0, END)


def add_to_stored_values():
    global current_input
    if current_input:  # Only append if current_input is not empty
        stored_values.append(int(current_input))  # Convert to integer before appending
        current_input = ""  # Reset current_input


def add():
    global stored_values, current_input
    # Add the last input to the stored values
    add_to_stored_values()
    if len(stored_values) >= 2:
        # Perform the addition
        result = sum(stored_values)
        # Display the result
        display_widget.delete(1.0, END)
        display_widget.insert(END, str(result))
        # Clear stored values
        stored_values.clear()
    else:
        # Error message if fewer than 2 values
        display_widget.delete(1.0, END)
        display_widget.insert(END, "Error: Two values required")
        stored_values.clear()


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

btn1 = Button(
    buttons, text="1", width=5, height=2, command=lambda: [on_click(1), calculate(1)]
)

for i, num in enumerate(range(1, 10), start=1):
    Button(
        buttons, text=str(num), width=5, height=2, command=lambda n=num: on_click(n)
    ).grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)
Button(buttons, text="0", width=5, height=2, command=lambda: on_click(0)).grid(
    row=3, column=1
)

Button(
    buttons,
    text="+",
    width=5,
    height=2,
    command=lambda: [add_to_stored_values(), on_click("+")],
).grid(row=4, column=0)
Button(buttons, text="=", width=5, height=2, command=add).grid(row=4, column=1)
Button(buttons, text="Del", width=5, height=2, command=clear_input).grid(
    row=4, column=2
)

window.mainloop()
