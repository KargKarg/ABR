

class Noeud:

    def __init__(self, valeur, gauche=None, droite=None, descendants = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
        self.descendants = descendants


    def insert(self, value):
        """Insère la valeur dans l'ABR"""

        if self.gauche == None and value <= self.valeur:
            self.gauche = Noeud(value)

        elif self.droite == None and value > self.valeur:
            self.droite = Noeud(value)

        elif value >  self.valeur:
            return self.droite.insert(value)

        elif value <= self.valeur:
            return self.gauche.insert(value)


    def recherche(self, value):
        """Recherche la valeur dans l'ABR et renvoie le parcours de recherche"""

        if value == self.valeur:
            return f"<= C'est le chemin de recherche, {value} est dans l'ABR"

        elif self.gauche == None and self.droite == None:
            return f"<= C'est le chemin de recherche, {value} n'est pas dans l'ABR"

        elif self.gauche == None and self.droite != None:

            if value <= self.valeur:
                return f"<= C'est le chemin de recherche, {value} n'est pas dans l'ABR"

            elif value > self.valeur:
                return "Droite " + self.droite.recherche(value)

        elif self.droite == None and self.gauche != None:

            if value > self.valeur:
                return f"<= C'est le chemin de recherche, {value} n'est pas dans l'ABR"

            elif value <= self.valeur:
                return "Gauche " + self.gauche.recherche(value)

        elif value > self.valeur:
            return "Droite " + self.droite.recherche(value)

        elif value <= self.valeur:
            return "Gauche " + self.gauche.recherche(value)



    def taille(self):
        """Renvoie la taille de l'ABR soit son nombre de noeud"""

        if self.gauche == None and self.droite == None:
            return 1

        elif self.gauche == None and self.droite != None:
            return 1 + self.droite.taille()

        elif self.gauche != None and self.droite == None:
            return 1 + self.gauche.taille()

        else:
            return 1 + self.gauche.taille() + self.droite.taille()

    def nombre_feuille(self):
        """Renvoie son nombre de feuille soit des noeuds sans enfant"""

        if self.gauche == None and self.droite == None:
            return 1

        elif self.gauche == None and self.droite != None:
            return 0 + self.droite.nombre_feuille()

        elif self.gauche != None and self.droite == None:
            return 0 + self.gauche.nombre_feuille()

        else:
            return 0 + self.gauche.nombre_feuille() + self.droite.nombre_feuille()


    def est_ABR(self):
        """Renvoie vrai si l'arbre est un ABR"""

        if self.gauche == None and self.droite == None:
            return True

        elif self.gauche == None and self.droite != None:

            if self.droite.valeur <= self.valeur:
                return False

            else:
                return True and self.droite.est_ABR()

        elif self.gauche != None and self.droite == None:

            if self.gauche.valeur > self.valeur:
                return False

            else:
                return True and self.gauche.est_ABR()

        elif self.gauche != None and self.droite != None:

            if self.gauche.valeur <= self.valeur and self.droite.valeur > self.valeur:
                return True and self.gauche.est_ABR() and self.droite.est_ABR()
            else:
                return False

    def compte_descendants(self):
        """Calcul est stock le nombre de descendant de chaque noeud"""

        if self.gauche == None and self.droite == None:
            return

        elif self.gauche != None and self.droite == None:
            self.descendants = self.gauche.taille()
            self.gauche.compte_descendants()

        elif self.gauche == None and self.droite != None:
            self.descendants = self.droite.taille()
            self.droite.compte_descendants()

        else:
            self.descendants = self.gauche.taille() + self.droite.taille()
            self.gauche.compte_descendants()
            self.droite.compte_descendants()

    def un_fils(self):
        """Renvoie le nombre de noeud possédant un fils dans l'ABR"""

        if self.gauche == None and self.droite == None:
            return 0

        elif self.gauche != None and self.droite == None:
            return 1 + self.gauche.un_fils()

        elif self.gauche == None and self.droite != None:
            return 1 + self.droite.un_fils()

        else:
            return 0 + self.gauche.un_fils() + self.droite.un_fils()

    def deux_fils(self):
        """Renvoie le nombre de noeud intérieur soit le nombre de noeud à deux fils"""

        return self.taille() - self.nombre_feuille() - self.un_fils()

