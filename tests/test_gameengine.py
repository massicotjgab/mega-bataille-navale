from GameEngine.GameEngine import Cube

def test():
    assert 2 > 1

def test_tire_bateau():
    test = Cube(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    assert test.tirer(10, 2) == (1, 'porte_container')

def test_double_tire_bateau():
    test = Cube(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    test.tirer(10, 2)
    assert test.tirer(10, 2) == (4, 'X')

def test_triple_tire_bateau_unique():
    test = Cube(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    test.tirer(10, 2)
    test.tirer(10, 2)
    assert test.tirer(10, 2) == (4, 'XX')

def test_tire_eau():
    test = Cube(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    assert test.tirer(0, 0) == (4, 'X')

def test_double_tire_eau():
    test = Cube(15, 15, 3)
    test.place_bateau("porte_container", 3, 2, 10, 2, 1)
    test.tirer(0, 0)
    assert test.tirer(0, 0) == (4, 'XX')
