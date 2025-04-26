from tkinter import *
import index

tk = Tk()


def on_click():
    index.display_widget.insert(END, "Hello")
