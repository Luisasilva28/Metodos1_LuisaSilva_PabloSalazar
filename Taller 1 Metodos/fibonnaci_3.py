import fibonnaci_1 as f1
import math as m
import matplotlib.pyplot as plt

def main():
    n=20
    numero_aureo=(1+m.sqrt(5))/2
    lista=[]
    for i in range(2,n+1):
        aprox=f1.fib(i+1)[i]/f1.fib(i)[i-1]
        lista.append(aprox)
    plt.plot(lista,label='Estimación usando la serie')
    plt.axhline(y=numero_aureo, color='r', linestyle='--',label='Número Áureo')
    plt.legend(loc="upper right")
    plt.show()
    
main()

