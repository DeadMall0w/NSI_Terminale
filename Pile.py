class Pile:
    def __init__(self):
        self.l = []
        
    def Push(self, el):
        self.l.append(el)

    def Is_empty(self):
        return len(self.l) == 0

    def Sommet(self):
        return self.l[-1]

    def Pop(self):
        if self.Is_empty() == True:
            print("La pile est vide")
        return self.l.pop()
    
    def Len(self):
        return len(self.l)



