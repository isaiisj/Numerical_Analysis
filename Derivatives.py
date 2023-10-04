import numpy as np
import matplotlib.pyplot as plt

n=20
a=1
b=3
h=(b-a)/n
x=np.linspace(a,b,n)
#Función f(x) original
f= lambda x: (x**3)/(0.12-x**2)
#Función f'(x)
fp= lambda x: (-6*x**3-0.12*x**3+x**5)/(0.12-x**2)**2
#Función f''(x)
fpp= lambda x: 0

y=f(x)

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
#Primera derivada
yp=derivadaFinita(x,y)
#Segunda derivada
#ypp=derivadaFinita(x,yp)
def derivadaFinita2(x,y):
  h=x[1]-x[0]
  n=len(x)
  ypp=np.zeros(n)
  for i in range(n):
    #Progresivas
    if(i==0):
      ypp[i]=(y[i+2]-2*y[i+1]+y[i])/h**2
    #Regresivas
    elif (i==n-1):
      ypp[i]=(y[i]-2*y[i-1]+y[i-2])/h**2
    else:
      ypp[i]=(y[i+1]-2*y[i]+y[i-1])/h**2
  return ypp
    
ypp=derivadaFinita2(x,y)

#Derivada analítica
#plt.plot(x,fpp(x),'r-')
#plt.plot(x,ypp,'bo')
#plt.grid(True)
#plt.show()
