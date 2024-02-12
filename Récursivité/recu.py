
def nb_chiffre(n):
    if n < 10:
        return 1
    else:
        return nb_chiffre(n/10)+1
    
def syracuse(u):
    print("u :",u)
    if u <= 1:
        return
    else:
        if u % 2 == 0:
            return syracuse(u/2)
        else:
             return syracuse(3*u+1)
            
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n
    
def pgcd(a,b):
    q = a%b
    if q >= 1:
        a = a%b
    r = a//b
    print(a,b,q,r)
    if r == 0:
        return q
    else:
        return pgcd(b,a)
    
    