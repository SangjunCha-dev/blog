import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python 3.7 or higher")
def test_skipif_v1():
    assert 1 == 1

try:
    import numpy as np
except ImportError:
    pass

@pytest.mark.skipif('numpy' not in sys.modules, reason="requires the Numpy library")
def test_skipif_v2():
    assert 1 == 1