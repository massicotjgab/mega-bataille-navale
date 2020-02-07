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

class Partie:
    def __init__(self, joueur1, joueur2, x, y, z):
        self.joueur1 = Joueur(joueur1)
        self.joueur2 = Joueur(joueur2)
        self.plateau_joueur1 = Plateau(x, y, z)
        self.plateau_joueur2 = Plateau(x, y, z)

    def get_pseudo_joueur1(self):
        return self.joueur1.get_pseudo()

    def get_pseudo_joueur2(self):
        return self.joueur2.get_pseudo()

    def setup_joueur1(self, nom, plateau, niveau):
        placement = Bateau(nom, 15, 15)
        placement.change_position(plateau, niveau)
        placement.place_bateau(self.plateau_joueur1)
        print(f"{nom} placé par {self.joueur1.get_pseudo()}")

    def setup_joueur2(self, nom, plateau, niveau):
        placement = Bateau(nom, 15, 15)
        placement.change_position(plateau, niveau)
        placement.place_bateau(self.plateau_joueur2)
        print(f"{nom} placé par {self.joueur2.get_pseudo()}")

    def tir_joueur1(self, x, y):
        (niveau, state) = self.plateau_joueur2.tirer(x, y)
        if niveau == 4:
            if state == 'X':
                print("Coup dans l'eau !")
            elif state == 'XX':
                print("Tu as déjà tiré ici !")
        else:
            if self.plateau_joueur2.check_any_exist(state) == False:
                print(f"Tu as coulé un {state} au niveau {niveau} !")
            else :
                print(f"Tu as touché un {state} au niveau {niveau} !")

        if self.plateau_joueur2.check_vide() == True:
            print("Plus aucun bateau adverse !")
            return True
        else :
            return False

    def tir_joueur2(self, x, y):
        (niveau, state) = self.plateau_joueur1.tirer(x, y)
        if niveau == 4:
            if state == 'X':
                print("Coup dans l'eau !")
            elif state == 'XX':
                print("Tu as déjà tiré ici !")
        else:
            if self.plateau_joueur1.check_any_exist(state) == False:
                print(f"Tu as coulé un {state} au niveau {niveau} !")
            else :
                print(f"Tu as touché un {state} au niveau {niveau} !")

        if self.plateau_joueur1.check_vide() == True:
            print("Plus aucun bateau adverse !")
            return True
        else :
            return False





def main():
    NewGame = Partie("Cocasticox", "Lacoutt", 15, 15, 3)

    Plateau_temp = [[0 for k in range(15)] for j in range(15)]
    Plateau_temp[3][7] = "X"
    #Plateau_temp[3][10] = "X"
    #Plateau_temp[2][11] = "X"
    #Plateau_temp[3][11] = "X"
    NewGame.setup_joueur1("Sous_marin", Plateau_temp, 0)

    Plateau_temp = [[0 for k in range(15)] for j in range(15)]
    Plateau_temp[0][0] = "X"
    NewGame.setup_joueur2("Bateau", Plateau_temp, 0)
    NewGame.setup_joueur2("Bateau", Plateau_temp, 2)




    while(1):
        print(f"Au tour de {NewGame.get_pseudo_joueur1()}")
        if NewGame.tir_joueur1(int(input()), int(input())) == True:
            break
        print(f"Au tour de {NewGame.get_pseudo_joueur2()}")
        if NewGame.tir_joueur2(int(input()), int(input())) == True:
            break


    #zone_de_jeu.print_zone()


if __name__ == ('__main__'):
    main()
