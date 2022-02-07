import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [pytest.param(1, 2, 4, marks=pytest.mark.xfail),
     pytest.param(2, 2, 6, marks=pytest.mark.xfail)]
)
def test_add_fail_xfail(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
