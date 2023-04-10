import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()

print("X0:")
X0 = float(input())
print("x1: ")
X1 = float(input())
print("Tol:")
Tol = float(input())
print("Niter:")
Niter = float(input())

Fun = lambda x: abs(x)**(x-1) -(2.5*x)-5 #Aca se ingresa la funcion


fn=[]
xn=[]
E=[]
N=[]
fn.append(Fun(X0))
fn.append(Fun(X1))
c=0
Error=100               
xn.append(X0)
xn.append(X1)
E.append(Error)
Error = abs(X1-X0)
E.append(Error)
N.append(c)
N.append(c+1)
while Error>Tol and fn[c]!=0 and c<Niter:
  print(fn)
  print(xn)  
  x=xn[c]-(fn[c]*(xn[c]-xn[c-1])/(fn[c]-fn[c-1]))
 
  f=Fun(x)
  fn.append(f)
  xn.append(x)
  c=c+1
  Error=abs(xn[c]-xn[c-1])
  N.append(c)
  E.append(Error)
if f==0:
    s=x
    print(s,"es raiz de f(x)")
elif Error<Tol:
    s=x
    print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
    print("N",N)
    print("xn",xn)
    print("fn",fn)
    print("Error",E)
else:
    s=x
    print("Fracaso en ",Niter, " iteraciones ") 

Tabla=[fn,E,xn]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["F(n)", "Error","Xn"])
print(df)
