import pandas as pd
import numpy as np
import math

x = np.pi/7

n = 0

Tol = 0.5E-3
fm=[]
exactitud = []
fx=((-1)**n)*(x**(1+2*n))/np.math.factorial(1+2*n)
E=[]
E.append(100)
exactitud.append(100)
fm.append(fx)
#N.append(n)
while E[n]>Tol:
     n+=1
     #N.append(n)
     fx+=((-1)**n)*(x**(1+2*n))/np.math.factorial(1+2*n)
     fm.append(fx)
     error=abs(fm[n]-fm[n-1])
     exactitud.append(abs(math.sin(x)-fx))
     E.append(error)

Tabla=[E,fm, exactitud]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["Error", "sinx", "exactitud"])
print(df)  

