import pytest

@pytest.mark.parametrize(
    "a, b, result",
    [(1, 2, 3),
     (2, 2, 4)]
)
def test_add(calculator, a, b, result):
    assert calculator.add(a, b) == result

@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 4),
     (2, 2, 6)]
)
def test_add_fail(calculator, a, b, expected):
    assert calculator.add(a, b) != expected
