import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import calcular as cl
import checkdiametro as cd


# Funciones
def proceso():
    try:
        longitud = ent_lg.get()
        rb_traslape = Radiobtn1.get()
        rb_diametro = Radiobtn2.get()
        rb_diametro = cd.dato(rb_diametro)

        if longitud == '':
            tk.messagebox.showerror(title='ERROR!!!', message='Debe ingresar un numero.')
        else:
            resultado = cl.datos(float(longitud), rb_traslape, rb_diametro)
            texto.set(resultado)
    except ValueError:
        tk.messagebox.showerror(title='Error!!!', message='Ingrese un numero.')


# GUI
myColor = 'cornflowerblue'
myColor1 = 'red'
root = tk.Tk()
root.title('BARRA12')
root.geometry('250x250')
root.resizable(False, False)
root.config(bg=myColor)
root.iconbitmap('Degree.ico')
# root.overrideredirect(True)  # turns off title bar
# root.attributes('-type', 'splash')
# root.attributes('-topmost', True)  # encima de todas las ventanas
# root.attributes('-alpha', 0.5)  # convierte en transparente la ventana
# root.attributes("-fullscreen", True)  # ocupa toda la pantalla
# root.attributes('-zoomed', '1')  # NO FUNCIONA
# root.attributes("-toolwindow", 1)  # oculta maximizar y minimizar y el icono 0 y 1
# root.lift()
# root.lower()
# root.focus_force()

# UI options
paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Arial Black', 11), 'width': '10'}

# Estilo de Widgets
style = ttk.Style()
style.configure('S.Label', padding=(0, 5, 0, 5), foreground='black', background=myColor, font=('Helvetica', 11))

style.layout('E.TEntry', [('Entry.plain.field', {'children': [('Entry.background', {'children': [('Entry.padding', {'children': [('Entry.textarea', {'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})], 'border': '1', 'sticky': 'nswe'})])

style.configure('E.TEntry', foreground='black', background=myColor, fieldbackground='gainsboro')

style.configure('C.TButton', padding=(0, 5, 0, 5), relief='flat', overrelief='raised', background='blue', font=('Helvetica', 11))
style.configure('W.TRadiobutton', background=myColor, foreground='black')

# Constantes
numero = tk.StringVar()
texto = tk.StringVar()
Radiobtn1 = tk.IntVar()
Radiobtn2 = tk.IntVar()

# Widgets
lbl_lg = ttk.Label(root, text='Longitud:', style='S.Label')
lbl_lg.place(x=10, y=10)

ent_lg = ttk.Entry(root,  textvariable=numero, style='E.TEntry', **entry_font)
ent_lg.place(x=80, y=7, relwidth=0.6)
ent_lg.focus()

lbl_traslape = ttk.Label(root, text='Incluir traslape:', style='S.Label')
lbl_traslape.place(x=10, y=40)
rbNo = ttk.Radiobutton(root, text='NO', variable=Radiobtn1, style='W.TRadiobutton', value=0).place(x=110, y=40)
rbSi = ttk.Radiobutton(root, text='SI', variable=Radiobtn1, style='W.TRadiobutton', value=1).place(x=160, y=40)

lbl_diametro = ttk.Label(root, text='Diametro:', style='S.Label')
lbl_diametro.place(x=10, y=70)
rb8 = ttk.Radiobutton(root, text='8', variable=Radiobtn2, style='W.TRadiobutton', value=1).place(x=10, y=90)
rb12 = ttk.Radiobutton(root, text='12', variable=Radiobtn2, style='W.TRadiobutton', value=0).place(x=50, y=90)
rb14 = ttk.Radiobutton(root, text='14', variable=Radiobtn2, style='W.TRadiobutton', value=2).place(x=100, y=90)
rb16 = ttk.Radiobutton(root, text='16', variable=Radiobtn2, style='W.TRadiobutton', value=3).place(x=150, y=90)
rb18 = ttk.Radiobutton(root, text='18', variable=Radiobtn2, style='W.TRadiobutton', value=4).place(x=200, y=90)
rb20 = ttk.Radiobutton(root, text='20', variable=Radiobtn2, style='W.TRadiobutton', value=5).place(x=10, y=120)

btn_cal = ttk.Button(root, text='CALCULAR', style='C.TButton', command=proceso)
btn_cal.place(x=10, y=150, relx=0.25)

lbl_cal = ttk.Label(root, textvariable=texto, wraplength=230, style='S.Label')
lbl_cal.place(x=10, y=200)

root.mainloop()
