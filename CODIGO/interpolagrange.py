
# t es el valor que queremos evaluar en el polinomio
def interpol_Lagrange(x0, x1, x2, y0, y1, y2, t):
    p = y0*(t-x1)*(t-x2)/((x0-x1)*(x0-x2)) + y1*(t-x0)*(t-x2)/((x1-x0)*(x1-x2)) + y2*(t-x1)*(t-x0)/((x2-x1)*(x2-x0)) 
    
    print(p)
    
    
interpol_Lagrange(1, 4, 6, 1.5709, 1.5727, 1.5751, 3.5)    
#f(xi)=yi
#quiero aproximar t
