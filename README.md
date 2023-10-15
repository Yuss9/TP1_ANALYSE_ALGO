
# ANALYSE ALGORITHME TP1
Nous retrouvons dans ce repo les trois problèmes du TP1.


**Dans le fichier "documentation.pdf," vous trouverez toutes les réponses du TP1.**

Entrer dans les codes sources : 
```bash
cd src
```


## Authors

- [@Yuss9](https://github.com/Yuss9) (Full stack)

## INSTALLATION

### PROBLEME 1
Dans le dossier "graphs," vous trouverez tous les graphes pour chaque fonction.

Vous pouvez également modifier le fichier "testData.json."

Pour choisir la fonction que vous souhaitez tester, il faut commenter celle que vous utilisez actuellement et décommenter celle que vous souhaitez utiliser, à partir de la ligne 183 jusqu'à la ligne 187.

On entre dans le projet : 

```bash
cd probleme1
```

Generer des 20 nombres : 

```bash
python3 genererNombres.py 20
```

Lancer le problème 1 (sans graphe) : 

```bash
python3 algo1.py integersList_20
```

Lancer le problème 1 (avec graphe) : 

```bash
python3 graphChronoGenerator.py
```


### PROBLEME 2

Dans le dossier "graphs," vous trouverez tous les graphes pour chaque fonction.

Vous pouvez également modifier le fichier "testData.json" si vous souhaitez exécuter les fonctions avec les graphes.

On entre dans le problème 2 : 

```bash
cd probleme2
```

Générer une liste de 20 points : 
```bash
python3 generatePoint.py 20
```

Lancer le programme avec la fonction naive : 

```bash
python3 algo2.py naive pointsListe_20 
```

Lancer le programme avec la fonction dpr : 

```bash
python3 algo2.py dpr pointsListe_20 
```

Lancer le programme avec graphe (attention on modifie dans le testData.json): 

```bash
python3 graphChronoGenerator.py 
```



### PROBLEME 3
Vous pouvez également modifier le fichier "testData.json" si vous souhaitez exécuter les fonctions avec les graphes.

Dans le programme actuel "algo3," vous disposez du temps d'exécution pour chaque fonction (optimisée et non optimisée).

Pour générer un graphe, vous devez commenter soit les lignes de 54 à 62 pour utiliser l'algorithme dynamique, sinon, commentez les lignes de 64 à 72.

On entre dans le problème 2 : 

```bash
cd probleme3
```

Générer une game : 
```bash
python3 generateGame.py 20
```

Lancer le programme pour avoir le timing des deux algos: 

```bash
python3 algo3.py integersList_20 
```

## Tech Stack

**Server:** Python


