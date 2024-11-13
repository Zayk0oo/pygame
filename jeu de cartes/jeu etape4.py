import random

class JeuDeCartes:
    def __init__(self):
        valeurs = range(13)
        couleurs = range(4)
        self.cartes = [(v, c) for c in couleurs for v in valeurs]

    def nomCarte(self, c):
        valeur, couleur = c
        noms_valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        noms_couleurs = ["Pique", "Trèfle", "Carreau", "Coeur"]
        return f"{noms_valeurs[valeur]} de {noms_couleurs[couleur]}"
    
    def battre(self):
        random.shuffle(self.cartes)

    def tirer(self):
        if self.cartes:
            return self.cartes.pop(0)
        else:
            return None

jeux = JeuDeCartes()
jeux.battre()
"""
print(jeux.cartes)
c = jeux.tirer()
print(jeux.nomCarte(c))
print()
print(jeux.cartes)
"""

for n in range(53):
    c = jeux.tirer()
    if c:
        print(jeux.nomCarte(c))
    else:
        print("Plus de cartes")