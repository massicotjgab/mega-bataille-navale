from pprint import pprint


class Plateau:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.cube = [[[0 for k in range(x)] for j in range(y)] for i in range(z)]

    def tirer(self, x, y):
        x = x - 1
        y = y - 1
        state_0 = 0
        state_X = 0
        nom_bateau = ""

        for z in range(3):
            if self.cube[z][y][x] == 0:
                state_0 = state_0 + 1
                self.cube[z][y][x] = "X"
            elif self.cube[z][y][x] == "X":
                state_X = state_X + 1
            else:
                nom_bateau = self.cube[z][y][x]
                self.cube[z][y][x] = "X"
                resultat = state_X + state_0 + 1
                coule = self.check_coule(nom_bateau)
                break

        if nom_bateau == "":
            resultat = 0
            coule = 0

        tram_answer = [3, resultat, coule]
        return tram_answer

    def place_bateau(self, type, taille_x, taille_y, x, y, z):
        x = x - 1
        y = y - 1
        z = z - 1
        for y_temp in range(taille_y):
            for x_temp in range(taille_x):
                self.cube[z][y_temp+y][x_temp+x] = type

    def check_vide(self):
        for x in range(self.x):
            for y in range(self.y):
                for z in range(self.z):
                    if self.cube[z][y][x] != 0 and self.cube[z][y][x] != "X":
                        return False
        return True

    def check_coule(self, type):
        for x in range(self.x):
            for y in range(self.y):
                for z in range(self.z):
                    if self.cube[z][y][x] == type:
                        return 0
        return 1

    def get_xyz(self, x, y, z):
        x = x - 1
        y = y - 1
        z = z - 1
        return self.cube[z][y][x]

    def set_xyz(self, x, y, z, value):
        x = x - 1
        y = y - 1
        z = z - 1
        self.cube[z][y][x] = value

    def print_zone(self):
        pprint(self.cube)


class Joueur:
    def __init__(self, nom):
        self.pseudo = nom
        self.attaque = Plateau(15, 15, 3)
        self.defense = Plateau(15, 15, 3)
        self.tram_pseudo = [1, len(self.pseudo)]
        self.tram_pseudo = self.tram_pseudo + list(self.pseudo)

    def get_pseudo(self):
        return self.pseudo

    def change_pseudo(self, nom):
        self.pseudo = nom
        self.tram_pseudo = [1, len(self.pseudo)]
        self.tram_pseudo = self.tram_pseudo + list(self.pseudo)

    def format_pseudo(self):
        return self.tram_pseudo

    def tirer(self, x, y):
        self.x = x
        self.y = y
        self.tram_tire = [2, x, y]
        return self.tram_tire

    def answer_tire(self, x, y):
        return self.defense.tirer(x, y)

    def place_bateau_test(self):
        self.defense.set_xyz(0, 0, 2, "Sous_marin")
        self.defense.set_xyz(1, 0, 2, "Sous_marin")
        self.defense.set_xyz(0, 1, 2, "Sous_marin")
        self.defense.set_xyz(1, 1, 2, "Sous_marin")


class Bateau:
    def __init__(self, nom, x, y):
        self.x = x
        self.y = y
        self.emplacement = [[0 for k in range(x)] for j in range(y)]
        self.niveau = 0
        self.name = nom

    def change_position(self, Plateau, niveau):
        self.emplacement = Plateau
        self.niveau = niveau
        for x_temp in range(self.x):
            for y_temp in range(self.y):
                if self.emplacement[y_temp][x_temp] != 0:
                    self.emplacement[y_temp][x_temp] = self.name

    def place_bateau(self, zone_de_jeu):
        for x_temp in range(self.x):
            for y_temp in range(self.y):
                if self.emplacement[y_temp][x_temp] != 0:
                    zone_de_jeu.set_xyz(x_temp, y_temp, self.niveau, self.name)


def main():
    Joueur1 = Joueur("Cocasticox")
    Joueur2 = Joueur("Lacoutt")

    Joueur1.place_bateau_test()

    pprint(Joueur1.tirer(1, 1))

    pprint(Joueur1.answer_tire(1, 1))


if __name__ == ('__main__'):
    main()
