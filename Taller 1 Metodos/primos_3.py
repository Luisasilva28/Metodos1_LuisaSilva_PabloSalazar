import primos_1 as p1
import matplotlib.pyplot as plt

def main():
    n=1000
    plt.plot(p1.primos(n))
    plt.title('Primeros %i números primos'%n)
    plt.show()

main()

