from GameEngine.GameEngine import Joueur


def main():
    Joueur1 = Joueur("Cocasticox")  # Création d'un Joueur
    Joueur2 = Joueur("Lacoutt")     # Création d'un autre joueur

    # Placement d'un bateau (exemple uniquement) pour le joueur 1 et 2
    Joueur1.place_bateau_test()
    Joueur2.place_bateau_test()

    # Le joueur 1 tire en (x=1, y=1), cela crée la tram associée
    tram = Joueur1.tirer(1, 1)
    # Le joueur 2 décrypte cette tram, applique le tir sur sa grille
    # de défense, et conçois une nouvelle tram de réponse
    tram = Joueur2.decrypt_tram(tram)
    # Le joueur 1 recois la tram de réponse et applique les changements
    # sur sa grille d'attaque
    Joueur1.decrypt_tram(tram)


if __name__ == ('__main__'):
    main()
