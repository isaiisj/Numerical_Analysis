#Método LU
import numpy as np

def descLU(A,b):
  A=np.array(A,dtype=np.float32)
  b=np.array(b,dtype=np.float32)
  print("A=\n",A)
  print("b=\n",b)
  m=len(b)
  aux=np.zeros(m)
  auxsol=np.zeros(m)
  #Matriz U
  U=np.zeros([m,m])
  #Matriz L
  L=np.identity(m)
  
  for i in range(m):
    for j in range(i+1,m):
      factor=(A[j,i]/A[i,i])
      L[j,i]=factor
      for c in range(m):
        A[j,c]=A[j,c]-factor*A[i,c]
  aux[0]=b[0]

  #Obteniendo la solución para y
  for i in range(1,m):
    suma=0
    for j in range(m):
      suma=suma+L[i,j]*aux[j]
    aux[i]=b[i]-suma

  U=A
  auxsol[m-1]=aux[m-1]/U[m-1,m-1]
  for i in range(m-2,-1,-1):
    suma=0
    for j in range(m):
      suma=suma+U[i,j]*auxsol[j]
    auxsol[i]=(aux[i]-suma)/U[i,i]
  
  return U,L,aux,auxsol

#Ingresar sin numpy
A=[[5,6,9],[2,1,5],[9,8,4]]
b=[10,12,5]

U,L,y,x=descLU(A,b)
print("L=\n",L)
print("U=\n",U)
print("y=\n",y)
print("x=\n",x)
