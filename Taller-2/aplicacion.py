import matplotlib.pyplot as plt
import numpy as np

# SE DEFINE EL CIRCULO
theta=np.linspace(0,2*np.pi,100)
radius=2
xc = radius*np.cos(theta)
yc = radius*np.sin(theta)

# DEFINIR MESHGRID
xi,xf,N=-4,4,25
x = np.linspace(xi,xf,N)
y = x.copy()
h=x[1]-x[0]
X, Y = np.meshgrid(x, y)

# DEFINIR PUNTOS FUERA DEL CIRCULO (X[outside], Y[outside])
r = np.sqrt((X)**2 + (Y)**2)
outside = r > radius

# DEFINIR FUNCION POTENCIAL DE FLUJO
V=2
f=lambda X,Y: V*X*(1-((radius**2)/ (X**2 + Y**2)))

# DEFINIR DERIVADA X
def Dx(f,x,y,h):
    return (f(x+h,y)-f(x-h,y))/(2*h)

Dx=Dx(f,X[outside],Y[outside],h)

# DEFINIR DERIVADA Y
def Dy(f,x,y,h):
    return (f(x,y-h)-f(x,y+h))/(2*h)

Dy=Dy(f,X[outside],Y[outside],h)

# GRAFICAR
fig, ax = plt.subplots()
ax.set(xlabel='x [cm]', ylabel='y [cm]', aspect='equal') 
ax.plot(xc,yc,color='r')

for i in range(X[outside].size):
    ax.quiver(X[outside][i],Y[outside][i],Dx[i],Dy[i],color='b',alpha=0.6)

plt.show()
