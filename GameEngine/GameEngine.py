
import pprint

class Cube:

    def __init__(self, x, y, z):
        Cube.cube = [[[0 for k in range(x)] for j in range(y)] for i in range(z)]

    def tirer(self, x, y):

        state_0 = 0
        state_X = 0
        nom_bateau = ""

        for z in range(3):
            if Cube.cube[z][y][x] == 0:
                state_0 = state_0 + 1
                Cube.cube[z][y][x] = "X"

            elif Cube.cube[z][y][x] == "X":
                state_X = state_X + 1
            else :
                nom_bateau = Cube.cube[z][y][x]
                Cube.cube[z][y][x] = "X"
                return z, nom_bateau

            if state_X >= 3:
                return 4, "XX"
                print("Plus rien à détruire ici")
            else :
                return 4, "X"

    def place_bateau(self, type, taille_x, taille_y, x, y, z):
        for y_temp in range(taille_y):
            for x_temp in range(taille_x):
                Cube.cube[z][y_temp+y][x_temp+x] = type





def main():
    zone_de_jeu = Cube(15, 15, 3)

    zone_de_jeu.place_bateau("porte_container", 3, 2, 10, 2, 1)

    zone_de_jeu.tirer(0, 0)
    zone_de_jeu.tirer(5, 5)
    zone_de_jeu.tirer(10, 2)
    zone_de_jeu.tirer(0, 0)



    pprint.pprint(zone_de_jeu.cube)





if __name__ == "__main__":
    main()
