#Gauss-Seidel
import numpy as np

def gs(A,b,tol):
  A=np.array(A,dtype=np.float32)
  b=np.array(b,dtype=np.float32)
  it=0
  n=len(A[0:])
  x=np.zeros((n))
  while True:
    xi=x[0]
    for i in range(n):
      pivote=A[i,i]
      for j in range(n):
        A[i,j]=A[i,j]/pivote
      b[i]=b[i]/pivote
    for i in range(n):
      sum=b[i]
      for j in range(n):
        if (i != j):
          sum=sum-A[i,j]*x[j]
      x[i]=sum
    Ea=np.abs(xi-x[0])
    print("it=\n",it)
    print("x=\n",x)
    print("Ea=\n",Ea)
    it+=1
    if( Ea < tol):
      break


A=np.matrix([[9,1,1],[2,-10,5],[5,3,11]])
b=np.matrix([[5],[12],[20]])
tol=0.01
gs(A,b,tol)


#x=np.matrix([[5.078],[2.922],[0.9609]])
#print("b=",A*x)
