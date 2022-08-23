def fib(n):
    a, b = 0, 1
    i=0
    lista=[]
    while i < n:
        lista.append(a)
        a, b = b, a+b
        i+=1
    return lista

def main():
    print(fib(20))

if __name__=='__main__':
    main()
    
