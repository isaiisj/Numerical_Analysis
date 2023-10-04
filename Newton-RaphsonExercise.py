import numpy as np
#Newton Rapson
#Función original
def f(x):
  return 10*np.sin(x*np.exp(-x))-1

#Derivada
def df(x):
  return 10*np.cos(x*np.exp(-x))*(np.exp(-x)-x*np.exp(-x))
#Punto NR
xi=.3
tol=0.0001
it=1

print ("{:<8} {:<8} {:<8} {:<8} ".format('Itr','x_i','x_i+1','Ea'))
while True:
  #Criterio de convergencia
  if (df(xi) == 0):
    xi=float(input("Introduce un nuevo punto para obtener la raíz"))
    continue
  xi1=xi-f(xi)/df(xi)
  Ea=abs(xi1-xi)
  print ("{:<8} {:<8.4g} {:<8.4g} {:<8.4g} ".format(it,xi,xi1,Ea))  
  xi=xi1
  it+=1
  if(Ea < tol):
    print("Raíz encontrada")
    print("{:.4g}".format(xi1) )
    break
