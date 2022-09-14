import numpy as np
import matplotlib.pyplot as plt

def derivada_central(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

def derivada_progresiva(y,x,h):
    derivada=0
    lista=[]
    for i in range(len(y)-1):
        derivada=(y[i+1]-y[i])/h
        lista.append(derivada)
    return lista

x=np.linspace(0.1,1.1,100)
h=x[1]-x[0]
f=lambda x: np.sqrt(np.tan(x))
y=f(x)

df=lambda x: ((np.cos(x))**-2)/(2*np.sqrt(np.tan(x)))
derivada_real=df(x)

fig=plt.figure(figsize=(15,10))

ax=fig.add_subplot(2,2,1)
ax1=fig.add_subplot(2,2,2)
ax2=fig.add_subplot(2,2,3)
ax3=fig.add_subplot(2,2,4)

plt.setp([ax,ax1,ax2,ax3], xlabel='x',ylabel='y')

ax.plot(x,derivada_central(f, x, h),label='Derivada Central')
ax.legend(loc="upper right")
ax.plot(x,derivada_real)

ax1.plot(x[:-1],derivada_progresiva(y, x, h),label='Derivada Progresiva')
ax1.legend(loc="upper right")
ax1.plot(x,derivada_real)

ax2.plot(x,np.abs(derivada_central(f,x,h)-derivada_real),label='Error Derivada Central')
ax2.legend(loc="upper right")

ax3.plot(x[:-1],np.abs(derivada_progresiva(y,x,h)-derivada_real[:-1]),label='Error Derivada Progresiva')
ax3.legend(loc="upper right")

print('Los errores de las derivadas varían drásticamente')
print('La derivada central parece tener un error de precisión h^2 en el intervalo x=[0.2 , 1.0]')
print('La derivada progresiva parece tener un error de precisión h^2 solo en el punto x=0.5')
print('Esto parece indicar que la derivada central es más precisa que la progresiva')
