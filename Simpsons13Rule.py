#Método de simpson 1/3
import numpy as np
#Límite inferior
a=0
#Límite superior
b=2
#Número de intervalos
n=4
#x en función de intervalos
x=np.zeros(n+1)
#f(x) en expresión lambda
#f=lambda x : x**5
def f(x):
  return x**5

def simpson13(a,b,n,x,f):
  h=(b-a)/n
  for k in range(len(x)-1):
    x[k+1]=x[k]+h
  sum1=0
  sum2=0
  for k in range(1,int(n/2)+1):
    sum1 = sum1 + f( x[2*k-1] )
  for k in range(1,int(n/2-1)+1 ):
    sum2 = sum2 + f( x[2*k] )
  return h*(f(x[0])+f(x[n])+4*sum1+2*sum2)/3

integral=simpson13(a,b,n,x,f)
print("Integral de x**5 es: ",integral  )
