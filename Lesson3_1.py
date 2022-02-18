#!usr/bin/python3.10
"""
課程練習
"""
#print(__name__)
import tkinter as tk

def createdWindow():
    window = tk.Tk()
    window.title("測試視窗")
    window.geometry("200x100+50+50")
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    createdWindow()