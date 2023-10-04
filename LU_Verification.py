import numpy as np

A=np.matrix([[5,6,9],[2,1,5],[9,8,4]])
L=np.matrix([[1,0,0],[0.40000001,1,0],[1.79999995,1.99999928,1]])
U=np.matrix([[5,6,9],[0,-1.4000001,1.3999999],[0,0,-14.999998]])
print("A=\n",A)
print("L=\n",L)
print("U=\n",U)
print("Comprobación: \n LU=\n ",L*U  )
x=np.matrix([[3.0571],[-3.7809],[1.9333]])
print("Ax=\n",A*x)
