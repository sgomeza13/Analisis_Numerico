import pandas as pd
import numpy as np
import math

x = np.pi/(1+1)
n = 0

tol = 5E-8

fm = []
E=[]
fx=((-1)**n)*(x**(1+2*n))/np.math.factorial(1+2*n)
E.append(100)
fm.append(fx)

while E[n] > tol:
    n+=1
    fx+=((-1)**n)*(x**(1+2*n))/np.math.factorial(1+2*n)
    fm.append(fx)
    error_relativo = abs(fm[n]-fm[n-1])/math.sin(x)
    E.append(error_relativo)

Tabla=[E,fm]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["Error Relativo", "Sinx"])
print(df)
