import tkinter
from tkinter import ttk
window = tkinter.Tk()
enter_name_label=ttk.Label(window,text = "enter your name :-")
enter_name_label.grid(row=0,column=1,sticky=ttk.W)
enter_name_label=ttk.Label(window,text = "enter your name :-").grid(row=0,column=2,sticky=ttk.W)
enter_name_label=ttk.Label(window,text = "enter your name :-").grid(row=0,column=3,sticky=ttk.W)
window.mainloop()