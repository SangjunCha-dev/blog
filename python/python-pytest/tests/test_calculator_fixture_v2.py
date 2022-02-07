def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(2, 2) == 4

def test_sub(calculator):
    assert calculator.sub(5, 1) == 4
    assert calculator.sub(3, 2) == 1

def test_mul(calculator):
    assert calculator.mul(2, 2) == 4
    assert calculator.mul(5, 6) == 30

def test_div(calculator):
    assert calculator.div(8, 2) == 4
    assert calculator.div(9, 3) == 3
