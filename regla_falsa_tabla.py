import numpy as np
import pandas as pd

# INGRESO
fx = lambda x: -7*np.log(x)+x-15
print("a")
a = float(input())
print("b")
b = float(input())
print("Tolerancia")
tolera = float(input())
print("Numero de iteraciones")
niter = float(input())

index = 0
flag = False
fm =[]
error = []
xm = []
# PROCEDIMIENTO
tramo = abs(b-a)
while not(tramo<=tolera and index<=niter):

    fa = fx(a)
    fb = fx(b)
    c = b - fb*(a-b)/(fa-fb)
    xm.append(c)
    fc = fx(c)
    fm.append(fc)
    cambia = np.sign(fa)*np.sign(fc)
    if (cambia > 0):
        tramo = abs(c-a)
        error.append(tramo)
        a = c
    else:
        tramo = abs(b-c)
        error.append(tramo)
        b = c
    index = index+1
    if index == niter:
        flag = True
raiz = c

# SALIDA
if(flag==False):
    print("numero de iteraciones: \n",index)
    print("resultado: \n",raiz)
else:
    print("Alcanzo el numero maximo de iteraciones")
print("fm: \n")
print(fm)
print("Error: \n")
print(error)
print("Xm: \n")
print(xm)

#Creacion tabla
tabla = [fm,error,xm]
tabla = np.transpose(tabla)
df = pd.DataFrame(tabla, columns=["F(m)","Error","Xm"])
print(df)

