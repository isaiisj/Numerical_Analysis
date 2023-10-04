#tabla de dezplazamiento:
import numpy as np
import sympy as sym
dt=lambda x: x**3 /(0.12-x**2)

t=np.linspace(0,3,20) 
dis=dt(t)
v=derivadaFinita(t,dis)


x,polinomio= InLagrange(t,v)
funcion_lista=sym.lambdify(x,polinomio)
print("velocidad(1.2)=",funcion_lista(1.2))


def derivadaFinita(x,y):
  h=x[1]-x[0]
  n=len(x)
  yp=np.zeros(n)
  for i in range(n):
    if (i==0):
      yp[i]=(y[i+1]-y[i])/h
    elif (i==n-1):
      yp[i]=(y[i]-y[i-1])/h
    else:
      yp[i]=(y[i+1]-y[i-1])/(2*h)
  return yp

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
  #print('polinomio no desarrollado \n',polinomio)
  #print('polinomio simplificado \n',polisimple)
  return x,polinomio
