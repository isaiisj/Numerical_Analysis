#Interpolación por diferencias Finitas Progresivas

import numpy as np
import sympy as sym
#import matplotlib.pyplot as plt

xi=np.array([1,1.1,1.2,1.3,1.4,1.5,1.6])
fi=np.array([-1.1363,-1.2211,-1.3090,-1.3993,-1.4913,-1.5845,-1.6786])

# Cálculo de la tabla
n=len(xi)
ki=np.arange(0,n)
tabla=np.concatenate(([ki],[xi],[fi]),axis=0)
tabla=np.transpose(tabla)
dfinita=np.zeros((n,n),dtype=float)
tabla=np.concatenate((tabla,dfinita),axis=1)
[n,m]=np.shape(tabla)
j=3
i=0
diagonal=0
while (j < m):
  i=diagonal
  while (i  < n-1):
    tabla[i+1,j]=tabla[i+1,j-1]-tabla[i,j-1]
    i+=1
  diagonal+=1
  j+=1
########

#Obteniendo el polinomio interpolante
x=sym.Symbol('x')
dfinita=np.array([7,-6,6])
h=xi[1]-xi[0]
polinomio=fi[0]
n=len(dfinita)
k=(x-xi[0])/h
termino=k

for i in range(1,n+1):
  polinomio=polinomio + +termino*dfinita[i-1]/np.math.factorial(i)
  termino=termino*(k-i)

print("Polinomio: \n ",polinomio)
polinomiosimple=sym.expand(polinomio)
print("Polinomio simplificado",polinomiosimple)
y=sym.lambdify(x,polinomio)
print(y(1.2))
