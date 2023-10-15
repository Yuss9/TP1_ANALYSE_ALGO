#!/usr/local/bin/python3

# -*- coding: utf-8 -*-
import sys
from math import sqrt


# -----------------------   Votre algorithme   ------------------------------

#  L'argument l contient une liste d'entiers de taille n

""" def fctAlgo(l):
    '''
        À vous de jouer! 
    '''

    print("Pour l'instant l'algorithme ne fait pas grand chose...")
    print("... mais il est super rapide!")

    return 42  # En vrai, votre fonction n'a même pas besoin de retourner quelque chose

 """


"""
    Multiplie chaque élément de la liste l par le coefficient a.

    Args:
    l (list): La liste d'entiers d'entrée.
    Returns:
    list: Une nouvelle liste contenant les éléments de l multipliés par a.
    
    Linear function
    
"""


def fctLinear(l):
    a = 2
    resultat = [element * a for element in l]
    return resultat


"""
    Calcule la somme de toutes les paires possibles d'éléments de la liste l.

    Args:
    l (list): La liste d'entiers d'entrée.

    Returns:
    int: La somme des paires d'éléments.
"""


def fctQuadratic(l):
    somme = 0
    n = len(l)
    for i in range(n):
        for j in range(n):
            somme += l[i] + l[j]
    return somme


"""
    Calcule la somme de tous les produits possibles de triplets d'éléments de la liste l.

    Args:
    l (list): La liste d'entiers d'entrée.

    Returns:
    int: La somme des produits de triplets d'éléments.
"""


def fctCubic(l):
    somme = 0
    n = len(l)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                somme += l[i] * l[j] * l[k]
    return somme


"""
    Trie une liste d'entiers en utilisant l'algorithme de tri fusion (Merge Sort).
    
    Args:
    l (list): La liste d'entiers à trier.

    Returns:
    list: La liste triée dans l'ordre croissant.
"""


def fctPseudoLinear(l):
    if len(l) > 1:
        middle = len(l) // 2
        left_half = l[:middle]
        right_half = l[middle:]

        fctPseudoLinear(left_half)
        fctPseudoLinear(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l[k] = left_half[i]
                i += 1
            else:
                l[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            l[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            l[k] = right_half[j]
            j += 1
            k += 1
    return l


"""
    Génère toutes les permutations possibles de la liste l de manière récursive.

    Args:
    l (list): La liste d'éléments à permuter.

    Returns:
    list of list: Liste de toutes les permutations possibles.
"""


def fctExponentiel(l):
    if len(l) == 0:
        return [[]]
    subsets_without_first = fctExponentiel(l[1:])
    subsets_with_first = [[l[0]] +
                          subset for subset in subsets_without_first]
    return subsets_without_first + subsets_with_first

# -----  Fonction mère (normalement il n'y a pas à modifier la suite)  ------

#  Aide indiquant comment utiliser notre fonction


def usage(nom):
    print("Usage : " + nom + " file")
    print("  Importe un fichier file listant un ensemble d'entiers et")
    print("  applique votre algorithme sur cette liste d'entiers.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ce programme nécessite un fichier en argument.")
        usage(sys.argv[0])
        exit(1)

    verbose = True
    if len(sys.argv) >= 3 and sys.argv[1] == "--mute":
        verbose = False
        filename = sys.argv[2]
    else:
        filename = sys.argv[1]

    tab = []
    file = open(filename, "r")
    try:
        next(file)
        for line in file:
            tab.append(int(line))
    finally:
        file.close()
    if verbose:
        print("Input: ")
        print(tab)

    # val = fctLinear(tab)
    # val = fctQuadratic(tab)
    val = fctCubic(tab)
    # val = fctPseudoLinear(tab)
    # val = fctExponentiel(tab)

    if verbose:
        print("Output: ")
        print(val)
