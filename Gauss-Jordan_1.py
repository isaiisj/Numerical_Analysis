#Metodo de Gauss-Jordan
import numpy as np

x = np.matrix([[ 3, -6, 7],[ 8, 0, -5],[ 1, -2, 6]])
x = np.array(x, dtype=np.float32)
print("x=",x)
b = np.matrix([[4],[19],[5]])
b = np.array(b, dtype=np.float32)
print("b=",b)

xa = np.concatenate((x,b), axis=1)
print("xa=",xa)
#obteniendo los elementos de la matriz para obtener el pivote 
mx=xa[:,:3]
print("mx=",mx)

pivote = np.max(np.abs(mx))
print("pivote= ",pivote)

#transformacion de renglones 
xa[1,:] = 1/pivote*xa[1,:]
print("transformación de renglon")
print("xa= ",xa)
xa[0,:]=xa[0,:]-3*xa[1,:]
print("xa= ",xa)
