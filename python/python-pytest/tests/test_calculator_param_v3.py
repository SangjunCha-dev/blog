import pytest

add_test_data = [
    (1, 2, 3),
    (2, 2, 4),
    pytest.param(1, 2, 4, marks=pytest.mark.xfail),
    pytest.param(2, 2, 6, marks=pytest.mark.xfail),
]

@pytest.mark.parametrize("a, b, result", add_test_data)
def test_add(calculator, a, b, result):
    assert calculator.add(a, b) == result