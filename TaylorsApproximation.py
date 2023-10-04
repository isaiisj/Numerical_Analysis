import math
from math import factorial

def fun(num):
    e=2.7128
    vr_e=0
    for i in range(num):
        vr_e = vr_e + 1/factorial(i)
        print("valor aporximado de e: ",vr_e)
        ea = abs(vr_e - e) 
        print("error absoluto: ",ea)
        er = ea/vr_e
        print("error relativo: ",er)
        erp = er*100
        print("error relativo porcentual: ",erp)
        print("-------")

fun(7)
        
#vr_e = 2.71828
#e=1 + 1 + 0.5 + (1/6) + (1/24)
#print("valor aporximado de e: ",e)
#ea = abs(vr_e - e) 
#print("error absoluto: ",ea)
#er = ea/vr_e
#print("error relativo: ",er)
#erp = er*100
#print("error relativo porcentual: ",erp)

#e0 = 1/factorial(0)
#print("valor de e0", e0)
#n=1
#while True: 
#    e1=e0+1/factorial(n)
#    print("Valor aproximado de e: ",e1)
#    Ea=abs(e0-e1)
#    print("Error absoluto: ", Ea)
#    Er=Ea/abs(e0)
#    print("Error relativo: ", Er)
#    Erp=Er*100
#    print("Error relativo porcentual: ", #Erp)
#    e0=e1
#    n=n+1 #n+=1
#    if Erp < 1.5:
#        break
