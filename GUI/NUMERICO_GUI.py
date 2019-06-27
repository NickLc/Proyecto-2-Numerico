# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk 
import numpy as np
import os
from tools import INT_Lagrange,coef,evaluation


def convertir(cadena):
    tmp=cadena.split(",")
    tmp=map(float,tmp)
    return list(map(float,tmp))


class Aplicacion:
    def __init__(self):
        self.archi1=None
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.label1=tk.Label(text="Concentraciones:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=25, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="Tiempos:")
        self.label2.grid(column=0, row=1)
        self.label3=tk.Label(text="GRÁFICA:")
        self.label3.grid(column=2, row=0)
        self.canvas1=tk.Canvas(self.ventana1, width=700, height=500, background="white")
        self.canvas1.grid(column=2, row=1,rowspan=2)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=25, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.radio1=ttk.Radiobutton(self.ventana1,text="LAGRANGE", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=2)
        self.radio2=ttk.Radiobutton(self.ventana1,text="NEWTON", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=3)
        self.radio3=ttk.Radiobutton(self.ventana1,text="MINIMOS CUADRADOS", variable=self.seleccion, value=3)
        self.radio3.grid(column=0, row=4)
        self.boton1=ttk.Button(self.ventana1, text="CALCULAR", command=self.ingresar)
        self.boton1.grid(column=1, row=5)
        self.ventana1.mainloop()

    def ingresar(self):
        x=(convertir(self.dato1.get()))
        y=(convertir(self.dato2.get()))


        if self.seleccion.get()==1:   #LAGRANGE
            pol = INT_Lagrange(x,y,True)    
            x1 = np.linspace(0, 6, 400 , endpoint=True)
            y1 = pol(x1,True)
            plt.plot(x1, y1, '-')
            plt.plot(x,y,'o')
            plt.savefig('grafica.png')
            plt.close("all")
            self.archi1=tk.PhotoImage(file='grafica.png')
            self.canvas1.create_image(0,0, image=self.archi1, anchor="nw")
        if self.seleccion.get()==2:   #NEWTON
            size =len(x)
            x=np.array(x,dtype=float).reshape(1,size)
            y=np.array(y,dtype=float).reshape(1,size)
            Matriz = coef(x,y)[0,:]
            x1 = np.linspace(0, 6, 400, endpoint=True)
            y1 = []
            for e in x1:
                y1.append(evaluation(Matriz,x,e))
            y1=np.array(y1)

            plt.plot(x1, y1, '-')
            plt.plot(x,y,'o')
            plt.savefig('grafica.png')
            plt.close("all")
            self.archi1=tk.PhotoImage(file='grafica.png')
            self.canvas1.create_image(0,0, image=self.archi1, anchor="nw")

        #print(x)
        #print(y)
        #plt.plot(x, y, 'o')
        #plt.savefig('grafica.png')
        #plt.close("all")
        #self.archi1=tk.PhotoImage(file='grafica.png')
        #print("GRAFICANDO")
        #self.canvas1.create_image(0,0, image=self.archi1, anchor="nw")

aplicacion1=Aplicacion() 

