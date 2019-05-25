
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import ttk
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

#Creando dimensiones de la ventana
root = Tkinter.Tk()
root.title("Numerico xd")
root.geometry("800x400")

def calcular():
	#Creaccion de la imagen con los resultados
	plt.plot([4,9],[8,18], c='red')

	plt.savefig("graf1.jpg")

	#Seccion de la imagen y resultado
	image = Image.open("graf1.jpg")
	image = image.resize((300, 250), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)

	imagen.configure(image=photo)
	imagen.image = photo

	#Borrando rastro e.e
	os.system("rm graf1.jpg")

#Ingreso de valores

Tkinter.Label(root, text="-----------------Titulo perron-----------------").place(x=75, y=20)

#P1

Tkinter.Label(root, text="P1 = ( ").place(x=25, y=50)
t1 = Tkinter.Entry(root, width=2)
t1.place(x=70, y=50)

Tkinter.Label(root, text=",").place(x=95, y=50)

cb1 = Tkinter.Entry(root, width=2)
cb1.place(x=105, y=50)

Tkinter.Label(root, text=")").place(x=130, y=50)

#P2

Tkinter.Label(root, text="P2 = ( ").place(x=25, y=80)
t1 = Tkinter.Entry(root, width=2)
t1.place(x=70, y=80)

Tkinter.Label(root, text=",").place(x=95, y=80)

cb1 = Tkinter.Entry(root, width=2)
cb1.place(x=105, y=80)

Tkinter.Label(root, text=")").place(x=130, y=80)

#P3

Tkinter.Label(root, text="P3 = ( ").place(x=25, y=110)
t1 = Tkinter.Entry(root, width=2)
t1.place(x=70, y=110)

Tkinter.Label(root, text=",").place(x=95, y=110)

cb1 = Tkinter.Entry(root, width=2)
cb1.place(x=105, y=110)

Tkinter.Label(root, text=")").place(x=130, y=110)

#P4

Tkinter.Label(root, text="P4 = ( ").place(x=25, y=140)
t1 = Tkinter.Entry(root, width=2)
t1.place(x=70, y=140)

Tkinter.Label(root, text=",").place(x=95, y=140)

cb1 = Tkinter.Entry(root, width=2)
cb1.place(x=105, y=140)

Tkinter.Label(root, text=")").place(x=130, y=140)

#P5

Tkinter.Label(root, text="P5 = ( ").place(x=25, y=170)
t1 = Tkinter.Entry(root, width=2)
t1.place(x=70, y=170)

Tkinter.Label(root, text=",").place(x=95, y=170)

cb1 = Tkinter.Entry(root, width=2)
cb1.place(x=105, y=170)

Tkinter.Label(root, text=")").place(x=130, y=170)

#P6

Tkinter.Label(root, text="P6 = ( ").place(x=25, y=200)
t1 = Tkinter.Entry(root, width=2)
t1.place(x=70, y=200)

Tkinter.Label(root, text=",").place(x=95, y=200)

cb1 = Tkinter.Entry(root, width=2)
cb1.place(x=105, y=200)

Tkinter.Label(root, text=")").place(x=130, y=200)

#Metodos
Tkinter.Label(root, text="--------------Metodos posibles--------------").place(x=75, y=230)

metodos = ttk.Combobox(values = ["Metodo1","Metodo2","Metodo3","Metodo4"])
metodos.place(x=100, y=270)

#Boton de listo

boton1 = Tkinter.Button(root, text="Calcular", command=calcular)
boton1.place(x=150, y=320)

#Insetando la imagen
imagen = Tkinter.Label(root)
imagen.place(x=450,y=50)

#Loop infinito hasta cerrar la ventana
root.mainloop()