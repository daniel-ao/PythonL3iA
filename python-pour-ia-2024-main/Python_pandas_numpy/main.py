import pandas as pd
import numpy as np
import KNN

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = pd.read_csv("data/titanic/train.csv")
    print("Succès : Lecture des données")



    # Prétraitement des données
    # 1. Remplacer les colonnes Sex et Embarked par des codes de catégories
    # 2. Remplir les âges manquants avec la valeur moyenne
    # 3. Supprimer les colonnes Tickets, Name, Cabin et PassengerId
    # 4. Afficher la matrice de corrélation et vérifier quelles caractéristiques influencent le plus la variable Survived

    # Prenez les 80 % premières lignes avec toutes les colonnes sauf Survived et convertissez-les en tableau numpy, nommé X_train
    # Prenez les 80 % premières lignes de la colonne Survived et convertissez-les en tableau numpy, nommé y_train

    # Prenez les 20 % dernières lignes avec toutes les colonnes sauf Survived et convertissez-les en tableau numpy, nommé X_test
    # Prenez les 20 % dernières lignes de la colonne Survived et convertissez-les en tableau numpy, nommé y_test

    # Implémentez la fonction KNN_algo et obtenez y_prediction

    # Évaluez la précision de KNN_algo (la distance entre y_prediction et y_test)


