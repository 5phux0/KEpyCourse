import simple_math as sm


def test_add():
    assert sm.simple_add(1, 2) == 3

def test_sub():
    assert sm.simple_sub(2, 1) == 1

def test_mult():
    assert sm.simple_mult(2, 3) == 6

def test_div():
    assert sm.simple_div(6, 2) == 3
    assert sm.simple_div(27, 3) == 9

def test_poly_first():
    assert sm.poly_first(1, 2, 3) == 5
    assert sm.poly_first(-8, 5, 3) == -8*3+5

def test_poly_second():
    assert sm.poly_second(1, 2, 3, 4) == 2+3+4
    assert sm.poly_second(-5, 3, -4, 5) == 3 - 4*-5 + 5*-5*-5

