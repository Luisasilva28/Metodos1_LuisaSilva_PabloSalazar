import numpy as np
import math as m
import matplotlib.pyplot as plt
def espiral():
    rads = np.arange(0,(6*np.pi),0.02)
    x=[]
    y=[]
    for rad in rads:
       x.append(rad*m.cos(rad)) 
       y.append(rad*m.sin(rad))
    plt.plot(x,y)
    plt.show()

def main():
    espiral()
    
if __name__=='__main__':
    main()