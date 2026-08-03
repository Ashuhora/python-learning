from funcs import add, subtract, divide
import pytest

# running a test multiple times with different data
@pytest.mark.parametrize("a, b, expected_result", [
    (10, 5, 5),
    (0, 0, 0),
    (-2, 2, -4)
])
def test_subtract_params(a, b, expected_result):
    assert subtract(a, b) == expected_result

# use the test_ prefix or _text suffix to auto detect tests.
def test_add():
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(10, 5) == 5

def test_divide_by_zero():
    # This test verifies that dividing by zero raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)

    # you can use the excinfo for additional checks if you want
    assert "Cannot divide by zero!" in str(excinfo.value)