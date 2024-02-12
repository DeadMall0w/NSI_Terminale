def fibo(n, n1, n2) :
    if n == 0 :
        return n1
    else :
        return fibo(n -1, n1 + n2, n1)
    
    
print(fibo(15, 0, 1))