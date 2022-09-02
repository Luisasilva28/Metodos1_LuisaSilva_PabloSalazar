import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,400)
f=lambda x: 1/(np.sqrt(1+np.exp((-x**2))))
h=x[1]-x[0]

def derivada(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

derivada_real=lambda x: (x*np.exp((-x**2)))/(1+np.exp((-x**2)))**(3/2)

fig=plt.figure(figsize=(7,3))
ax=fig.add_subplot(2,2,1)
ax1=fig.add_subplot(2,2,2)
ax2=fig.add_subplot(2,2,3)


funcion=f(x)
derivada=derivada(f,x,h)
derivada_real=derivada_real(x)
ax.plot(x,funcion)
ax1.plot(x,derivada)
ax1.plot(x,derivada_real)
ax2.plot(x,np.abs(derivada-derivada_real))

plt.show()                                                                                                                                  