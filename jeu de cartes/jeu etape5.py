import random

class JeuDeCartes:
    def __init__(self):
        valeurs = range(13)
        couleurs = range(4)
        self.cartes = [(v, c) for c in couleurs for v in valeurs]

    def nom_carte(self, carte):
        valeur, couleur = carte
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

def bataille():
    jeuA = JeuDeCartes()
    jeuB = JeuDeCartes()
    jeuA.battre()
    jeuB.battre()

    comptA = 0
    comptB = 0

    while jeuA.cartes and jeuB.cartes:
        carteA = jeuA.tirer()
        carteB = jeuB.tirer()

        if carteA[0] > carteB[0]:
            comptA += 1
        elif carteA[0] < carteB[0]:
            comptB += 1

    print("Score :")
    print(f"Joueur A = {comptA} -------- Joueur B = {comptB}")

if __name__ == "__main__":
    bataille()