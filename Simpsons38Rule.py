#Simpson3/8
import numpy as np

#Límite inferior
a=0
#Límite superior
b=2
#Número de intervalos
n=7 # puntos= n+1
#x en función de intervalos
x=np.zeros(n+1)
#Definimos la función
f= lambda x: x**5

def simpson38(a,b,n,x,f):
  h=(b-a)/n
  x[0]=a
  x[n]=b
  for k in range(len(x)-1):
    x[k+1]=x[k]+h
  sum1=0
  sum2=0
  sum3=0
  for k in range(1,n-1,3):
    sum1+=f(x[k])
  for k in range(2,n,3):
    sum2+=f(x[k])
  for k in range(3,n-2,3):
    sum3+=f(x[k])
  #print(h)  
  return (3*h*(f(x[0])+f(x[n]) +3*sum1+3*sum2+2*sum3))/8

integral= simpson38(a,b,n,x,f)

print("La integral de x**5 en el intervalo [0,2]",integral)
