import tkinter as tk
from tkinter import ttk
from tkinter import *

# GUI
root = tk.Tk()
root.title('BARRA12')
# root.geometry('300x150')
root.resizable(False, False)

# UI options
paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Arial Black', 11), 'width': '10'}

# Estilo de Widgets
style = ttk.Style()
style.configure('S.Label', foreground='black', font=('Helvetica', 11))
style.configure('C.TButton', padding=(0, 5, 0, 5), relief='flat', background='blue', font=('Helvetica', 11))

# Constantes
numero = tk.StringVar()
texto = tk.StringVar()

lbl_lg = ttk.Label(root, text='Longitud:', style='S.Label')
lbl_lg.grid(row=0, column=0, sticky='w', **paddings)

ent_lg = ttk.Entry(root,  textvariable=numero, **entry_font)
ent_lg.grid(row=0, column=2, sticky='e', **paddings)

btn_cal = ttk.Button(root, text='CALCULAR', style='C.TButton')
btn_cal.grid(row=1, column=0, columnspan=2, **paddings)

lbl_cal = ttk.Label(root, textvariable=texto, style='S.Label')
lbl_cal.grid(row=2, column=0, **paddings)

root.mainloop()
