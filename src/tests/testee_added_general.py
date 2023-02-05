from src import General

def test_f():
    assert General.square(2) == 4
    assert General.square(-2) == 4
    assert General.square(0) == 0
    assert General.square(2.5) == 6.25


def test_g():
    assert General.cube(2) == 16
    assert General.cube(-2) == 16
    assert General.cube(0) == 0
    assert General.cube(2.5) == 39.0625


def test_h():
    assert General.firstLetter("hello") == 'h'
    assert General.firstLetter("h") == 'h'
    assert General.firstLetter("") == None


def test_j():
    assert General.lastLetter("hello") == 'o'
    assert General.lastLetter("h") == 'h'
    assert General.lastLetter("") == None