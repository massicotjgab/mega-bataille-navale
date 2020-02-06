import pprint

class Cube:

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


class Joueur:
    def __init__(self, nom):
        self.pseudo = nom

    def get_pseudo(self):
        return self.pseudo

    def change_pseudo(self, nom):
        self.pseudo = nom




def main():
    zone_de_jeu = Cube(15, 15, 3)
    Joueur1 = Joueur("Cocasticox")
    Joueur2 = Joueur("Lacoutt")
    print()

    print(zone_de_jeu.check_vide())
    zone_de_jeu.place_bateau("porte_container", 3, 2, 10, 2, 1)
    print(zone_de_jeu.check_vide())
    print(zone_de_jeu.tirer(10, 2))

    print(zone_de_jeu.tirer(10, 2))

    #pprint.pprint(zone_de_jeu.cube)





if __name__ == ('__main__'):
    main()
