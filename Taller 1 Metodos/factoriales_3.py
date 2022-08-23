import factoriales_1 as f1
import factoriales_2 as f2
def comb_sin_repeticion(n,m):
    comb=f2.var_sin_repeticion(n, m)/f1.factorial(m)
    return comb

def main():
    print('¿cuantos equipos de 11 jugadores se pueden formar con 22 jugadores disponibles? \n')
    print('Caso 1: cualquiera puede ser el arquero')
    print(comb_sin_repeticion(22, 11))
    print()
    print('Caso 2: ya se sabe quien sera el arquero')
    print(comb_sin_repeticion(21, 10))

if __name__=='__main__':
    main()
    
    