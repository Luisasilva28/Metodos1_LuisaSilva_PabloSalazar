def primos(n):
    lista=[]
    i=2
    while len(lista)<n:    
        primo=True
        j=2
        while j<i and primo==True:
            if i%j==0:
                primo=False
            j+=1
        if primo==True:
            lista.append(i)
        i+=1
    return lista

def main():
    print(primos(1000))
    
if __name__=='__main__':
    main()
    
