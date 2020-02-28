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
        resultat = 0
        coule = 0
        nom_bateau = ""

        for z in range(3):
            if self.cube[z][y][x] == 0:
                state_0 = state_0 + 1
                self.cube[z][y][x] = "X"
            elif self.cube[z][y][x][0] == "X":
                state_X = state_X + 1
            else:
                nom_bateau = self.cube[z][y][x]
                self.cube[z][y][x] = "X_" + nom_bateau
                resultat = state_X + state_0 + 1
                coule = self.check_coule(nom_bateau)
                break

        if nom_bateau.find("ucl") >= 0 and coule == 1:
            self.explose_nucleaire(nom_bateau)

        tram_answer = [3, resultat, coule]
        return tram_answer

    def explose_nucleaire(self, nom_bateau):
        for x in range(15):
            for y in range(15):
                for z in range(3):
                    if self.cube[z][y][x] == 0:
                        pass
                    elif self.cube[z][y][x].find(nom_bateau) >= 0:
                        for x_exp in range(-3, 4):
                            for y_exp in range(-3, 4):
                                nom_case = self.cube[z][y+y_exp][x+x_exp]
                                if (0 <= (x+x_exp) <= 14) and (0 <= (y+y_exp) <= 14):
                                    if nom_case == 0:
                                        self.cube[z][y+y_exp][x+x_exp] = "X"
                                    elif nom_case[0] != "X":
                                        self.cube[z][y+y_exp][x+x_exp] = "X_" + nom_case

    def get_plateau_gui(self):
        tab = []
        for z in range(1, 4):
            for y in range(1, 16):
                for x in range(1, 16):
                    tab.append(self.get_xyz(x, y, z))
        return tab

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
                    if self.cube[z][y][x] != 0 and self.cube[z][y][x][0] != "X":
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
        self.pseudo_adversaire = ""
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

    def decrypt_tram(self, tram):
        if tram[0] == 1:    # Name
            self.pseudo_adversaire = ''.join(tram[2:])
        elif tram[0] == 2:  # Tire
            return self.answer_tire(tram[1], tram[2])
        elif tram[0] == 3:  # Answer
            if tram[1] == 0:
                for z in range(1, 4):
                    self.attaque.set_xyz(self.x, self.y, z, "X")
            else:
                for z in range(1, tram[1]):
                    self.attaque.set_xyz(self.x, self.y, z, "X")
                self.attaque.set_xyz(self.x, self.y, tram[1], "T")
                if tram[2] == 1:
                    return True
        return False

    def get_pseudo_adversaire(self):
        return self.pseudo_adversaire

    def print_defense(self):
        self.defense.print_zone()

    def print_attaque(self):
        self.attaque.print_zone()

    def get_xyz_defense(self, x, y, z):
        return self.defense.get_xyz(x, y, z)

    def get_xyz_attaque(self, x, y, z):
        return self.attaque.get_xyz(x, y, z)

    def formate_attaque_gui(self):
        return self.attaque.get_plateau_gui()

    def formate_defense_gui(self):
        return self.defense.get_plateau_gui()

    def place_bateau(self, type, array):
        if self.check_placement_bateau(array) is False:
            return False
        len_array = len(array)
        base = 15
        for indice in range(len_array):
            value = array[indice]
            z = value//(base*base)+1
            value = value - (z-1)*(base*base)
            y = (value//base)+1
            x = (value % base)+1
            self.defense.set_xyz(x, y, z, type)

    def check_placement_bateau(self, array):
        len_array = len(array)
        base = 15
        for indice in range(len_array-1):  # check même profondeur
            value = array[indice]
            z_prev = value//(base*base)+1
            value = array[indice+1]
            z_next = value//(base*base)+1
            if z_prev != z_next:
                return False
        for transition_prev in range(14, 660, 15):
            transition_next = transition_prev + 1
            for i in range(len_array-1):
                if array[i] == transition_prev and array[i+1] == transition_next:
                    return False
        return True

    def place_bateau_test(self):
        self.place_bateau("Sous_marin", [225, 226, 240, 241])

    def place_nucleaire_test(self):
        self.place_bateau("Sous_marin_nucleaire_1", [275, 276, 277, 278,
                          279, 280])

    def place_nucleaire_test_coin(self):
        self.place_bateau("Sous_marin_nucleaire_1", [225, 226, 227, 228,
                          229, 230])


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


# def main():
#     Joueur1 = Joueur("Cocasticox")
#     # Joueur2 = Joueur("Lacoutt")
#
#     Joueur1.place_bateau("Bateau", [73, 74, 75, 76])
#     # Joueur1.place_bateau_test()
#     # Joueur2.place_bateau_test()
#
#     # tram = Joueur1.tirer(1, 1)
#     # tram = Joueur2.decrypt_tram(tram)
#     # Joueur1.decrypt_tram(tram)
#
#     Joueur1.print_defense()
#     print("##################################################################")
#     # Joueur1.print_attaque()
#
# if __name__ == ('__main__'):
#     main()
