import numpy as np


def KNN_algo(X_train, y_train, X_test, k):
    # Calculate the Euclidean distance between each test point and all training points
    distances = np.sqrt(((X_test[:, np.newaxis] - X_train) ** 2).sum(axis=2))
    
    # Get the indices of the k nearest neighbors
    nearest_neighbors_indices = np.argsort(distances, axis=1)[:, :k]
    
    # Get the labels of the k nearest neighbors
    nearest_neighbors_labels = y_train[nearest_neighbors_indices]
    
    # Predict the label by taking the most common label among the nearest neighbors
    from scipy.stats import mode
    predictions = mode(nearest_neighbors_labels, axis=1)[0].flatten()
    
    return predictions

'''2. Coder l'évaluation : La précision de prédictions '''
def accuracy(y_true, y_pred):
    return (y_true == y_pred).mean() * 100

'''3. Testez votre code avec k=2 et quelle est la précision de l'algorithm KNN ?'''
# Load the data
import pandas as pd
data = pd.read_csv("data/titanic/train.csv")
