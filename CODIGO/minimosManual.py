import numpy as np
import matplotlib.pyplot as plt
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
    """
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
        a - Coeficientes del polinomio obtimo """
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

x = np.array([0.,2.,3.,6.,7.])
y= np.array([0.12, 0.154, 0.17, 0.225, 0.26])

x = np.array([0.00, 0.10, 0.40, 0.60, 0.80, 1.00])
y = np.array([0.00, 0.30, 0.55, 0.80, 1.10, 1.15])
a = min_Cuadratico(x,y,2, graphic='True')
print(a)
