def factorial(n)->int:
    fact=1
    if n==0 or n==1:
        return fact
    else:
        for i in range(2,n+1):
            fact*=i
    return fact

def main():
    n=int(input('Ingrese numero:\n'))
    print()
    print('El factorial de %i es:'%n)
    print(factorial(n))

    lista=[]
    print()
    print('Los primeros 20 factoriales son:')
    for j in range(1,21):
        lista.append(factorial(j))
    print(lista)
    
if __name__=='__main__':
    main()
      