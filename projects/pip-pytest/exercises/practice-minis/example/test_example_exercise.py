import pytest
import example_exercise as ex

class TestExample:
    @pytest.mark.parametrize("x, y, expected", [
        (1, 1, 2),
        (5, 10, 15)
    ])
    def test_add(self, x, y, expected):
        actual = ex.add(x, y)
        
        assert actual == expected