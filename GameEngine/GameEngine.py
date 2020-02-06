from pprint import pprint

class Plateau:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.cube = [[[0 for k in range(x)] for j in range(y)] for i in range(z)]

    def tirer(self, x, y):

        state_0 = 0
        state_X = 0
        nom_bateau = ""

        for z in range(3):
            if self.cube[z][y][x] == 0:
                state_0 = state_0 + 1
                self.cube[z][y][x] = "X"
            elif self.cube[z][y][x] == "X":
                state_X = state_X + 1
            else :
                nom_bateau = self.cube[z][y][x]
                self.cube[z][y][x] = "X"
                return z, nom_bateau

        if state_X >= 3:
            return 4, "XX"
        else :
            return 4, "X"

    def place_bateau(self, type, taille_x, taille_y, x, y, z):
        for y_temp in range(taille_y):
            for x_temp in range(taille_x):
                self.cube[z][y_temp+y][x_temp+x] = type

    def check_vide(self):
        for x in range(self.x):
            for y in range(self.y):
                for z in range(self.z):
                    if self.cube[z][y][x] != 0 and self.cube[z][y][x] != "X" :
                        return False
        return True

    def check_any_exist(self, type):
        for x in range(self.x):
            for y in range(self.y):
                for z in range(self.z):
                    if self.cube[z][y][x] == type :
                        return True
        return False

    def get_xyz(self, x, y, z):
        return self.cube[z][y][x]

    def set_xyz(self, x, y, z, value):
        self.cube[z][y][x] = value

    def print_zone(self):
        pprint(self.cube)



class Joueur:
    def __init__(self, nom):
        self.pseudo = nom

    def get_pseudo(self):
        return self.pseudo

    def change_pseudo(self, nom):
        self.pseudo = nom

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
    zone_de_jeu = Plateau(15, 15, 3)
    Bateau1 = Bateau("Porte_container", 15, 15)

    Plateau_temp = [[0 for k in range(15)] for j in range(15)]
    Plateau_temp[2][10] = "Sous_marin"
    Plateau_temp[3][10] = "Sous_marin"
    Plateau_temp[2][11] = "Sous_marin"
    Plateau_temp[3][11] = "Sous_marin"

    Bateau1.change_position(Plateau_temp, 0)
    Bateau1.place_bateau(zone_de_jeu)
    zone_de_jeu.print_zone()


if __name__ == ('__main__'):
    main()
