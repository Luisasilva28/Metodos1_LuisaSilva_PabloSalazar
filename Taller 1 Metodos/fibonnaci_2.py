import fibonnaci_1 as f1
import matplotlib.pyplot as plt

def main():
    plt.plot(f1.fib(20),'k',label='Serie Fibonacci')
    plt.legend(loc="upper left")
    plt.title('Primeros 20 números de Fibbonacci')
    plt.show()

main()