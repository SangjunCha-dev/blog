import pytest

add_test_data = [
    pytest.param(1, 2, 3, id="1 add 2 is 3"),
    pytest.param(2, 2, 4, id="2 add 2 is 4"),
    pytest.param(1, 2, 4, marks=pytest.mark.xfail, id="1 add 2 is not 4"),
    pytest.param(2, 2, 6, marks=pytest.mark.xfail, id="2 add 2 is not 6"),
]

@pytest.mark.parametrize("a, b, result", add_test_data)
def test_add(calculator, a, b, result):
    assert calculator.add(a, b) == result
