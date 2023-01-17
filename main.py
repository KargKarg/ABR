from noeud import Noeud
import random

Racine = Noeud(100)

Racine.insert(307)

#Racine.gauche = Noeud(101) # à utiliser pour que est_ABR() == False

for i in range(98):
    num = random.randint(1,1000)
    Racine.insert(num)

Racine.compte_descendants()

print(f"Membre gauche de la racine : {Racine.gauche.valeur}")

print(f"Membre droit de la racine : {Racine.droite.valeur}")

print(f"Recherche de l'élèment 307 dans l'arbre : {Racine.recherche(307)}")

print(f"La taille de l'arbre est de : {Racine.taille()}")

print(f"Pour vérifier si l'arbre est ABR : {Racine.est_ABR()}")

print(f"Le nombre de descendant de 100 est : {Racine.descendants}, pour {Racine.droite.valeur} : {Racine.droite.descendants}"
      f" et pour {Racine.gauche.valeur} c'est : {Racine.gauche.descendants}")

print(f"Le nombre de feuille de l'arbre est de : {Racine.nombre_feuille()}")

print(f"Le nombre de noeud possédant exactement un fils est : {Racine.un_fils()}")

print(f"Le nombre de noeud possédant exactement deux fils est : {Racine.deux_fils()}")


