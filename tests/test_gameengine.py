from GameEngine.GameEngine import Plateau
from GameEngine.GameEngine import Joueur
from GameEngine.GameEngine import Bateau
from pprint import pprint


def test():
    assert 2 > 1

########################################### Plateau
def test_tire_vide_plateau():
    plateau = Plateau(15, 15, 3)
    assert plateau.tirer(15, 15) == [3, 0, 0]

def test_tire_plateau():
    plateau = Plateau(15, 15, 3)
    plateau.set_xyz(2, 2, 2, "sous_marin")
    assert plateau.tirer(2, 2) == [3, 2, 1]

def test_place_bateau():
    plateau = Plateau(15, 15, 3)
    plateau.place_bateau("sous_marin", 2, 2, 2, 2, 1)
    assert plateau.get_xyz(2, 2, 1) == "sous_marin"

def test_place_bateau_2():
    plateau = Plateau(15, 15, 3)
    plateau.place_bateau("sous_marin", 2, 2, 2, 2, 1)
    assert plateau.get_xyz(3, 3, 1) == "sous_marin"

def test_vide():
    plateau = Plateau(15, 15, 3)
    assert plateau.check_vide() == True

def test__non_vide():
    plateau = Plateau(15, 15, 3)
    plateau.set_xyz(2, 2, 2, "sous_marin")
    assert plateau.check_vide() == False

def test_coule():
    plateau = Plateau(15, 15, 3)
    assert plateau.check_coule("sous_marin") == 1

def test_non_coule():
    plateau = Plateau(15, 15, 3)
    plateau.set_xyz(2, 2, 2, "sous_marin")
    assert plateau.check_coule("sous_marin") == 0

########################################### Joueur
def test_get_pseudo():
    player = Joueur("toto")
    assert player.get_pseudo() == "toto"

def test_change_pseudo():
    player = Joueur("toto")
    player.change_pseudo("titi")
    assert player.get_pseudo() == "titi"

def test_format_pseudo():
    player = Joueur("toto")
    assert player.format_pseudo() == [1, 4, "t", "o", "t", "o"]

def test_tire_joueur():
    player = Joueur("toto")
    assert player.tirer(1, 2) == [2, 1, 2]

def test_answer_tire():
    player = Joueur("toto")
    player.place_bateau_test()
    player.answer_tire(0, 1) == [3, 2, 0]

########################################### Bateau
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
