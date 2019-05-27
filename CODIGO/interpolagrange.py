# Ln_i: Retorna el coeficiente de Lagrange L_ni
def Ln_i(n, i, x_vector, x):
	p1 = 1
	p2 = 1

	for j in range(0, n):
		if i != j:
			p1 *= (x - x_vector[j])
			p2 *= (x_vector[i] - x_vector[j])
	
	return p1/p2

# INT_Lagrange: Retorna el polinomio generado P_n_eq, listo para evaluar cualquier
# x y tomar el valor de la curva interpolada en cualquier punto
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

	def P_n_eq(x, verbose=False):
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
		return acc
	return P_n_eq

x_vector=[1,2,3,4,5,6,7,8]
y_vector=[1,4,10,18,26,38,52,69]
poly=INT_Lagrange(x_vector, y_vector, verbose=True)
for val in x_vector:
    print(poly(val,True))

