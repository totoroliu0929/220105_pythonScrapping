#!usr/bin/python3.10
"""
課程練習
"""
#print(__name__)
import tkinter as tk
from tkinter import ttk

def createdWindow():
    window = tk.Tk()
    window.title("測試視窗")
    window.geometry('600x300+200+200')
    window.resizable(False, False)
    label = ttk.Label(window, text="Hello World")
    label.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
    window.mainloop()

if __name__ == "__main__":
    createdWindow()