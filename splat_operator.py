# Le Splat Operator (*) en Python permet de collecter 
# plusieurs éléments d'une séquence (liste, tuple, etc.) 
# dans une variable. Cela donne une grande flexibilité 
# pour travailler avec des séquences de longueur variable.

# 1. Décomposition de Séquences avec * (splat operator) en Python
*head, tail = [1,2,3,4,5]
print(head)
print(tail)

# 2. Traitement de Colonnes dans un DataFrame (Pandas)
import pandas as pd

# Exemple de DataFrame
df = pd.DataFrame({
    "ID": [1, 2, 3],
    "Feature1": [10, 20, 30],
    "Feature2": [0.5, 0.7, 0.8],
    "Feature3": [100, 200, 300]
})
id_col, *features = df.columns
print(id_col)
print(features)

feature_data = df[features]
print(feature_data)

# 3. Gestion d'Arguments Variables dans des Fonctions
def process_scores(student_name, *scores):
    print(f"Etudiant : {student_name}")
    print(f"Scores : {scores}")
    moyenne = sum(scores)/len(scores) if scores else 0
    print(f"Moyenne : {moyenne:.2f}")

process_scores("Josh", 18, 15, 12, 14)
process_scores("Melissa", 20, 19)

# 4. Segmentation des Données en Entraînement et Test
data = [1,2,3,4,5,6,7,8,9,10]
*train, test = data
print("train:", train)
print("test:", test)

