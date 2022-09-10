import math as m

#EL POLINOMIO ORIGINAL ES DE GRADO 5
#PODEMOS SIMPLIFICAR EL PROBLEMA TOMANDO FACTOR COMUN X**3
# x**3 * (3x**2 + 5x -1) = 0
#LUEGO 0 ES RAIZ DEL POLINOMIO CON MULTIPLICIDAD 3 
#SOLO FALTA HALLAR LAS RAICES DEL POLINOMIO DE GRADO 2 (3x**2 + 5x -1) = 0
a=3
b=5
c=-1
def raices(a,b,c):
    Roots=[]
    d=(b**2) - (4*a*c)
    sol1 = (-b-m.sqrt(d))/(2*a)
    Roots.append(sol1)
    Roots.append(0)
    sol2 = (-b+m.sqrt(d))/(2*a)
    Roots.append(sol2)
    return Roots

print('Las raíces del polinomio son:')
print(raices(a,b,c))