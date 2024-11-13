import random

class JeuDeCartes:
    def __init__(self):
        valeurs = range(13)
        couleurs = range(4)
        self.cartes = [(v, c) for c in couleurs for v in valeurs]

jeux = JeuDeCartes()
print(jeux.cartes)