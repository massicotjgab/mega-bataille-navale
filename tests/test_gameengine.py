from GameEngine.GameEngine import Plateau
from GameEngine.GameEngine import Joueur
from GameEngine.GameEngine import Bateau


def test():
    assert 2 > 1

########################################### Test Zone de jeu

def test_tire_bateau():
    test = Plateau(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    assert test.tirer(10, 2) == (1, 'porte_container')

def test_double_tire_bateau():
    test = Plateau(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    test.tirer(10, 2)
    assert test.tirer(10, 2) == (4, 'X')

def test_triple_tire_bateau_unique():
    test = Plateau(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    test.tirer(10, 2)
    test.tirer(10, 2)
    assert test.tirer(10, 2) == (4, 'XX')

def test_tire_eau():
    test = Plateau(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    assert test.tirer(0, 0) == (4, 'X')

def test_double_tire_eau():
    test = Plateau(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    test.tirer(0, 0)
    assert test.tirer(0, 0) == (4, 'XX')

def test_vide():
    test = Plateau(15, 15, 3)
    assert test.check_vide() == True

def test_non_vide():
    test = Plateau(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    assert test.check_vide() == False


######################################### Test Joueur

def test_get_pseudo():
    joueur1 = Joueur("toto")
    assert joueur1.get_pseudo() == "toto"

def test_change_pseudo():
    joueur1 = Joueur("toto")
    joueur1.change_pseudo("titi")
    assert joueur1.get_pseudo() == "titi"

####################################### Test Bateau

def test_bateau_existe():
    test = Plateau(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    assert test.check_any_exist("porte_container") == True

def test_bateau_disparu():
    test = Plateau(15, 15, 3)
    assert test.check_any_exist("porte_container") == False

def test_bateau_class_1():
    zone_de_jeu = Plateau(15, 15, 3)
    Bateau1 = Bateau("Porte_container", 15, 15)

    Plateau_temp = [[0 for k in range(15)] for j in range(15)]
    Plateau_temp[2][10] = "Sous_marin"
    Plateau_temp[3][10] = "Sous_marin"
    Plateau_temp[2][11] = "Sous_marin"
    Plateau_temp[3][11] = "Sous_marin"

    Bateau1.change_position(Plateau_temp, 0)
    Bateau1.place_bateau(zone_de_jeu)
    assert zone_de_jeu.get_xyz(10, 2, 0) == "Porte_container"

def test_bateau_class_2():
    zone_de_jeu = Plateau(15, 15, 3)
    Bateau1 = Bateau("Porte_container", 15, 15)

    Plateau_temp = [[0 for k in range(15)] for j in range(15)]
    Plateau_temp[2][10] = "Sous_marin"
    Plateau_temp[3][10] = "Sous_marin"
    Plateau_temp[2][11] = "Sous_marin"
    Plateau_temp[3][11] = "Sous_marin"

    Bateau1.change_position(Plateau_temp, 2)
    Bateau1.place_bateau(zone_de_jeu)
    assert zone_de_jeu.get_xyz(11, 3, 2) == "Porte_container"
