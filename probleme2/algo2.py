#!/usr/local/bin/python3

# -*- coding: utf-8 -*-
import sys
from math import sqrt


# On définit une classe pour les points

class Point:
    x = 0
    y = 0

    def __init__(self, u, v):
        self.x = u
        self.y = v

    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def __str__(self):
        return "Point"

    def distance(self, autre):
        diff_x = self.x-autre.x
        diff_y = self.y-autre.y
        return sqrt(diff_x**2+diff_y**2)

    def cmp_x(self, autre):
        return (self.x < autre.x)

    def cmp_y(self, autre):
        return (self.y < autre.y)


# Fonctions de recherche de distance minimale.
# Le deuxième algorithme est à implémenter
#      Algorithme naïf quadratique
"""
    Du coup on retrouve une complexité en O(n^2) quadratic car on parcourt deux fois la liste et on peut voir ceci sur le graphique dans le dossier graph fichier algoNaiveGraph.png        
"""


def distance_min_naive(L):
    if len(L) < 2:
        print("Il doit y avoir au moins deux points.")
        return 0
    else:
        daux = L[0].distance(L[1])
        for indA, a in enumerate(L):
            for indB, b in enumerate(L):
                if indA < indB:
                    if a.distance(b) < daux:
                        daux = a.distance(b)
        return daux

#      Algorithme amélioré vu en cours


"""
    Trouve la distance minimale entre deux points dans la liste 'L' en utilisant l'algorithme de la distance minimale.

    Args:
    L (list of Point): Une liste de points.

    Returns:
    float: La distance minimale entre deux points.
    
    
    Reponse au question:
    - Tester la vitesse d'exécution de votre algorithme sur des listes de points de plus en plus rapides.
    - la compléxité est x *  log(x) * log(x)  pour cette fonction
"""


def distance_min_dpr(L):
    n = len(L)

    # Si moins de 2 points, la distance minimale est infinie
    if n < 2:
        return float('inf')

    # Si 2 points, calculer leur distance
    if n == 2:
        return L[0].distance(L[1])

    # Trier les points selon leurs coordonnées x
    L.sort(key=lambda point: point.x)

    # Division du tableau en deux parties
    mid = n // 2
    L_left = L[:mid]
    L_right = L[mid:]

    # Récursion pour les deux moitiés
    d_left = distance_min_dpr(L_left)
    d_right = distance_min_dpr(L_right)

    # Trouver la distance minimale entre les deux moitiés
    d_min = min(d_left, d_right)

    # Trouver les points proches de la ligne de séparation
    strip = [point for point in L if abs(point.x - L[mid].x) < d_min]

    # Trier les points proches par coordonnée y
    strip.sort(key=lambda point: point.y)

    # Trouver la distance minimale dans la bande
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j].y - strip[i].y < d_min:
                dist = strip[i].distance(strip[j])
                d_min = min(d_min, dist)

    return d_min


"""
Derniere question : 
first algo : (10^8)^2 = 1e+16
second algo : (10^8) * log(10^8) * log(10^8) =  6400000000
Nombre d'étapes de calcule

mon processeur fait : 2500000000 operations par seconde 
on a 1e+16 / 2500000000 = 4000000 pour le premier algo mais on a des pertes donc on fait * 100 = 400000000 secondes
on a 6400000000 / 2500000000 = 2.56 secondes pour le second algo mais on a des pertes donc on fait * 100 = 256 secondes
"""

# Fonction mère (normalement il n'y a pas à modifier la suite)

#  Aide indiquant comment utiliser notre fonction


def usage(nom):
    print("Usage : " + nom + " METHODE file")
    print("  Importe un fichier file listant un ensemble de points dans")
    print("  le plan puis détermine la distance minimum entre deux de")
    print("  ces points.")
    print("  Valeurs valides pour METHODE :")
    print("  - naive -          Double boucle en O(n^2)")
    print("  - dpr -            Méthode diviser-pour-régner ")
    print("                       (algorithme à implémenter))")
    print("  - naive_muette -   comme naive mais sans sortie")
    print("  - dpr_muette -     comme dpr mais sans sortie")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Ce programme nécessite une méthode et un fichier en arguments.")
        usage(sys.argv[0])
        exit(1)

    mute = 0

    if sys.argv[1] == "naive":
        print("# [Méthode naïve]")
        fctDistMin = distance_min_naive
    elif sys.argv[1] == "naive_muette":
        fctDistMin = distance_min_naive
        mute = 1
    elif sys.argv[1] == "dpr":
        print("# [Méthode diviser-pour-régner]")
        fctDistMin = distance_min_dpr
    elif sys.argv[1] == "dpr_muette":
        fctDistMin = distance_min_dpr
        mute = 1
    else:
        print("Cette méthode n'existe pas.")
        usage(sys.argv[0])
        exit(1)

    filename = sys.argv[2]
    tab = []
    file = open(filename, "r")
    try:
        next(file)
        for line in file:
            CoupPoints = line.split()
            tab.append(Point(int(CoupPoints[0]), int(CoupPoints[1])))
    finally:
        file.close()
    if mute == 0:
        print("input : ", end="")
        print(tab)

    # Si besoin, on peut augmenter le nombre de récursions possible pour les méthodes récursives
        # sys.setrecursionlimit(10 ** 6)
        # resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))

    val = fctDistMin(tab)
    if mute == 0:
        print(val)
