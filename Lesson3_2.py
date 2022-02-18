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

        topFrame = ttk.LabelFrame(self, text="上方選項")
        labelFont = tkFont.Font(family="Arial", size=30)
        label = ttk.Label(topFrame, text='Hello World', font=labelFont, anchor=tk.CENTER)
        label.pack(padx=20, pady=10)
        leftbutton = ttk.Button(topFrame, text="確定",command=self.topLeftClick)
        leftbutton.pack(side=tk.LEFT, pady=10, ipady=10, padx=20)
        rightbutton = ttk.Button(topFrame, text="取消",command=self.topRightClick)
        rightbutton.pack(side=tk.RIGHT, pady=10, ipady=10, padx=20)
        topFrame.pack(padx=10, pady=10)

        buttonFrame = ttk.LabelFrame(self, text="下方選項")
        labelFont = tkFont.Font(family="Arial", size=30)
        label1 = ttk.Label(buttonFrame, text='Hello World', font=labelFont, anchor=tk.CENTER)
        label1.pack(padx=20, pady=10)
        leftbutton1 = ttk.Button(buttonFrame, text="確定")
        leftbutton1.pack(side=tk.LEFT, pady=10, ipady=10, padx=20)
        rightbutton1 = ttk.Button(buttonFrame, text="取消")
        rightbutton1.pack(side=tk.RIGHT, pady=10, ipady=10, padx=20)
        buttonFrame.pack(padx=10, pady=10)

    def topLeftClick(self):
        print("123")

    def topRightClick(self):
        print("456")

if __name__ == "__main__":
    window = Window()
    window.title("測試視窗1")
    window.geometry('600x300')
    window.config(bg="blue")
    window.mainloop()