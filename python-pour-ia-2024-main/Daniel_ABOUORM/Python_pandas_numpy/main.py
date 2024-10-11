import pandas as pd
import numpy as np
import KNN as KN


if __name__ == '__main__':
    data = pd.read_csv("data/titanic/train.csv")
    print("Succès : Lecture des données")

'''1. Quelle est la taille du jeu de données (combien de lignes et de colonnes) ?'''
print("Taille du jeu de données : ", data.shape)
'''2. Affichez le nom de toutes les colonnes'''
print("Nom de toutes les colonnes : ", data.columns)
'''3. Affichez les dix premières lignes'''
print("Dix premières lignes : ", data.head(10))
'''4. Vérifiez le tarif le plus élevé'''
print("Tarif le plus élevé : ", data['Fare'].max())
'''5. Combien de passagers ont plus de 60 ans ?'''
print("Nombre de passagers de plus de 60 ans : ", data[data['Age'] > 60].shape[0])
'''6. Combien de personnes ont entre 30 et 40 ans ?'''
print("Nombre de personnes entre 30 et 40 ans : ", data[(data['Age'] >= 30) & (data['Age'] <= 40)].shape[0])
'''7. Quel est le pourcentage de personnes ayant survécu ?'''
print("Pourcentage de personnes ayant survécu : ", data['Survived'].mean()*100)
'''8. Quel est le pourcentage de femmes et d'hommes ayant survécu ?'''
survival_by_gender = data.groupby('Sex')['Survived'].mean() * 100
print("Pourcentage de femmes ayant survécu : ", survival_by_gender['female'])
print("Pourcentage d'hommes ayant survécu : ", survival_by_gender['male'])
'''9. Quel est le taux de survie pour chaque classe (Pclass) ?'''
survival_by_class = data.groupby('Pclass')['Survived'].mean() * 100
print("Taux de survie pour chaque classe : ")
print(survival_by_class)

# 10 is done at the end of the code #

## Prétraitement des données

# 1. Remplacer les colonnes Sex et Embarked par des codes de catégories
data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Remplir les valeurs manquantes restantesavec un espace réservé
data['Embarked'].fillna(-1, inplace=True)

# Convertir Embarked en type entier
data['Embarked'] = data['Embarked'].astype(int)

############################

data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Sex'].fillna(-1, inplace=True) 
data['Sex'] = pd.to_numeric(data['Sex'], errors='coerce')

############################

# 2. Remplir les âges manquants avec la valeur moyenne
data['Age'].fillna(data['Age'].mean(), inplace=True)

# 3. Supprimer les colonnes Tickets, Name, Cabin et PassengerId
data.drop(columns=['Ticket', 'Name', 'Cabin', 'PassengerId'], inplace=True)

# 4. Prenez les 80 % premières lignes avec toutes les colonnes sauf Survived et convertissez-les en tableau numpy, nommé X_train
train_size = int(0.8 * len(data))
X_train = data.iloc[:train_size].drop(columns=['Survived']).to_numpy()

# 5. Prenez les 80 % premières lignes de la colonne Survived et convertissez-les en tableau numpy, nommé y_train
y_train = data.iloc[:train_size]['Survived'].to_numpy()

# 6. Prenez les 20 % dernières lignes avec toutes les colonnes sauf Survived et convertissez-les en tableau numpy, nommé X_test
X_test = data.iloc[train_size:].drop(columns=['Survived']).to_numpy()

# 7. Prenez les 20 % dernières lignes de la colonne Survived et convertissez-les en tableau numpy, nommé y_test
y_test = data.iloc[train_size:]['Survived'].to_numpy()


'''10. Afficher la matrice de corrélation et vérifier quelles caractéristiques influencent le plus la variable Survived'''
numeric_data = data.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()
print("Matrice de corrélation : ")
print(correlation_matrix)


# A Faire
# 3. Testing the KNN algorithm with k=2

k = 2
predictions_k2 = KN.KNN_algo(X_train, y_train, X_test, k)
accuracy_k2 = KN.accuracy(y_test, predictions_k2)
print(accuracy_k2)

print("\n")
# 4. Test for different values of k
k_values = range(1, 20)
accuracy_results = {k: KN.accuracy(y_test, KN.KNN_algo(X_train, y_train, X_test, k)) for k in k_values}

for k, acc in accuracy_results.items():
    print(f"k = {k}, Accuracy = {acc:.2f}%")

print("\n")

Conclusion = """L'observation des résultats montre que :

- **Petits k (k=1 à k=3)** : Avec des petites valeurs de k, le modèle est plus sensible au bruit et aux variations locales. L'accuracy augmente légèrement au fur et à mesure que k augmente.
  
- **Valeurs moyennes de k (k=4 à k=7)** : L'accuracy atteint son maximum à k=7 (**77.09%**). Cela montre que cette valeur offre un bon équilibre entre la capture des tendances locales et la réduction du bruit.

- **Grandes valeurs de k (k=8 à k=10)** : Au-delà de k=7, l'accuracy commence à diminuer légèrement, ce qui indique que des valeurs de k plus élevées rendent les prédictions plus généralisées et moins précises pour les cas spécifiques.

En résumé, **k=7** semble être la meilleure valeur pour ce modèle, offrant une bonne stabilité et précision. \n"""

print(Conclusion)