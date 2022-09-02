import numpy as np
import matplotlib.pyplot as plt
xi,xf,N=-10,10,400
x=np.linspace(xi,xf,N)
h=x[1]-x[0]

matrix=np.array([-1,0,1])
f=lambda x:1/np.sqrt(1+np.exp(-x**2))
f=f(x)

i=1
suma=np.array([])

while i<=len(f):
    j= i-1
    k= i+1
    if j<len(f) and k<len(f):
        conv=(f[i]*matrix[1])+(f[j]*matrix[0])+(f[k]*matrix[2])
        suma=np.append(suma,conv)
    i+=1
    
derivada=suma/(2*h)
derivada=np.insert(derivada,[0,N-2],0)        
plt.plot(x,derivada)

plt.show()