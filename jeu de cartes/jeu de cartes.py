#Programme écris par LAMBERT Nolhan, TG5
#------------------------------------------------------------------------------------------------ 
import random
import pygame
import socket
import math
import tkinter as tk
from tkinter import simpledialog


class JeuDeCartes:
    def __init__(self):
        valeurs = range(13)
        couleurs = range(4)
        self.cartes = [(c, v) for c in couleurs for v in valeurs]
        self.battre()

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

def afficher_score(fenetre, score_joueur1, score_joueur2, gagnant=None):
    font_score = pygame.font.SysFont("Helvetica", 36, bold=True)
    
    couleur_score_normal = (255, 255, 255)
    couleur_score_clignotant = (255, 0, 0)
    
    couleur_joueur1 = couleur_score_clignotant if gagnant == "joueur1" else couleur_score_normal
    couleur_joueur2 = couleur_score_clignotant if gagnant == "joueur2" else couleur_score_normal
    
    score1_texte = font_score.render(f"Joueur 1 : {score_joueur1}", True, couleur_joueur1)
    score2_texte = font_score.render(f"Joueur 2 : {score_joueur2}", True, couleur_joueur2)
    
    fenetre.blit(score1_texte, (50, 20))
    fenetre.blit(score2_texte, (fenetre.get_width() - score2_texte.get_width() - 50, 20))

def animer_cartes(fenetre, fond, carteA, carteB, position_depart_A, position_depart_B, position_finale, cartes_images, vitesse_animation):
    temps = 0
    xA, yA = position_depart_A
    xB, yB = position_depart_B
    delta_x_A = (position_finale[0] - xA) / 100
    delta_y_A = (position_finale[1] - yA) / 100
    delta_x_B = (position_finale[0] - xB) / 100
    delta_y_B = (position_finale[1] - yB) / 100

    while temps < 100:
        fenetre.blit(fond, (0, 0))
        
        xA += delta_x_A
        yA += delta_y_A + 5 * math.sin(temps / 10)
        xB += delta_x_B
        yB += delta_y_B + 5 * math.sin(temps / 10)
        
        fenetre.blit(cartes_images[carteA], (xA, yA))
        fenetre.blit(cartes_images[carteB], (xB, yB))
        pygame.display.flip()
        
        pygame.time.delay(vitesse_animation)
        temps += 1

    fenetre.blit(fond, (0, 0))
    if carteA[1] > carteB[1]:
        carte_gagnante = carteA
        texte_gagnant = "Le joueur A repmporte le plis"
    else:
        carte_gagnante = carteB
        texte_gagnant = "Le joueur B remporte le plis"

    fenetre.blit(fond, (0, 0))
    fenetre.blit(cartes_images[carteA], position_finale)
    fenetre.blit(cartes_images[carteB], position_finale)
    fenetre.blit(cartes_images[carte_gagnante], position_finale)  

    font = pygame.font.SysFont("Helvetica", 48)
    texte = font.render(texte_gagnant, True, (255, 255, 255))
    texte_rect = texte.get_rect(center=(position_finale[0] + 150, position_finale[1] - 50))
    fenetre.blit(texte, texte_rect)

    pygame.display.flip()
    pygame.time.delay(1000)

def afficher_regles():
    pygame.init()
    fenetre_regles = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Règles de la Bataille")
    
    fond_regles = pygame.Surface((800, 600))
    fond_regles.fill((50, 50, 50))
    fond_regles.set_alpha(200)

    font_titre = pygame.font.SysFont("Helvetica", 36, bold=True)
    font_texte = pygame.font.SysFont("Helvetica", 24)
    font_retour = pygame.font.SysFont("Helvetica", 20)

    regles_texte = [
        "Règles de la Bataille :",
        "",
        "1. Le jeu se joue avec un jeu de 52 cartes.",
        "2. Les joueurs tirent chacun une carte de leur paquet.",
        "3. Le joueur avec la carte la plus forte remporte les deux cartes.",
        "4. En cas d'égalité, il y a 'bataille'.",
        "5. Le joueur qui remporte la bataille remporte toutes les cartes.",
        "6. Le jeu se termine lorsqu'un joueur n'a plus de cartes."
    ]

    rect_retour = pygame.Rect(600, 500, 150, 50)
    couleur_retour_normal = (0, 0, 0)
    couleur_retour_survol = (255, 255, 255)

    en_attente = True
    while en_attente:
        fenetre_regles.fill((0, 0, 0))
        fenetre_regles.blit(fond_regles, (0, 0))

        titre_surface = font_titre.render("Règles de la Bataille", True, (255, 255, 0))
        titre_rect = titre_surface.get_rect(center=(400, 50))
        fenetre_regles.blit(titre_surface, titre_rect)

        y_offset = 120
        for ligne in regles_texte:
            texte_surface = font_texte.render(ligne, True, (255, 255, 255))
            fenetre_regles.blit(texte_surface, (60, y_offset))
            y_offset += 30

        mouse_pos = pygame.mouse.get_pos()
        survol = rect_retour.collidepoint(mouse_pos)
        couleur_fond_retour = couleur_retour_survol if survol else couleur_retour_normal
        couleur_texte_retour = couleur_retour_normal if survol else couleur_retour_survol

        pygame.draw.rect(fenetre_regles, couleur_fond_retour, rect_retour, border_radius=10)
        texte_retour = font_retour.render("Retour", True, couleur_texte_retour)
        texte_retour_rect = texte_retour.get_rect(center=rect_retour.center)
        fenetre_regles.blit(texte_retour, texte_retour_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_retour.collidepoint(mouse_pos):
                    en_attente = False
                    fenetre_regles = pygame.display.set_mode((600, 400))
                    return

def charger_sons():
    son_tirage = pygame.mixer.Sound("son_cartes.mp3")
    return son_tirage


def bataille():
    pygame.init()
    son_tirage = charger_sons()

    largeur_fenetre = 1200
    hauteur_fenetre = 798
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Bataille")

    fond_jeu = pygame.image.load("fond_tapis_de_cartes.jpg")
    fond_jeu = pygame.transform.scale(fond_jeu, (largeur_fenetre, hauteur_fenetre))

    fond_score = pygame.image.load("tapis_de_carte.png")
    fond_score = pygame.transform.scale(fond_score, (largeur_fenetre, hauteur_fenetre))

    cartes_images = {}
    for i in range(55):
        nom_fichier = f"data/{i}.png"
        cartes_images[i // 13, i % 13] = pygame.image.load(nom_fichier)

    jeuA = JeuDeCartes()
    jeuB = JeuDeCartes()
    jeuA.battre()
    jeuB.battre()
    comptA = 0
    comptB = 0


    en_cours = True
    while en_cours:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_SPACE:
                en_cours = False

        carteA = jeuA.tirer()
        carteB = jeuB.tirer()
        son_tirage.play()

        if carteA is None or carteB is None:
            break

        position_depart_A = (100, hauteur_fenetre // 2 - 100)
        position_depart_B = (largeur_fenetre - 300, hauteur_fenetre // 2 - 100)
        position_finale = (largeur_fenetre // 2 - 150, hauteur_fenetre // 2 - 100)

        animer_cartes(fenetre, fond_jeu, carteA, carteB, position_depart_A, position_depart_B, position_finale, cartes_images, 20)

        gagnant = None
        if carteA[1] > carteB[1]:
            comptA += 1
            gagnant = "Joueur n°1"
        elif carteA[1] < carteB[1]:
            comptB += 1
            gagnant = "Joueur n°2"

        fenetre.blit(fond_jeu, (0, 0))
        afficher_score(fenetre, comptA, comptB, gagnant)    

        pygame.display.flip()
        pygame.time.delay(1000)

    fenetre.blit(fond_score, (0, 0))
    font = pygame.font.SysFont("Helvetica", 72)
    texte_score = font.render(f"Score final - Joueur 1 : {comptA} Joueur 2 : {comptB}", True, (255, 255, 255))
    texte_score_rect = texte_score.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
    fenetre.blit(texte_score, texte_score_rect)
    pygame.display.flip()

    pygame.time.delay(3000)
    pygame.quit()

def afficher_bouton(fenetre, texte, rect, font, couleur_bouton, couleur_texte, couleur_bouton_hover, couleur_texte_hover):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(fenetre, couleur_bouton_hover, rect, border_radius=10)
        texte_surface = font.render(texte, True, couleur_texte_hover)
    else:
        pygame.draw.rect(fenetre, couleur_bouton, rect, border_radius=10)
        texte_surface = font.render(texte, True, couleur_texte)
    
    texte_rect = texte_surface.get_rect(center=rect.center)
    fenetre.blit(texte_surface, texte_rect)

def menu_principal():
    pygame.init()
    fenetre = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Bataille - Menu")
    font = pygame.font.SysFont("Helvetica", 30)
    titre_font = pygame.font.SysFont("Helvetica", 72, bold=True)

    fond = pygame.image.load("tapis_de_carte.png")
    fond = pygame.transform.scale(fond, (600, 400))

    pygame.mixer.music.load("musique_fond.mp3")
    pygame.mixer.music.play(-1)

    couleur_bouton = (0, 0, 0, 128)
    couleur_texte = (255, 255, 255)
    couleur_bouton_hover = (255, 255, 255)
    couleur_texte_hover = (0, 0, 0)

    bouton_hauteur = 50
    bouton_ecart = 20
    y_position = (400 - (3 * bouton_hauteur + 2 * bouton_ecart - 60)) // 2

    boutons = {
        "Jouer en solo": pygame.Rect(150, y_position, 300, bouton_hauteur),
        "Jouer en multijoueur": pygame.Rect(150, y_position + bouton_hauteur + bouton_ecart, 300, bouton_hauteur),
        "Mode Entraînement": pygame.Rect(150, y_position + 2 * (bouton_hauteur + bouton_ecart), 300, bouton_hauteur),
        "Règles": pygame.Rect(450, 350, 100, 40),
    }
    
    choix = None
    while choix is None:
        fenetre.blit(fond, (0, 0))

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if boutons["Jouer en solo"].collidepoint(x, y):
                    choix = "solo"
                elif boutons["Jouer en multijoueur"].collidepoint(x, y):
                    choix = "multijoueur"
                elif boutons["Mode Entraînement"].collidepoint(x, y):
                    choix = "entrainement"
                elif boutons["Règles"].collidepoint(x, y):
                    afficher_regles()

        afficher_bouton(fenetre, "Jouer en solo", boutons["Jouer en solo"], font, couleur_bouton, couleur_texte, couleur_bouton_hover, couleur_texte_hover)
        afficher_bouton(fenetre, "Jouer en multijoueur", boutons["Jouer en multijoueur"], font, couleur_bouton, couleur_texte, couleur_bouton_hover, couleur_texte_hover)
        afficher_bouton(fenetre, "Mode Entraînement", boutons["Mode Entraînement"], font, couleur_bouton, couleur_texte, couleur_bouton_hover, couleur_texte_hover)
        afficher_bouton(fenetre, "Règles", boutons["Règles"], font, couleur_bouton, couleur_texte, couleur_bouton_hover, couleur_texte_hover)

        titre = titre_font.render("Bataille", True, (255, 255, 255))
        titre_rect = titre.get_rect(center=(300, 80))
        fenetre.blit(titre, titre_rect)

        pygame.display.flip()

    pygame.mixer.music.stop()
    return choix
    
def mode_entrainement():
    pygame.init()
    son_tirage = charger_sons()

    largeur_fenetre = 1200
    hauteur_fenetre = 798
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mode Entraînement")

    fond_jeu = pygame.image.load("fond_tapis_de_cartes.jpg")
    fond_jeu = pygame.transform.scale(fond_jeu, (largeur_fenetre, hauteur_fenetre))

    cartes_images = {}
    for i in range(52):
        couleur = i // 13
        valeur = i % 13
        nom_fichier = f"data/{i}.png"
        try:
            cartes_images[(couleur, valeur)] = pygame.image.load(nom_fichier)
        except pygame.error as e:
            print(f"Erreur de chargement de {nom_fichier}: {e}")

    jeu = JeuDeCartes()
    jeu.battre()

    en_cours = True
    while en_cours:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_SPACE:
                carte = jeu.tirer()
                son_tirage.play()
                position_finale = (largeur_fenetre // 2 - 75, hauteur_fenetre // 2 - 100)

                fenetre.blit(fond_jeu, (0, 0))
                if carte is not None:
                    fenetre.blit(cartes_images[carte], position_finale)
                else:
                    font = pygame.font.SysFont("Helvetica", 48)
                    texte = font.render("Plus de cartes !", True, (255, 0, 0))
                    texte_rect = texte.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
                    fenetre.blit(texte, texte_rect)

                pygame.display.flip()
                pygame.time.delay(1000)

    pygame.mixer.music.stop()
    pygame.quit()

def obtenir_adresse_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def obtenir_adresse_ip_adversaire():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("Adresse IP", "Entrez l'adresse IP de l'adversaire :")

def serveur():
    hote, port = '', 12800
    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((hote, port))
    connexion_principale.listen(5)
    print(f"Serveur en écoute sur le port {port}")

    client1 = connexion_principale.accept()[0]
    client2 = connexion_principale.accept()[0]

    client1.close()
    client2.close()
    connexion_principale.close()

def client(hote):
    port = 12800
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion.connect((hote, port))
    connexion.close()

if __name__ == "__main__":
    choix = menu_principal()
    if choix == "solo":
        bataille()
    elif choix == "multijoueur":
        mon_ip = obtenir_adresse_ip()
        ip_adversaire = obtenir_adresse_ip_adversaire()
        if ip_adversaire is None:
            pygame.quit()
            exit()
        if mon_ip < ip_adversaire:
            serveur()
        else:
            client(ip_adversaire)
    elif choix == "entrainement":
        mode_entrainement()