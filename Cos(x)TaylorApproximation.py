from math import cos
pi=3.1416
VR=cos(pi)
VA=1-(pi)**2/2+(pi)**4/24
print("Valor real: ", VR)
print("Valor aproximado: ",VA)
Ea=abs(VR-VA)
Er=Ea/abs(VR)
Erp=Er*100
print("Error absoluto: ",Ea)
print("Error relativo: ", Er)
print("Error relativo porcentual", Erp)
