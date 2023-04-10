import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()
x = np.pi/19

Tol = 0.5E-3

n=0
#N=[]
fm=[]
exactitud = []

fx=((-1)**n)*(x**(2*n))/np.math.factorial(2*n)
E=[]
precision=[]
E.append(100)
fm.append(fx)
exactitud.append(100)
#N.append(n)
while E[n]>Tol:
     n+=1
     #N.append(n)
     fx+=((-1)**n)*(x**(2*n))/np.math.factorial(2*n)
     fm.append(fx)
     error=abs(fm[n]-fm[n-1])
     exactitud.append(abs(math.cos(x)-fx))

     E.append(error)

Tabla=[E,fm, exactitud]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["Error", "cosx", "exactitud"])
print(df)  

