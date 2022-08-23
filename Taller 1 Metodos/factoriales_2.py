import factoriales_1 as f1 
def var_sin_repeticion(n,r)->int:
    variaciones=f1.factorial(n)/f1.factorial(n-r)
    return variaciones

def main():
    print('La cantidad de maneras en las que se pueden ubicar 6 carros en 3 estacionamientos es:')    
    print(var_sin_repeticion(6,3))
    
if __name__=='__main__':
   main()

