import tkinter as tk
from tkinter import ttk
from tkinter import font
import dataSource

class Window(tk.Tk):
    def __init__(self,cities):
        super().__init__()
        #title_Font = font.nametofont('TkCaptionFont')
        self.configure(background='white')
        title_Font = font.Font(family='Helvetica', size=20, weight='bold')
        titleLabel = ttk.Label(self, text="台灣即時PM2.5",font=title_Font,anchor=tk.CENTER)
        titleLabel.pack(fill=tk.X, pady=20)

        top_frame = tk.Frame(self)
        #左邊容器==================start
        left_label_frame = tk.LabelFrame(top_frame,text="左邊容器",background="red")
        # 左上邊容器==================start
        left_top_frame = tk.Frame(left_label_frame)
        cityLabel = ttk.Label(left_top_frame, text="城市:")
        cityLabel.pack(side=tk.LEFT,padx=(50,0))

        self.cityvar = tk.StringVar()
        city_combobox = ttk.Combobox(left_top_frame, textvariable=self.cityvar)
        city_combobox.pack()
        city_combobox['values'] = cities
        city_combobox.state(["readonly"])
        city_combobox.bind('<<ComboboxSelected>>', self.city_selected)
        left_top_frame.pack()
        # 左上邊容器=================end
        # button_frame============start
        def betterClick():
            print("better")
        button_frame = tk.Frame(left_label_frame)
        betterButton = tk.Button(button_frame,text="空氣較佳品質",command=betterClick)
        betterButton.pack(side=tk.LEFT)

        def normalClick():
            print("normal")
        normalButton = tk.Button(button_frame, text="空氣一般品質",command=normalClick)
        normalButton.pack(side=tk.LEFT)


        def badClick():
            print("bad")

        badButton = tk.Button(button_frame, text="空氣品質不佳",command=badClick)
        badButton.pack(side=tk.LEFT)
        button_frame.pack(pady=20)
        # button_frame============end
        left_label_frame.pack(side=tk.LEFT, anchor=tk.N)
        #左邊容器==================end

        #右邊容器==================start
        right_label_frame = tk.LabelFrame(top_frame, text="右邊容器",bg='blue')
        siteLabel = ttk.Label(right_label_frame, text="站點:")
        siteLabel.pack(side=tk.LEFT, padx=(50, 0), anchor=tk.N)

        self.choicesvar = tk.StringVar(value=[])
        site_listbox = tk.Listbox(right_label_frame, height=10, listvariable=self.choicesvar)
        site_listbox.pack(side=tk.LEFT,padx=(0,50),pady=(0,30))
        site_listbox.bind("<<ListboxSelect>>", self.site_selected)
        right_label_frame.pack(side=tk.RIGHT)
        # 右邊容器==================end
        top_frame.pack()

        # 下方容器===================start
        self.tree = ttk.Treeview(self, columns=('id', 'site', 'city', 'pm25', 'date', 'unit'), show='headings')
        self.tree.heading('id', text="編號")
        self.tree.heading('site', text="站點")
        self.tree.heading('city', text="城市")
        self.tree.heading('pm25', text="pm25")
        self.tree.heading('date', text="日期")
        self.tree.heading('unit', text="單位")
        self.tree.column('id', width=100)
        self.tree.column('site', width=100)
        self.tree.column('city', width=100)
        self.tree.column('pm25', width=100)
        self.tree.column('date', width=100)
        self.tree.column('unit', width=100)
        self.tree.pack(side=tk.TOP)
        # 下方容器===================end

    def city_selected(self, event):
        for item in self.tree.get_children():
            self.tree.delete(item)
        data_list = dataSource.get_site_pm25(self.cityvar.get())
        self.choicesvar.set(data_list)

    #listboxbind事件
    def site_selected(self,event):
        selectedIndex = event.widget.curselection()
        if not selectedIndex:
            return
        site = event.widget.get(selectedIndex)
        #for item in self.tree.get_children():
        #    self.tree.delete(item)
        siteInfo = dataSource.get_site_info(site)
        self.tree.insert('',tk.END,values=list(siteInfo.values()))


if __name__ == "__main__":
    dataSource.download_save_to_DataBase()
    city_name_list = dataSource.get_city_name()
    window = Window(city_name_list)
    window.title("PM2.5")
    window.mainloop()