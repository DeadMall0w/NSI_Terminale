from File import * 


x = 0
y = 0

def afficher(x, y,val):
    #print(x, val)
    espace = '  '
    espaceDepart = espace * int(14/y)
    
    if x < 0:
        print(espaceDepart[:x] + val)
    else:
        print(espaceDepart + (espace * x) + val)


class ArbreBinaire():
    def __init__(self, etiquette = None, sag = None, sad = None):
        self.etiquette = etiquette
        self.sag = sag
        self.sad = sad
        self.v = 0
        
    def est_vide():
        if self.etiquette is None:
            return True
        return False
    
    def hauteur(self):
        if self.etiquette is None:
            return -1
        return 1 + max(self.sag.hauteur(), self.sad.hauteur())

    def parcoursPrefix(self, p=0,y=1):
        if not self.etiquette is None:
            x = self
            afficher(p, y,str(x.etiquette))
            self.sag.parcoursPrefix(p-1,y+1)
            self.sad.parcoursPrefix(p+1,y+1)
            
            
    def Trouver(self, el):
        if self.etiquette is None:
            return False
        x = self
        print(x.etiquette)
        if x.etiquette == el:
            return True
        if el < x.etiquette:
            return self.sag.Trouver(el)
        else:
            return self.sad.Trouver(el)

    def parcourLargeur(self):
        filee = File()
        filee.enfiler(self) #on place la racine dans la file
        while filee.is_empty() == False:
            x = filee.defiler()
            print(x.etiquette)
            if not x.sag.etiquette is None: 
                filee.enfiler(x.sag)
            if not x.sad.etiquette is None: 
                filee.enfiler(x.sad)
        
    def AfficherArbre(self):
        l = []
        filee = File()
        filee.enfiler(self) 
        while filee.is_empty() == False:
            x = filee.defiler()
            l.append(x.etiquette)
            if not x.sag.etiquette is None: 
                filee.enfiler(x.sag)
                l.append('♥')
            if not x.sad.etiquette is None: 
                filee.enfiler(x.sad)
                l.append('♥')
        for i in range(len(l)):
            print(l[i])
        return l
    
a = ArbreBinaire(15, ArbreBinaire(), ArbreBinaire())
a.sag = ArbreBinaire(6, ArbreBinaire(), ArbreBinaire())
a.sag.sag = ArbreBinaire(3, ArbreBinaire(), ArbreBinaire())
a.sag.sag.sag = ArbreBinaire(2, ArbreBinaire(), ArbreBinaire())
a.sag.sag.sad = ArbreBinaire(4, ArbreBinaire(), ArbreBinaire())
a.sag.sad = ArbreBinaire(7, ArbreBinaire(), ArbreBinaire())
a.sag.sad.sad = ArbreBinaire(13, ArbreBinaire(), ArbreBinaire())
a.sag.sad.sad.sag = ArbreBinaire(9, ArbreBinaire(), ArbreBinaire())

a.sad = ArbreBinaire(18, ArbreBinaire(), ArbreBinaire())
a.sad.sag = ArbreBinaire(17, ArbreBinaire(), ArbreBinaire())
a.sad.sad = ArbreBinaire(20, ArbreBinaire(), ArbreBinaire())