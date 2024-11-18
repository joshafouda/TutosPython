# Déclaration "in" permet de vérifier si un élément existe dans 
# une séquence (comme une liste, un tuple, une chaîne de caractères, 
# un dictionnaire, etc.) ou même de parcourir une séquence dans des boucles.

# 1.  Vérification de l'existence d'un élément
fruits = ["pomme", "banane", "cerise"]
print("pomme" in fruits) # True
print("orange" in fruits)

# 2. Utilisation dans une boucle for
for fruit in fruits:
    print(fruit)

# 3. Avec des ensembles (sets)

nombres = {1,2,3,4,5}
print(3 in nombres)
print(0 in nombres)

# 4. Avec des compréhensions
nombres_list = [1,2,3,4,5]
pairs = [x for x in nombres_list if x % 2 == 0]
print(pairs)

# 5. Dans une structure if
fruits = ["pomme", "banane", "cerise"]
if "orangee" in fruits:
    print("L'orange est dans la liste des fruits")
else:
    print("L'orange n'est pas dans la liste des fruits")