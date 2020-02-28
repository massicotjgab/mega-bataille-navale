from Src.GameEngine.GameEngine import Plateau, Joueur, Bateau


# -------------------------- Test ---------------------------


def test():
    assert 2 > 1

# -------------------------- Plateau ---------------------------


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
    assert plateau.check_vide() is True


def test__non_vide():
    plateau = Plateau(15, 15, 3)
    plateau.set_xyz(2, 2, 2, "sous_marin")
    assert plateau.check_vide() is False


def test_coule():
    plateau = Plateau(15, 15, 3)
    assert plateau.check_coule("sous_marin") == 1


def test_non_coule():
    plateau = Plateau(15, 15, 3)
    plateau.set_xyz(2, 2, 2, "sous_marin")
    assert plateau.check_coule("sous_marin") == 0


def test_decrypt_tram_pseudo_adverse():
    Joueur1 = Joueur("toto")
    Joueur1.decrypt_tram([1, 4, "T", "I", "T", "I"])
    assert Joueur1.get_pseudo_adversaire() == "TITI"


def test_decrypt_tram_tire_eau():
    Joueur1 = Joueur("toto")
    assert Joueur1.decrypt_tram([2, 4, 5]) == [3, 0, 0]


def test_decrypt_tram_tire_bateau():
    Joueur1 = Joueur("toto")
    Joueur1.place_bateau_test()
    assert Joueur1.decrypt_tram([2, 2, 2]) == [3, 2, 0]


def test_decrypt_tram_tire_bateau_coule():
    Joueur1 = Joueur("toto")
    Joueur1.place_bateau_test()
    Joueur1.decrypt_tram([2, 1, 1])
    Joueur1.decrypt_tram([2, 1, 2])
    Joueur1.decrypt_tram([2, 2, 1])
    assert Joueur1.decrypt_tram([2, 2, 2]) == [3, 2, 1]


def test_differentiation_non_touche():
    Joueur1 = Joueur("toto")
    Joueur2 = Joueur("titi")
    Joueur2.place_bateau_test()
    tram = Joueur1.tirer(4, 5)
    tram = Joueur2.decrypt_tram(tram)
    Joueur1.decrypt_tram(tram)
    assert Joueur1.get_xyz_attaque(4, 5, 3) == "X"


def test_differentiation_touche():
    Joueur1 = Joueur("toto")
    Joueur2 = Joueur("titi")
    Joueur2.place_bateau_test()
    tram = Joueur1.tirer(1, 2)
    tram = Joueur2.decrypt_tram(tram)
    Joueur1.decrypt_tram(tram)
    assert Joueur1.get_xyz_attaque(1, 2, 2) == "T"


def test_placement_bateau_valid():
    Joueur1 = Joueur("toto")
    Joueur1.place_bateau("Bateau", [81, 82, 96, 97])
    tab = [Joueur1.get_xyz_defense(8, 6, 1), Joueur1.get_xyz_defense(7, 7, 1)]
    assert ["Bateau", "Bateau"] == tab


def test_placement_bateau_invalid():
    Joueur1 = Joueur("toto")
    Joueur1.place_bateau("Bateau", [73, 74, 75, 76])
    tab = [Joueur1.get_xyz_defense(15, 5, 1), Joueur1.get_xyz_defense(1, 6, 1)]
    Joueur1.print_defense()
    assert [0, 0] == tab

# -------------------------- Joueur ---------------------------


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
    assert player.answer_tire(1, 1) == [3, 2, 0]


def test_explosion_nucleraire():
    Joueur1 = Joueur("Cocasticox")
    Joueur2 = Joueur("Lacoutt")
    Joueur2.place_nucleaire_test()
    for x in range(6, 12):
        tram = Joueur1.tirer(x, 4)
        tram = Joueur2.decrypt_tram(tram)
        Joueur1.decrypt_tram(tram)
    result = [Joueur2.get_xyz_defense(3, 1, 2), Joueur2.get_xyz_defense(14,
                                                                        7, 2)]
    assert result == ["X", "X"]


def test_explosion_nucleaire_coin():
    Joueur1 = Joueur("Cocasticox")
    Joueur2 = Joueur("Lacoutt")
    Joueur2.place_nucleaire_test_coin()
    for x in range(1, 7):
        tram = Joueur1.tirer(x, 1)
        tram = Joueur2.decrypt_tram(tram)
        Joueur1.decrypt_tram(tram)
    result = [Joueur2.get_xyz_defense(1, 1, 2), Joueur2.get_xyz_defense(9,
                                                                        4, 2)]
    assert result == ["X_Sous_marin_nucleaire_1", "X"]


def test_format_grille_gui():
    Joueur1 = Joueur("Cocasticox")
    Joueur1.place_nucleaire_test()
    tab = Joueur1.formate_defense_gui()
    print(len(tab))
    tab_t = [0, 0]
    tab_t[0] = tab[275]
    tab_t[1] = tab[274]
    assert ["Sous_marin_nucleaire_1", 0] == tab_t


# --------------------------- Bateau --------------------------


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
