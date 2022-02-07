import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 4),
     (2, 2, 6)]
)
def test_add_fail_parametrize(calculator, a, b, expected):
    assert calculator.add(a, b) != expected

@pytest.mark.xfail(reason="wrong result")
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 4),
     (2, 2, 6),
     (3, 4, 7)]
)
def test_add_fail_xfail(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
