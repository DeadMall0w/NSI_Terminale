from random import *
''' Tri Fusion

VARIABLE
tab : tableau d'entiers
tab1 : tableau d'entiers
tab2 : tableau d'entiers
tab_sortie : tableau d'entiers
i1 : entier
i2 : entier
n : entier


DEBUT

FUSION (tab1, tab2):
  i1 = 0
  i2 = 0
  tab_sortie = []
  tant que i1 < longueur de tab1 ET i2 < longueur de tab2:
    si tab1[i1] < tab2[i2]:
      ajouter tab1[i1] à tab_sortie
      i1 = i1+1
    sinon:
      ajouter tab2[i2] à tab_sortie
      i2 = i2+1
    fin si
  fin tant que
  
  si i1 = longueur de tab1:
    ajouter le reste de tab2 à partir de l'indice i2 à tab_sortie
  sinon:
    ajouter le reste de tab1 à partir de l'indice i1 à tab_sortie
  fin si
  
  renvoyer tab_sortie
fin FUSION

Tri_Fusio(tab):
  n = longueur de tab
  si n < 2:
    renvoyer tab
  sinon
    renvoyer FUSION(Tri_Fusio(n//2 premiers éléments de tab),Tri_Fusio(n//2 derniers éléments de tab))
  fin si
fin Tri_Fusio

FIN

'''
def create_random_liste(longeur):
    return [randint(-69000,69000) for i in range(longeur)]

def fusion(tab1, tab2):
    i1 = 0
    i2 = 0
    tab_sortie = []
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_sortie.append(tab1[i1])
            i1 += 1
        else:
            tab_sortie.append(tab2[i2])
            i2 += 1
    if i1 == len(tab1):
        for elements in tab2[i2:]: tab_sortie.append(elements)
    else:
        for elements in tab1[i1:]: tab_sortie.append(elements)
    return tab_sortie
        
def tri_fusion(tab):
    n = len(tab)
    if n < 2:
        return tab
    else:
        return fusion(tri_fusion(tab[0:n//2]), tri_fusion(tab[n//2:]))



def fusion_minimum(tab1, tab2):
    return min(tab1, tab2)
        
def min_fusion(tab):
    n = len(tab)
    if n < 2:
        return tab
    else:
        return fusion_minimum(min_fusion(tab[0:n//2]), min_fusion(tab[n//2:]))
