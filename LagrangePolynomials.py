#Metodo de Lagrange
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Datos de la tabla
xi=np.array([-2.1,-1.8,0,1,1.1,2.4])
yi=np.array([-40.84,-18.89,0,1,1.61,79.62])

def InLagrange(xi,yi):
  n=len(xi)
  x=sym.Symbol('x')
  polinomio=0
  #Sumatoria
  for i in range(0,n):
    numerador=1
    denominador=1
    #Productorio
    for j in range(0,n):
      if( i!=j ):
        numerador=numerador*(x-xi[j])
        denominador=denominador*(xi[i]-xi[j])
      termino=(numerador/denominador)*yi[i]
    polinomio=polinomio+termino
  polisimple=sym.expand(polinomio)
  #Salida
  print('polinomio no desarrollado \n',polinomio)
  print('polinomio simplificado \n',polisimple)
  return x,polinomio
  
x,polinomio= InLagrange(xi,yi)


#def graficaLagrange(xi,yi,x,polinomio,muestras):
  px=sym.lambdify(x,polinomio)
  n=len(xi)
  a=xi[0]
  b=xi[n-1]
  pxi=np.linspace(a,b,muestras)
  pyi=px(pxi)
  #Graficar
  plt.plot(xi,yi,'o')
  plt.plot(pxi,pyi)
  plt.show()
  return px

muestras=20
px=graficaLagrange(xi,yi,x,polinomio,muestras)
xmuestra=np.array([0.5, 0.7]) 
print("f(xm)=",  px(xmuestra))
