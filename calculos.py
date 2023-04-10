import numpy as np
#Calculo numero de iteraciones metodo punto fijo
print("Escriba 1 para hallar el numero de iteraciones del metodo punto fijo, 0 para biseccion")
res = int(input())
if res==1:
    print("a(x_inferior): ")
    a = float(input())
    print("b(x_superior): ")
    b = float(input())
    print("k: ")
    k = float(input())
    print("P_0: ")
    p_0 = float(input())
    print("Tolerancia: ")
    tol = float(input())

    maximo = max((p_0-a),b-p_0)


    n_iteraciones = np.log(tol/maximo)/np.log(k)
    print("El numero de iteraciones (ignorando los decimales) es: %1f" % (n_iteraciones))
else:
    print("a(x_inferior): ")
    a = float(input())
    print("b(x_superior): ")
    b = float(input())
    print("Escriba 1 si tiene la tolerancia, 0 si la necesita hallar")
    res2 = int(input())
    if res2==1:
        print("Tolerancia: ")
        tol = float(input())
    else:
        print("X_v: ")
        x_v = float(input())
        print("X_mn: ")
        x_mn = float(input())
        tol = abs(x_v - x_mn)
    iteraciones = np.log2((b-a)/tol)
    print("El numero de iteraciones es > %1f" % (iteraciones))
