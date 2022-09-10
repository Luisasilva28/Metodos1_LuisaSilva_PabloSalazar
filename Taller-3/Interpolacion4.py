import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import urllib

url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'
data = urllib.request.urlopen(url)

Data = pd.read_csv(data,sep=',')
X = np.float64(Data['X'])
Y = np.float64(Data['Y'])

def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod

def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum

x=np.linspace(0,6.6,100)
plt.scatter(X, Y, color='red')
plt.plot(x,Poly(x,X,Y))

x = sym.Symbol('x')
polinomio_cuadratico = sym.expand(Poly(x,X,Y))
coeficiente_cuadratico=float(polinomio_cuadratico.coeff(x,2))
derivada=sym.diff(polinomio_cuadratico)
theta=(float(derivada.coeff(x,0)))
v0=np.sqrt(np.abs( 9.81 / ( coeficiente_cuadratico*2*(np.cos(theta)**2) ) ))
theta=np.degrees(theta)
print('La velocidad inicial es %.0f m/s con ángulo de %.0f grados con la horizontal'%(v0,theta))