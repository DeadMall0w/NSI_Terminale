def pgcd(a,b):
    r = a % b
    q = a//b
    
    if q >= 1:
        a = a%b
    if r == 0:
        return b
    return pgcd(b,a)


def nbNMBR(nb, n=0):
    if nb >= 10:
        nb /= 10
        n += 1
        nbNMBR(nb,n)
    else:
        print(n+1)
        
        
def pal(mot):
    if len(mot) <= 1:
       return True
    
    if mot[0] != mot[-1]:
        return False
    else:
        return pal(mot[1:len(mot)-1])
    
    
    
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n
    
    
    
def SommeListe(liste):
    if len(liste) == 0:
        return 0
    else:
        return SommeListe(liste[1:])+liste[0]
    

    