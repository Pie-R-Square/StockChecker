from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

root = Tk()
root.title("Stock Checker")


w = 600
h = 650

ws = root.winfo_screenwidth() #screen width
hs = root.winfo_screenheight() #screen height


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

F1 = LabelFrame(root, text="Input", font=16, padx=20, pady=20)
F1.pack(pady=30)
F2 = LabelFrame(root, text="Output", font=16, padx=20, pady=20)
F2.pack()
F3 = LabelFrame(root, text="Output", font=16, padx=20, pady=20)
F3.pack(pady=30)

##### Stock oveerview #####
header = ["Original", "Seaweed", "Tom Yum", "Herbal"]
input = ttk.Treeview(F1, columns=header, show='headings', height=1)
input.pack()
for h in header:
	input.heading(h, text=h)

output = ttk.Treeview(F2, columns=header, show='headings',height=1)
output.pack()
for h in header:
	output.heading(h, text=h)

balance = ttk.Treeview(F3, columns=header, show='headings',height=1)
balance.pack()
for h in header:
	balance.heading(h, text=h)

headerwidth = [80, 80, 80, 80]
for h, w in zip(header, headerwidth):
	input.column(h, width=w)
	output.column(h, width=w)
	balance.column(h, width=w)
##### End #####

root.mainloop()