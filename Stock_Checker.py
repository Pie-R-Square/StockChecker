from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

root = Tk()
root.title("Stock Checker")


w = 550
h = 700

ws = root.winfo_screenwidth() #screen width
hs = root.winfo_screenheight() #screen height


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

F1 = Frame(root)
F1.pack()
F2 = LabelFrame(F1, padx=25, pady=20)
F2.pack(pady=20)
F3 = LabelFrame(F1, padx=25, pady=20)
F3.pack(pady=20)
F4 = LabelFrame(F1, padx=25, pady=20)
F4.pack(pady=20)
F5 = LabelFrame(F1, padx=150, pady=20)
F5.pack(pady=20)

##### Stock oveerview #####
header = ["Original", "Seaweed", "Tom Yum", "Herbal"]
text1 = ttk.Label(F2, text="INPUT").pack()
input = ttk.Treeview(F2, columns=header, show='headings', height=1)
input.pack(pady=15)
for h in header:
	input.heading(h, text=h)

text2 = ttk.Label(F3, text="OUTPUT").pack()
output = ttk.Treeview(F3, columns=header, show='headings',height=1)
output.pack(pady=15)
for h in header:
	output.heading(h, text=h)

text3 = ttk.Label(F4, text="BALANCE").pack()
balance = ttk.Treeview(F4, columns=header, show='headings',height=1)
balance.pack(pady=15)
for h in header:
	balance.heading(h, text=h)

headerwidth = [80, 80, 80, 80]
for h, w in zip(header, headerwidth):
	input.column(h, width=w)
	output.column(h, width=w)
	balance.column(h, width=w)
##### End #####

##### Button #####
B_input = ttk.Button(F5, text="INPUT")
B_input.place(x=-115)
B_output = ttk.Button(F5, text="OUTPUT")
B_output.pack()
B_view = ttk.Button(F5, text="LOG")
B_view.place(x=115)

##### End #####

root.mainloop()