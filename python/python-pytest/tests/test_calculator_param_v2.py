import pytest

@pytest.mark.parametrize(
    "a, b, result",
    [(1, 2, 3),
     (2, 2, 4),
     pytest.param(1, 2, 4, marks=pytest.mark.xfail),
     pytest.param(2, 2, 6, marks=pytest.mark.xfail)]
)
def test_add(calculator, a, b, result):
    assert calculator.add(a, b) == result
