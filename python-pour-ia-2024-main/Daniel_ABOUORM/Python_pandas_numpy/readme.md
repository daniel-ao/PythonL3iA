# TP Python

## Etapes premilinaires

Télécharger ce dossier
Activate l'environnement utilisé dans le cours précédent
Installer les packages suivants (s'ils ne sont pas installées) :
```bash
conda install numpy
conda install pandas 
```
Tester le code avec
```
 python .\main.py 
```

# Exercices:
## Familiarisez-vous avec votre jeu de données : [Détails des donnée](https://www.kaggle.com/competitions/titanic/data)
### A l'aide du pandas, répondre les questions suivantes:


1. Quelle est la taille du jeu de données (combien de lignes et de colonnes) ?
2. Affichez le nom de toutes les colonnes
3. Affichez les dix premières lignes
4. Vérifiez le tarif le plus élevé
5. Combien de passagers ont plus de 60 ans ?
6. Combien de personnes ont entre 30 et 40 ans ?
7. Quel est le pourcentage de personnes ayant survécu ?
8. Quel est le pourcentage de femmes et d'hommes ayant survécu ?
9. Quel est le taux de survie pour chaque classe (Pclass) ?
10. Afficher la matrice de corrélation et vérifier quelles caractéristiques influencent le plus la variable Survived


## Prétraitement des données
1. Remplacer les colonnes Sex et Embarked par des codes de catégories
2. Remplir les âges manquants avec la valeur moyenne
3. Supprimer les colonnes Tickets, Name, Cabin et PassengerId
4. Prenez les 80 % premières lignes avec toutes les colonnes sauf Survived et convertissez-les en tableau numpy, nommé X_train
5. Prenez les 80 % premières lignes de la colonne Survived et convertissez-les en tableau numpy, nommé y_train
6. Prenez les 20 % dernières lignes avec toutes les colonnes sauf Survived et convertissez-les en tableau numpy, nommé X_test
7. Prenez les 20 % dernières lignes de la colonne Survived et convertissez-les en tableau numpy, nommé y_test


## Numpy pour KNN
### A l'aide du numpy, coder l'algorithme suivant: 
L’algorithme des k plus proches voisins s'écrit en abrégé k-NN ou KNN , de l'anglais k-nearest
neighbors, appartient à la famille des algorithmes d’apprentissage automatique sans paramètres.
L’algorithme des k plus proches voisins est un algorithme d’apprentissage supervisé, il est
nécessaire d’avoir des données labellisées. À partir d’un ensemble E de données labellisées (données d'entraînement), il sera
possible de classer (déterminer le label) d’une nouvelle ensemble de donnée T (donnée n’appartenant pas à E, données de teste).

### Principe de algorithme
On suppose que l'ensemble E contiennent n données labellisées et T, une autre ensemble des données
disjointe de E qui ne possède pas de label. Soit d une fonction qui renvoie la distance
(qui reste à choisir) entre la donnée u de T et une donnée quelconque appartenant à E. Soit un entier k
inférieur ou égal à n.
Le principe de l’algorithme de k-plus proches voisins est le suivant :

Pour chaque donnée u dans T:
* On calcule les distances (par exemple Euclidean) entre la donnée u et chaque donnée appartenant à E.
* On retient les k données du jeu de données E les plus proches de u.
* On attribue à u la classe qui est la plus fréquente parmi les k données les plus proches.

# A faire

1. Coder l'algorithme KNN à l'aide de Numpy

    Remplir la fonction KNN_algo dans le fichier KNN.py. La fonction va retourner les prédictions pour T

    **Remarque** : Essayer de coder de façon avec moins de boucle (for), rappelle que numpy nous permet de faire les calculs terme à terme.

2. Coder l'évaluation : La précision de prédictions 

3. Testez votre code avec k=2 et quelle est la précision de l'algorithm KNN ?


4. Modifier la valeur de k (et retester. Quelle est votre observation sur effect de k ?
