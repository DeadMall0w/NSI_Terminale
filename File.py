class File:
    def __init__(self):
        self.content = []

    def is_empty(self):
        return self.content == []

    def enfiler(self, el):
        self.content.append(el)

    def defiler(self):
        if self.is_empty():
            print("aucun element car la file est vide")
            return
        return self.content.pop(0)

    def premier(self):
        return self.content[0]
    
    def sommet(self):
        return self.content[0]