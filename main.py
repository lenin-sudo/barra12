import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

from fire.console.console_attr import GetCharacterDisplayWidth

import calcular as cl


# Funciones
def proceso():
    try:
        longitud = ent_lg.get()

        if longitud == '':
            tk.messagebox.showerror(title='ERROR!!!', message='Debe ingresar un numero.')
        else:
            resultado = cl.datos(float(longitud))
            print(resultado, type(resultado))
            texto.set(resultado)
    except ValueError:
        tk.messagebox.showerror(title='Error!!!', message='Ingrese un numero.')


# GUI
root = tk.Tk()
root.title('BARRA12')
root.geometry('250x150')
root.resizable(False, False)

# UI options
paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Arial', 11), 'width': '10'}

# Estilo de Widgets
style = ttk.Style()
style.configure('S.Label', padding=(0, 5, 0, 5), foreground='black', font=('Helvetica', 11))
style.configure('C.TButton', padding=(0, 5, 0, 5), relief='flat', background='blue', font=('Helvetica', 11))

# Constantes
numero = tk.StringVar()
texto = tk.StringVar()

lbl_lg = ttk.Label(root, text='Longitud:', style='S.Label')
lbl_lg.place(x=10, y=10)

ent_lg = ttk.Entry(root,  textvariable=numero, **entry_font)
ent_lg.place(x=80, y=7, relwidth=0.6)
ent_lg.focus()

btn_cal = ttk.Button(root, text='CALCULAR', style='C.TButton', command=proceso)
btn_cal.place(x=10, y=40, relx=0.25)

lbl_cal = ttk.Label(root, textvariable=texto, style='S.Label')
lbl_cal.place(x=10, rely=0.6)

root.mainloop()
