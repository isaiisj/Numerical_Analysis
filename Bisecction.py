import numpy as np


def f(x):
  return np.exp(-x)-np.power(x,3)+3
a=1
b=2
it=1
tol=0.1
print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Itr','a','b','c','f(a)','f(b)','f(c)','Ea'))
while True:
  c=(a+b)/2
  fa=f(a)
  fb=f(b)
  fc=f(c)
  Ea=abs(a-b)    
  print ("{:<8} {:<8.4g} {:<8.4g} {:<8.4g} {:<8.4g} {:<8.4g} {:<8.4g}".format(it,a,b,c,fa,fb,fc,Ea))  
  #g indica el número de cifras significativas
  it+=1
  if(Ea < tol):
    print("Raíz encontrada")
    print("{:0.4g}".format(c) )
    break
  elif (fa*fc)<0:
    #El límite superior será c
    b=c
  elif (fb*fc)<0:
    #El límite inferior será c
    a=c
  else:
    print("No hubo cambio de signo, elija otro intervalo")
    a=float(input("Introduzca el límite inferior 'a':"))
    b=float(input("Introduzca el límite superior 'b: "))
