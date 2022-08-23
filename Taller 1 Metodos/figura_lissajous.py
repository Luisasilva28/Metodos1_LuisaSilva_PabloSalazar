import matplotlib.pyplot as plt
from numpy import pi,sin,linspace

def phi_0():
    t = linspace(0,2*pi)
    k=1
    for i in range(1,6):
        for j in range(1,6):
            if j>=i:
                x=sin(j*t)
                y=sin(i*t)
                fig=plt.subplot(5,5,k)
                plt.plot(y,x)
                fig.set_aspect('equal')
                k+=1
                plt.axis('off')
                
        k+=i
    plt.show()

def phi_45():
    t = linspace(0,2*pi)
    k=1
    for i in range(1,6):
        for j in range(1,6):
            if j>=i:
                x=sin(j*t+pi/4)
                y=sin(i*t)
                fig=plt.subplot(5,5,k)
                plt.plot(y,x)
                fig.set_aspect('equal')
                k+=1
                plt.axis('off')
        k+=i
    plt.show()

def phi_90():
    t = linspace(0,2*pi)
    k=1
    for i in range(1,6):
        for j in range(1,6):
            if j>=i:
                x=sin(j*t+pi/2)
                y=sin(i*t)
                fig=plt.subplot(5,5,k)
                plt.plot(y,x)
                fig.set_aspect('equal')
                k+=1
                plt.axis('off')
        k+=i
    plt.show()
    
def main():
    phi_0()
    phi_45()
    phi_90()
    
    
if __name__=='__main__':
    main()
        

