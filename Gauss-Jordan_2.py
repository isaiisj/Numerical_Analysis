import numpy as np

def gaussJordan(A,b):
  A=np.array(A,dtype=np.float32)
  b=np.array(b,dtype=np.float32)
  m=len(b)
  aux=np.zeros(m)
  for i in range(m):
    for j in range(i+1,m):
      factor=A[j,i]/A[i,i]
      b[j]=b[j]-factor*b[i]
      for c in range(m):
        A[j,c]=A[j,c]-factor*A[i,c]
  aux[m-1]=b[m-1]/A[m-1,m-1]


  for r in range(m-2,-1,-1):
    suma=0
    for c in range(m):
      suma=suma+A[r,c]*aux[c]
    aux[r]=(b[r]-suma)/A[r,r]
  return aux
A=np.matrix([[5,7,9],[2,4,5],[9,8,11]])
b=np.matrix([[16],[12],[40]])
print(gaussJordan(A,b))
#x=np.matrix([[-36],[-224],[196]])
#print("b=",A*x)
