import pytest

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip_v1():
    assert 1 == 1

def test_skip_v2():
    if True:
        pytest.skip(reason="no way of currently testing this")
    assert 1 == 1