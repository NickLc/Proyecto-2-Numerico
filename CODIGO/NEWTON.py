import numpy as np
import matplotlib.pyplot as plt

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

#Cb = np.array([0,0.3,0.55,0.8,1.10,1.15],dtype=float).reshape(1,6)
#t = np.array([0,0.1,0.4,0.6,0.8,1.0],dtype=float).reshape(1,6)
y = np.array([0,0.3,0.55,0.8,1.10,1.15],dtype=float).reshape(1,6)
x = np.array([0,0.1,0.4,0.6,0.8,1.0],dtype=float).reshape(1,6)
#x_p = np.array([0,0.1,0.4,0.6,0.8,1.0],dtype=float).reshape(1,6)
Matriz = coef(x,y)[0,:]
print(Matriz)
print("************************************")

sol=(evaluation(Matriz,x,0.6))
sol2=(evaluation(Matriz,x,0.4))
print(sol)
print(sol2)

print("#####################################################3")
for test in x.T:
	print("agg")
	print(f"Testeando en {test} --> {evaluation(Matriz,x,test)}")
print("#####################################################3")
print(f"Para el problema , Pol(0.82) = {evaluation(Matriz,x,0.82)}")

print("#####################################################3")


x1 = np.linspace(0, 1, 200, endpoint=True)        
y1 = []
for e in x1:
	y1.append(evaluation(Matriz,x,e))

y1=np.array(y1)

plt.plot(x1, y1, '-')
plt.plot(x,y,'o')
plt.show()

