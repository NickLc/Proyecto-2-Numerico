import numpy as np
import matplotlib.pyplot as plt
from time import time
import math
"""
def polinomi(a, x):
    total = 0
    for i in range(len(a)):
        total += a[i] * x**i

    return total

def pol_vect(a, x):
    p = np.zeros(len(x))
    for i in range(len(x)):
        p[i] = polinomi(a,x[i])

    return p

def min_Cuadratico(x, y, n=2, graphic='False'):
    
        Get Matrix Minimo
        -------------------
        Para obtener los "n+1" coeficientes del polinomio óptimo de grado "n" que
        pasa entre los m = len(x) parejas de puntos, para ello se resuelve el siguiente
        sistema: M * a = b donde \n
        M es la Matrix M_i,j = Sum(x^(i+j)),\n
        a es [a_1, a_2,....., a_n], a_i es el coeficiente del polinomio en x_n,\n
        b es [b_1, b_2,....., b_n], b_i es la Sum(y * x^i) desde i = 1 ... n
        Argumentos
        -----------
        x - Puntos a evualuar
        y - Puntos evaluados experimentalmente
        n - grado del polinomio optimo
        Retorna
        --------
        a - Coeficientes del polinomio obtimo 
    n = n+1
    M = np.zeros(n**2).reshape(n,n)
    b = np.zeros(n).reshape(n,1)

    for i in range(n):
        for j in range(n):
            M[i,j] = np.sum(x**(i+j))
        b[i] = np.sum(x**i * y)

    a = np.linalg.solve(M,b)

    if graphic:
        lin_a = -0.5 ; lin_b = 1.5
        l = np.linspace(lin_a, lin_b, 50)              # Vector de 50 elementos equiespaciados en (a,b)

        plt.plot(x, y,'g^', label='f(x)=y')

        plt.plot(l, polinomi(a,l),'y-',label='p(x)=x')
        plt.legend(loc='best')
        plt.show()

    return a

"""



def Ln_i(n,i,x_vector,x):
    p1 = 1
    p2 = 1

    for j in range(n):
        if i != j:
            p1 *= (x - x_vector[j])
            p2 *= (x_vector[i]-x_vector[j])
    return p1/p2

def INT_Lagrange(x_vector, y_vector, verbose):
    #=========================================
    if verbose:
        print("=========================================")
        print("METODO DE LAGRANGE")
        print("Este metodo genera una funcion P_n(x)\nrepresentando al polinomio interpolado por Lagrange")
        print("Se usara los datos de \'x\':", x_vector)
        print("Se usara los datos de \'y\':", y_vector)
        print("=========================================")
    #=========================================

    def P_n_eq(x, verbose):
        #=========================================
        if verbose:
            print("-----------------------------------")
            print("Evaluando x = {}".format(x))
        #=========================================
        n = len(x_vector)
        acc = 0
        for i in range(len(y_vector)):
            #=========================================
            if verbose:
                print("L_{},{}:{}".format(n, i, Ln_i(n, i, x_vector, x)))
            #=========================================
            acc += y_vector[i]*Ln_i(n, i, x_vector, x)

        #=========================================
        if verbose:
            print("Finalmente, P_{}({}):{}".format(n, x, acc))
            print("-----------------------------------")
        #=========================================
        return acc
    return P_n_eq




def coef(x_0,y_0):

    x = np.copy(x_0)
    y = np.copy(y_0)
    n = np.shape(x)[1]
    a = np.zeros(n*n).reshape(n,n)
    print(n)
    for i in range(n):
        a[i,0] = y[0,i]

    for j in range(1,n):
        for i in range(0,n-j):
            a[i,j] = (a[i+1,j-1]-a[i,j-1])/(x[0,i+j] - x[0,i])

    return a


def evaluation(a_0,x_0,pto):
    a=np.copy(a_0)
    x=np.copy(x_0)
    #y=np.copy(y_0)
    n = len(a)
    #print(f"Valor de n es {n}")
    #print(f"x es {x}")

    eval=0
    for i in range(0,n):
        #print(f"-------------- Iteracion i = {i} --------------")
        temp = 1
        for j in range(0,i):
            #print(f"i={i},j={j}")
            #print(f"x[0,{j}] = {x[0,j]}]")
            #print(f"Calculando temp= {temp*(pto-x[0,j])}")
            temp = temp*(pto-x[0,j])

        #print(f"a[{i}]={a[i]}")
        temp = temp*a[i]
        #print(f"##### Fuera de J,Calculando temp= {temp}")
        eval=eval+temp
        #print("##########################################")
        #print(f"eval = {eval}")
        #print("##########################################")


    return eval



