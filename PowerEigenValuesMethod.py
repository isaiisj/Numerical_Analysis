import numpy as np
import numpy.linalg as alg



def eigPotMin(A,x,tol):
  it=0
  Ain=alg.inv(A)
  print("A^-1=\n",Ain)
  lx=0
  while True:
    it+=1
    m=Ain*x
    mmax=m.max()
    mmin=m.min()
    print(it,m,lx)
    if (abs(mmax) >= abs(mmin) ):
      lx1=1/mmax
    else:
      lx1=1/mmin
    x=lx1*m
    Ea=abs(lx1-lx)
    if( Ea < tol):
      print("Valor característico min:",lx1)
      break
    else:
      lx=lx1


def eigPotMax(A,x,tol):
  m=A*x
  lx=m.max()
  m=(1/lx)*m
  it=0
  while True:
    it+=1
    m=A*m
    lx1=m.max()
    m=(1/lx1)*m
    Ea=abs(lx-lx1)
    print("Ea=",Ea)
    print(it,m,lx)
    if( Ea < tol):
      print("Valor característico máximo ",lx1)
      break
    else:
      lx=lx1

A=np.matrix([[2,3],[1,5]])
x=np.matrix([[1],[1]])
tol=0.01
eigPotMax(A,x,tol)

eigPotMin(A,x,tol)

print(alg.eigvals(A))

