import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

root =tk.Tk()
root.geometry('250x200+250+200')

Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

lbl1 = ttk.Label(root, text='Longitud:').grid(row=0, column=0)
ntr_long = ttk.Entry(root)
ntr_long.grid(row=0, column=1)
btncal = ttk.Button(root, text='CALCULAR').grid(row=1, column=0)
lbl1 = ttk.Label(root, text='').grid(row=2, column=0)



root.mainloop()