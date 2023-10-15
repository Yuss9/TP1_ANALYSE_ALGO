from math import inf
import sys
import time


def sommeMin(t, n):
    return sommeMinRec(t, n)


def sommeMinRec(t, i):
    if i == 0:
        return 0

    opt = inf
    for x in [1, 3, 5]:
        if x <= i:
            tmp = t[i] + sommeMinRec(t, i - x)
            if tmp < opt:
                opt = tmp

    return opt


def sommeMinDynamique(t, n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for x in [1, 3, 5]:
            if i - x >= 0:
                tmp = t[i] + dp[i - x]
                dp[i] = min(dp[i], tmp)

    return dp[n]


def charger_plateau_de_jeu_de_fichier(nom_fichier):
    plateau = []
    with open(nom_fichier, 'r') as file:
        next(file)  # Ignore la première ligne
        for line in file:
            plateau.append(int(line.strip()))
    return plateau


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python nom_de_ce_script.py nom_du_fichier")
        sys.exit(1)

    nom_fichier = sys.argv[1]
    plateau = charger_plateau_de_jeu_de_fichier(nom_fichier)
    n = len(plateau) - 1

    start_time = time.time()
    resultat = sommeMin(plateau, n)
    end_time = time.time()

    print("Somme minimale pour atteindre la case", n,
          " avec l'algo pas optimiser :", resultat)
    print("Temps d'exécution (Algo pas optimiser):",
          end_time - start_time, "secondes")

    a = time.time()
    resultat = sommeMinDynamique(plateau, n)
    b = time.time()

    print("Somme minimale pour atteindre la case",
          n, " avec l'algo optimiser :", resultat)
    print("Temps d'exécution (Algo optimiser):",
          b - a, "secondes")
