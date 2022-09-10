import numpy as np
import sympy as sym

def GetLegendre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = (x**2-1)**n
    p = sym.diff(y,x,n)/(2**n * np.math.factorial(n))
    
    return p

Legendre = []

n=20
for i in range(n+1):
    Legendre.append(GetLegendre(i))
    
def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    
    error = 1
    it=0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
    
    if it == itmax:
        return False
    else:
        return xn
    
def GetAllRoots(x,tolerancia=8):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewtonMethod(f,Derivative,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

x = sym.Symbol('x',Real=True)
xtrial = np.linspace(-1,1,100)
print('La raiz del polinomio de grado 0 de Legendre no existe \n')
print('La raiz del polinomio de grado 1 de Legendre es: \n0 \n')
for i in range(2,n+1):
    func=Legendre[i]
    f= sym.lambdify([x],func,'numpy')
    Roots = GetAllRoots(xtrial)
    print('Las raices del polinomio de grado %i de Legendre son:'%i)
    print(Roots,'\n')

