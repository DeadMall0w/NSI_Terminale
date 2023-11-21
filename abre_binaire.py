from File import * 

class ArbreBinaire():
    def __init__(self, etiquette = None, sag = None, sad = None):
        self.etiquette = etiquette
        self.sag = sag
        self.sad = sad
        self.v = 0
        
    def est_vide(self):
        if self.etiquette is None:
            return True
        return False
    
    def hauteur(self):
        if self.est_vide():
            return -1
        return 1 + max(self.sag.hauteur(), self.sad.hauteur())
    
    def taille(self):
        if self.est_vide():
            return 0
        return 1 + self.sag.taille() + self.sad.taille()

    def parcoursPrefixe(self):
        if not self.etiquette is None:
            x = self
            print(x.etiquette)
            self.sag.parcoursPrefixe()
            self.sad.parcoursPrefixe()
    
    def parcoursSuffixe(self):
        if not self.etiquette is None:
            x = self
            self.sag.parcoursSuffixe()
            self.sad.parcoursSuffixe()
            print(x.etiquette)

    def parcoursInfixe(self):
        if not self.etiquette is None:
            x = self
            self.sag.parcoursInfixe()
            print(x.etiquette)
            self.sad.parcoursInfixe()
            
    def trouver(self, el):
        if self.etiquette is None:
            return False
        x = self
        if x.etiquette == el:
            return True
        if el < x.etiquette:
            return self.sag.trouver(el)
        else:
            return self.sad.trouver(el)

    def parcoursLargeur(self):
        filee = File()
        filee.enfiler(self)
        while filee.is_empty() == False:
            x = filee.defiler()
            print(x.etiquette)
            if not x.sag.etiquette is None: 
                filee.enfiler(x.sag)
            if not x.sad.etiquette is None: 
                filee.enfiler(x.sad)



#creer un abre binaire 
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