class TestCalcultor:
    value = 0

    def test_add(self):
        self.value += 1
        assert self.value == 1

    def test_result(self):
        assert self.value == 0
