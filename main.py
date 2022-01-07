import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import proceso as pc


def calcular():
    # validacion en caso de que se ingrese valores erroneos
    try:
        longitud = ntr_long.get()
        if longitud == '':
            tk.messagebox.showerror(title='ERROR!!!', message='Debe ingresar un numero.')
        else:
            barra = pc.data(float(longitud))
            newtxt.set(barra)
    except ValueError:
        tk.messagebox.showerror(title='ERROR!!!', message='Debe ingresar un numero y no una cadena de texto.')


root = tk.Tk()
root.title('BARRA12')
root.geometry('350x200+350+200')
root.resizable(False, False)

# Estilo de los widgets
style = ttk.Style()
style.configure("TLabel", foreground="black", font=('Helvetica', 11))
style.configure("TButton", padding=(0, 5, 0, 5), relief="flat", background='blue', font=('Helvetica', 11))

# UI options extra
paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Arial', 11)}

# constantes
number = tk.StringVar()
newtxt = tk.StringVar()

# widgets
ttk.Label(root, text='Longitud:', style='BW.TLabel').grid(row=0, column=0, sticky=tk.W, **paddings)

ntr_long = ttk.Entry(root, textvariable=number, **entry_font).grid(row=0, column=1, sticky=tk.E, **paddings)

btncal = ttk.Button(root, text='CALCULAR', style='TButton', command=calcular).grid(row=1, column=0, sticky=tk.E, **paddings)

ttk.Label(root, textvariable=newtxt, style='BW.TLabel').grid(row=3, column=0, **paddings)


root.mainloop()
