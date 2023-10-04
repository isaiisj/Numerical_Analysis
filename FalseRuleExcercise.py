#Método de regla falsa, falsa posición y Secante
import numpy as np

def rf(a,b):
  return b-f(b)*(a-b)/(f(a)-f(b))

def f(x):
  return np.exp(-x)-np.power(x,2)

a=0.5
b=1
tol=0.1
cabecera="{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} ".format('Itera','a','b','c','f(a)','f(b)','f(c)')
print(cabecera)
it=1

while True:
  c=rf(a,b)
  fa=f(a)
  fb=f(b)
  fc=f(c)
  fila="{:<8} {:<8.4f} {:<8.4f} {:<8.4f} {:<8.4f} {:<8.4f} {:<8.4f}".format(it,a,b,c,fa,fb,fc)
  print(fila)
  if( abs(fc) < tol  ):
    print("Raíz encontrada")
    print("{:0.4f}".format(c))
    break
  elif (fa*fc) < 0:
    b=c
  elif (fb*fc) < 0:
    a=c
  else:
    print("No hubo cambio de signo, elige otro intervalo")
    a=float(input("Introduce límite inferior"))
    b=float(input("Introduce límite superior"))
  it+=1
  
