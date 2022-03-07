#!usr/bin/python3.10
"""
課程練習
"""
#print(__name__)
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import requests
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
        self.tree = ttk.Treeview(buttonFrame, columns=['site', 'county', 'pm25', 'date', 'unit'], show='headings')
        self.tree.column('site', width=100, anchor='center')
        self.tree.column('county', width=100, anchor='center')
        self.tree.column('pm25', width=100, anchor='center')
        self.tree.column('date', width=100, anchor='center')
        self.tree.column('unit', width=100, anchor='center')
        self.tree.heading('site', text='站點')
        self.tree.heading('county', text='城市')
        self.tree.heading('pm25', text='PM2.5')
        self.tree.heading('date', text='日期')
        self.tree.heading('unit', text='單位')
        self.tree.pack()
        buttonFrame.pack(padx=10, pady=10)

    def topLeftClick(self):
        urlpath = "https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json"
        response = requests.get(urlpath)
        if response.status_code == 200:
            dataList = response.json()["records"]
            for item in dataList:
                print(item)
                self.tree.insert('', 'end', values=list(item.values()))

            #print(dataList)

    def topRightClick(self):
        print("456")

if __name__ == "__main__":
    window = Window()
    window.title("測試視窗1")
    window.geometry('600x300')
    window.config(bg="blue")
    window.mainloop()