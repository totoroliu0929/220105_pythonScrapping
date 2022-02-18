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
        label.pack(expand=True, fill=tk.X, anchor=tk.CENTER, padx=20)
        #label.pack()
        leftbutton = ttk.Button(self, text="確定")
        leftbutton.pack(side=tk.LEFT, pady=10, ipady=10, padx=20)
        rightbutton = ttk.Button(self, text="取消")
        rightbutton.pack(side=tk.RIGHT, pady=10, ipady=10, padx=20)

        buttonFrame = ttk.LabelFrame(self, text="下方選項")
        labelFont = tkFont.Font(family="Arial", size=30)
        label1 = ttk.Label(buttonFrame, text='Hello World', font=labelFont, anchor=tk.CENTER)
        label1.pack(padx=20, pady=10)
        leftbutton1 = ttk.Button(buttonFrame, text="確定")
        leftbutton1.pack(side=tk.LEFT, pady=10, ipady=10, padx=20)
        rightbutton1 = ttk.Button(buttonFrame, text="取消")
        rightbutton1.pack(side=tk.RIGHT, pady=10, ipady=10, padx=20)
        buttonFrame.pack(padx=10, pady=10)

if __name__ == "__main__":
    window = Window()
    window.title("測試視窗1")
    window.geometry('600x300')
    window.config(bg="blue")
    window.mainloop()