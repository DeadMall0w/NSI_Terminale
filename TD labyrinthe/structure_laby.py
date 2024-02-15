from structures_lineaires import Pile,File


class Graphe:
    ''' Définition de la classe Graphe constituée de 2 attributs :
        un dictionnaire d'adjacence et un booléen
        précisant si le graphe est orienté ou non
    '''
    def __init__(self,oriente=False):
        ''' Constructeur de la classe '''
        self.dict_adj={
    'A1': ['B1'],
    'A2': ['A3', 'B2'],
    'A3': ['A2','B3'],
    'A4': ['A5', 'B4'],
    'A5': ['A4', 'A6'],
    'A6': ['A5', 'B6'],
    'A7': ['B7', 'A8'],
    'A8': ['A7','B8'],
    'A9': ['B9'],
    'A10': ['A9', 'B10'],

    'B1': ['A1', 'B2'],
    'B2': ['A2', 'B2'],
    'B3': ['A3', 'C3'],
    'B4': ['A4', 'B5'],
    'B5': ['B4', 'C5'],
    'B6': ['A6', 'B7'],
    'B7': ['A7', 'B6'],
    'B8': ['A8', 'B9'],
    'B9': ['B8', 'C9'],
    'B10': ['A10', 'C10'],

    'C1': ['C2', 'D1'],
    'C2': ['C1', 'C3'],
    'C3': ['C2','C4','B3'],
    'C4': ['C3'],
    'C5': ['B5', 'D5'],
    'C6': ['C7', 'D6'],
    'C7': ['C6', 'D7'],
    'C8': ['C9', 'D8'],
    'C9': ['C8', 'D10'],
    'C10': ['B10', 'C9'],

    'D1': ['C1', 'D2'],
    'D2': ['D1', 'D3', 'E2'],
    'D3': ['D2'],
    'D4': ['D5', 'E4'],
    'D5': ['C5', 'D4','D6'],
    'D6': ['C6', 'D5'],
    'D7': ['C7', 'E7'],
    'D8': ['C8', 'D9'],
    'D9': ['D8', 'D10'],
    'D10': ['D9', 'E10'],

    "E1" : ["E2", "F1"],
    "E2" : ["E1", "D2"],
    "E3" : ["E4", "F3"],
    "E4" : ["D4", "E3"],
    "E5" : ["E6", "F5"] , 
    "E6" : ["E5", "E7"], 
    "E7" : ["E6", "D7"], 
    "E8" : ["E9", "F8"], 
    "E9" : ["D9", "E8"], 
    "E10" : ["D10", "F10"],

     "F1":["E1","F2"],
     "F2":["F1","F3"],
     "F3":["F2","E3","G3"],
     "F4":["G4","F5"],
     "F5":["F4","E5"],
     "F6":["F7"],
     "F7":["F6","F8"],
     "F8":["F7","E8"],
     "F9":["F10"],
     "F10":["F9","E10"],
    
     "G1":["H1","G2"],
     "G2":["G1","G3"],
     "G3":["G2","F3"],
     "G4":["F4","G5"],
     "G5":["G4","G6"],
     "G6":["G5","H6"],
     "G7":["F7","G8"],
     "G8":["G7","G9"],
     "G9":["G8","H9"],
     "G10":["G9","H10"],

    "H1": ["G1", "H2"],
    "H2": ["H1", "I2"],
    "H3": ["I3", "H4"],
    "H4": ["H3", "I4"],
    "H5": ["H6"],
    "H6": ["G6"],
    "H7": ["I7", "H8"],
    "H8": ["H7", "H9"],
    "H9": ["H8", "G9"],
    "H10": ["G10", "I10"],
 
    "I1": ["I2", "J1"],
    "I2": ["H2", "I1"],
    "I3": ["J3", "H3"],
    "I4": ["H4", "J4"],
    "I5": ["J5", "I6"],
    "I6": ["I5", "J6"],
    "I7": ["H7", "I8"],
    "I8": ["I7", "I9"],
    "I9": ["I8", "J9"],
    "I10": ["H10"],
 
    "J1": ["I1", "J2"],
    "J2": ["J1", "J3"],
    "J3": ["J2", "I3"],
    "J4": ["I4", "J5"],
    "J5": ["J4", "I5"],
    "J6": ["I6", "J7"],
    "J7": ["J6", "J8"],
    "J8": ["J7"],
    "J9": ["I9", "J10"],
    "J10": ["J9"]
}
        self.oriente=oriente

    def ajouter_sommet(self,s):
        '''
        Méthode qui permet d'ajouter un sommet au graphe
        '''
        if not s in self.dict_adj.keys():
            # Ajout d'une entrée vide correspondant à la clé du sommet s dans le dictionnaire d'adjacences
            self.dict_adj[s]=[]
    
       
    def ajouter_arc(self,s1,s2,poids=1):
        '''
        Méthode qui permet d'ajouter un arc entre 2 sommets du graphe définis par leur clé
        '''
        # Ajout automatique des sommets s1 et s2 au graphe si ils n'existent pas
        if not s1 in self.dict_adj.keys():
            self.ajouter_sommet(s1)
        if not s2 in self.dict_adj.keys():
            self.ajouter_sommet(s2)
        # Ajout du sommet s2 dans la liste des 
        # sommets adjacents au sommet s1 dans le dictionnaire d'adjacences
        self.dict_adj[s1].append(s2)
        # Ajout du sommet s1 dans la liste des 
        # sommets adjacents au sommet s2 dans le dictionnaire d'adjacences
        # si le graphe n'est pas orienté
        if not self.oriente:
            self.dict_adj[s2].append(s1)
            
    
    def parcours_profondeur(self, s_depart, visite = None):
        '''
        Méthode qui renvoie une liste des clés des sommets correspondants à un
        parcours en profondeur du graphe à partir du sommet s_depart
        Le nom anglais est DFS pour depth-first search
        '''

        # Si visite vaut None, on affecte une liste vide à visite
        if visite is None:
            visite = []

        # On vérifie que le sommet s_depart existe dans le graphe
        if not s_depart in visite:
            # Si le sommet de départ n’est pas visité, on l’ajoute au tableau visite
            visite.append(s_depart)
        
        # Pour chaque nœud s adjacent au sommet s_depart
        for noeud in self.dict_adj[s_depart]:
            # Si s n'a pas été visité, on fait un parcours en profondeur à partir de s
            if not noeud in visite:
                self.parcours_profondeur(noeud, visite) 
            
        return visite
    
    def parcours_profondeur_iter(self, s_depart):
        '''
        Méthode qui renvoie une liste des clés des sommets correspondants à un
        parcours en profondeur d'abord du graphe à partir du sommet s_depart
        Le nom anglais est DFS pour depth-first search
        '''
        # On vérifie que le sommet s_depart existe dans le graphe
        if s_depart not in self.dict_adj:
            return []
        
        # On initialise la liste des nœuds visités visite à [].
        visite = []
        
        # On initialise la pile utilisée à [s_depart].
        p = Pile()
        p.empiler(s_depart)
        
        # Tant que pile n’est pas vide, on dépile p.
        while not p.est_vide():
            # Le nœud récupéré est s
            s = p.depiler()
            
            # Si s n’a pas été visité, alors on l’ajoute au tableau visite
            if s not in visite:
                visite.append(s)
                
                # On ajoute à la pile tous les nœuds adjacents au nœud s qui n’ont pas encore été visités
                # (rajouté par Raph) dans l'ordre inverse de leur apparition dans le dictionnaire d'adjacence
                for noeud in reversed(self.dict_adj[s]):
                    if noeud not in visite:
                        p.empiler(noeud)
        
        # On renvoie la liste visite qui contient le parcours
        return visite
    
    
    def parcours_largeur(self, s_depart):
        '''
        Méthode qui renvoie une liste des clés des sommets correspondants à un
        parcours en largeur d'abord du graphe à partir du sommet s_depart
        Le nom anglais est BFS pour breadth-first search
        '''
        # On vérifie que le sommet s_depart existe dans le graphe
        if s_depart not in self.dict_adj:
            return []
        
        # On initialise la liste des nœuds visités visite à [].
        visite = []

        # On initialise la file utilisée à [s_depart].
        f = File()
        f.enfiler(s_depart)
        
        # Tant que la file n’est pas vide, on défile la file.
        while not f.est_vide():
            # Le nœud récupéré est s
            s = f.defiler()
            
            # Si s n’a pas été visité, alors on l’ajoute au tableau visite
            if not s in visite:
                visite.append(s)
                
                # On ajoute à la file tous les nœuds adjacents au nœud s qui n’ont pas encore été visités
                for noeud in self.dict_adj[s]:
                    f.enfiler(noeud)
        
        # On renvoie la liste visite qui contient le parcours
        return visite


    def recherche_chemins(self, s_depart, s_fin):
        '''
        Méthode qui renvoie une liste des chemins possibles dans le graphe,
        à partir du sommet s_depart jusqu'au sommet s_fin
        '''
        # On vérifie que le sommet s_depart existe dans le graphe
        if s_depart not in self.dict_adj:
            return []

        # On vérifie que le sommet s_fin existe dans le graphe
        if s_fin not in self.dict_adj:
            return []

        # On initialise la file utilisée file à [(s_depart, [s_depart])]
        file = File()
        file.enfiler((s_depart, [s_depart]))

        # On initialise la liste des chemins à []
        chemins = []

        # Tant que file n’est pas vide, on défile file.
        while not file.est_vide():
            sommet, chemin = file.defiler()

            # Pour chaque voisin s de sommet qui n’est pas dans chemin
            for s in self.dict_adj[sommet]:
                if s not in chemin:
                    # si s est le nœud final s_fin, alors on a ajoute le chemin chemin+[s] au tableau chemins.
                    if s == s_fin:
                        chemins.append(chemin + [s])
                    else:
                        # sinon, on ajoute à la file le tuple (s,chemin+[s])
                        file.enfiler((s, chemin + [s]))

        # On renvoie la liste des chemins possibles entre s_depart et s_fin
        return chemins

    def presence_chemin(self,s_depart,s_fin):
        '''
        Prédicat qui indique si au moins un chemin existe dans le graphe
        à partir du sommet s_depart jusqu'au sommet s_fin
        '''
        # On se base sur le résultat de la recherche des chemins de s_depart à s_fin
        if len(self.recherche_chemins(s_depart, s_fin)) == 0:
            return False
        return True

    def recherche_cycles(self, s_depart):
        '''
        Méthode qui renvoie une liste des cycles possibles dans le graphe,
        à partir du sommet s_depart
        '''
        # On vérifie que le sommet s_depart existe dans le graphe
        if s_depart not in self.dict_adj:
            return []

        # On initialise la file utilisée file à [(s_depart, [s_depart])]
        file = File()
        file.enfiler((s_depart, [s_depart]))

        # On initialise la liste des cycles à []
        cycles = []

        # Tant que file n’est pas vide, on défile file.
        while not file.est_vide():
            sommet, chemin = file.defiler()

            # Pour chaque voisin s de sommet
            for s in self.dict_adj[sommet]:
                # Si s n’est pas dans chemin ou si s est le sommet de départ
                if s not in chemin or s == s_depart:
                    # si s est le nœud initial s_depart, alors on a ajoute le chemin chemin+[s] à la liste cycles.
                    if s == s_depart:
                        cycles.append(chemin + [s])
                    else:
                        # sinon, on ajoute à la file le tuple (s,chemin+[s])
                        file.enfiler((s, chemin + [s]))

        # On renvoie la liste des cycles possibles depuis s_depart
        return cycles
    
    
    def presence_cycle(self,s_depart):
        '''
        Prédicat qui indique si au moins un cycle existe dans le graphe
        à partir du sommet s_depart
        '''
        # On se base sur le résultat de la recherche des cycles à partir de s_depart
        if len(self.recherche_cycles(s_depart)) == 0:
            return False
        return True   

g=Graphe()
print(g.recherche_chemins('A1','C1'))

    
