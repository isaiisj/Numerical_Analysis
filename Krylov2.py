import numpy as np
from math import sqrt
A=np.matrix([[1,2,4],[7,3,1],[0,1,4]])
y=np.matrix([[1],[0],[0]])

print("A=\n",A)
print("y=\n",y)

def krylov(A,y):
  n=len(A[0:])
  cont=n-1
  m=np.zeros((n,n))
  b=np.zeros((n,1))
  Ak=A*y
  m[0:,cont:]=y
  while cont > 0:
    if(cont != 0):
      m[0:,0:cont]=Ak
    print("A{0}=\n{1}".format(cont,Ak))
    print("m=\n",m)
    Ak=A*Ak
    cont-=1
  return m,-Ak

m,Ak=krylov(A,y)



print(Ak)
