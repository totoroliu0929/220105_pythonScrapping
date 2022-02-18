#!usr/bin/python3.10
"""
課程練習
"""
#print(__name__)
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        labelFont = tkFont.Font(family="Lucida Grande", size=30)
        label = ttk.Label(self, text='Hello World', font=labelFont)
        label.pack()

if __name__ == "__main__":
    window = Window()
    window.title("測試視窗1")
    window.geometry('600x300')
    window.config(bg="blue")
    window.mainloop()