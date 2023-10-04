import numpy as np
#Newton Rapson
#Función original
def f(x):
  return 3*np.exp(-3*x)-np.power(x,3)+3

#Derivada
def df(x):
  return 3*np.exp(-3*x)-3*np.power(x,2)
#Punto NR
xi=1
tol=0.001
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
  
