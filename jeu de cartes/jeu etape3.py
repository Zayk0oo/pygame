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

jeux = JeuDeCartes()
jeux.battre()
print(jeux.cartes)