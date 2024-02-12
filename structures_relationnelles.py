from structures_lineaires import Pile,File


class Graphe:
    ''' Définition de la classe Graphe constituée de 2 attributs :
        un dictionnaire d'adjacence et un booléen
        précisant si le graphe est orienté ou non
    '''
    def __init__(self,oriente=False):
        ''' Constructeur de la classe '''
        self.dict_adj={}
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

if __name__ == '__main__':
    g=Graphe()
    g.ajouter_arc('A','B')
    g.ajouter_arc('A','F')
    g.ajouter_arc('B','C')
    g.ajouter_arc('B','D')
    g.ajouter_arc('B','G')
    g.ajouter_arc('C','E')
    g.ajouter_arc('D','I')
    g.ajouter_arc('E','I')
    g.ajouter_arc('F','G')
    g.ajouter_arc('F','H')
    g.ajouter_arc('G','I')
    g.ajouter_arc('H','I')
    print(g.dict_adj)
    print("parcours en largeur :")
    for s in g.dict_adj.keys():
        print(g.parcours_largeur(s))
    print("parcours en profondeur :")
    for s in g.dict_adj.keys():
        print(g.parcours_profondeur(s))
    
    print("parcours en profondeur (itératif) :")
    for s in g.dict_adj.keys():
        print(g.parcours_profondeur_iter(s))
         
    print("""La liste des chemins de 'A' à 'D' est :""",g.recherche_chemins('A','D'))
    print("""La liste des chemins de 'A' à 'G' est :""",g.recherche_chemins('A','G'))
    print("""La liste des chemins de 'A' à 'I' est :""",g.recherche_chemins('A','I'))
    '''print("""L'un des chemins les plus courts de 'A' à 'I' est :""",g.trouve_plus_courte_chaine('A','I'))
    print("""L'un des chemins les plus courts de 'A' à 'G' est :""",g.trouve_plus_courte_chaine('A','G'))
    '''
        
    for s in g.dict_adj.keys():
        print("Présence de cycle(s) à partir du sommet ",s," : ",g.presence_cycle(s))
    
    print("""La liste des cycles à partir de 'A' est :""",g.recherche_cycles('A'))
    