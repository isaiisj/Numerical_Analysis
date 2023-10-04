#Método Krylov
import metGaussJordan as gs
import numpy as np
import metLin as lin 
from math import sqrt
A = np.matrix([[1, 2, 4], [7, 3, 1], [0, 1, 4]])
y = np.matrix([[1], [0], [0]])

print("A=\n", A)
print("y=\n", y)


def krylov(A, y):
	n = len(A[0:])
	cont = n - 1
	m = np.zeros((n, n))
	b = np.zeros((n, 1))
	Ak = A * y
	m[0:, cont:] = y
	while cont > 0:
		if (cont != 0):
			m[0:, 0:cont] = Ak
		print("A{0}=\n{1}".format(cont, Ak))
		print("m=\n", m)
		Ak = A * Ak
		cont -= 1
	return m, -Ak


m, Ak = krylov(A, y)
#print("b=\n",Ak)
b = gs.gaussJordan(m, Ak)
print(b)

b = [1, -8, 4, 17]
lin.Lin(b, .0001)

print("l1\=n", 7.009)


def raizg(a, b, c):
	disc = b * b - 4 * a * c
	if (disc < 0):
		disc = -disc
		r = sqrt(disc)
		x1 = complex(-b / (2 * a), r / (2 * a))
		x2 = complex(-b / (2 * a), -r / (2 * a))
	else:
		r = sqrt(disc)
		x1 = (-b - r) / (2 * a)
		x2 = (-b + r) / (2 * a)
	return x1, x2


x1, x2 = raizg(1, -0.9007, -2.395)

print("l2={0}, l3={1} ".format(x1, x2))
