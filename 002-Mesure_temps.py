# Mesurer le temps d'exécution d'une séquence de code
# From: https://www.pythoniaformation.com/blog/tutoriels-python-par-categories/projet-debutant-python-supercool/range-python

# Analyse des Performances de range
# Efficacité en mémoire : range est conçu pour être économique en mémoire, en particulier dans Python 3, où il ne génère
# les nombres qu'à la demande (lazy evaluation).Vitesse d'exécution : bien que généralement rapide, l'utilisation de
# range dans des boucles très imbriquées ou avec de grands pas peut affecter les performances. Il est essentiel de
# profiler votre code pour identifier les goulots d'étranglement.
#
# Immutabilité : range produit des séquences immuables. Si vous avez besoin d'une séquence modifiable, vous devrez
# convertir le résultat en une liste ou une autre structure de données mutable.Limitation aux entiers : range ne
# fonctionne qu'avec des nombres entiers. Pour des itérations nécessitant des flottants ou d'autres types de données,
# vous devrez chercher des alternatives.Utilisation avec prudence dans les grandes boucles :
# bien que range soit efficace, l'utilisation de grandes valeurs dans range peut conduire à des itérations longues
# et potentiellement inefficaces.

import time

# Mesurer le temps pour range
start_time = time.time()
for i in range(1000000):
    pass
end_time = time.time()
print(f"Temps d'exécution avec range: {end_time - start_time} secondes")
print(f"-------------------------------------------------------------- ")

# Mesurer le temps pour la compréhension de liste
start_time = time.time()
liste = [i for i in range(1000000)]
end_time = time.time()
print(f"Temps d'exécution avec compréhension de liste: {end_time - start_time} secondes")

liste = ['a', 'b', 'c', 'd'] * 250000

# Mesurer le temps pour range
start_time = time.time()
for i in range(len(liste)):
    _ = liste[i]
end_time = time.time()
print(f"Temps d'exécution avec range: {end_time - start_time} secondes")

# Mesurer le temps pour enumerate
start_time = time.time()
for i, val in enumerate(liste):
    _ = val
end_time = time.time()
print(f"Temps d'exécution avec enumerate: {end_time - start_time} secondes")

# range dans les Boucles vs Itérateurs/Générateurs :
# Les itérateurs et les générateurs offrent plus de flexibilité et peuvent être plus efficaces pour itérer sur des
# séquences complexes, mais range reste un choix solide pour les séquences numériques simples et la répétition
# d'opérations.

# Mesurer le temps pour range
start_time = time.time()
for i in range(1000000):
    pass
end_time = time.time()
print(f"Temps d'exécution avec range: {end_time - start_time} secondes")

# Mesurer le temps pour un générateur
def compteur(max):
    n = 0
    while n < max:
        yield n
        n += 1

start_time = time.time()
for i in compteur(1000000):
    pass
end_time = time.time()
print(f"Temps d'exécution avec générateur: {end_time - start_time} secondes")