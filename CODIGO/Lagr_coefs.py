import numpy as np
from scipy.interpolate import lagrange


def eval_poly(lst,x):

    result=0.0

    i=0

    while len(lst)>i:

      result=result+lst[i]*x**i

      i=i+1

    return result


Cb = np.array([0,0.3,0.55,0.8,1.10,1.15],dtype=float)
t = np.array([0,0.1,0.4,0.6,0.8,1],dtype=float)
poly = lagrange(t, Cb)

from numpy.polynomial.polynomial import Polynomial

lst=Polynomial(poly).coef
lst=lst[::-1]

print("COEFICIENTES:")
print(lst)

for x in t:
	print(f'poly({x}) = {eval_poly(lst,x)}')


