import pytest
import condition_exercises as ce

@pytest.mark.parametrize("a_smile, b_smile, expected", [
    (True, True, True),
    (False, False, True),
    (False, True, False)
])
def test_are_we_in_trouble(a_smile, b_smile, expected):
    actual = ce.are_we_in_trouble(a_smile, b_smile)
    assert actual == expected


@pytest.mark.parametrize("is_weekday, is_vacation, expected", [
    (False, False, True),
    (True, False, False),
    (False, True, True)
])
def test_can_sleep_in(is_weekday, is_vacation, expected):
    actual = ce.can_sleep_in(is_weekday, is_vacation)
    assert actual == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3, 2, 5),
    (2, 2, 8)
])
def test_sum_double(a, b, expected):
    actual = ce.sum_double(a, b)
    assert actual == expected


@pytest.mark.parametrize("n, expected", [
    (23, 4),
    (10, 11),
    (21, 0)
])
def test_diff21(n, expected):
    actual = ce.diff21(n)
    assert actual == expected


@pytest.mark.parametrize("is_talking, hour, expected", [
    (True, 6, True),
    (True, 7, False),
    (False, 6, False)
])
def test_parrot_trouble(is_talking, hour, expected):
    actual = ce.parrot_trouble(is_talking, hour)
    assert actual == expected


@pytest.mark.parametrize("a, b, expected", [
    (9, 10, True),
    (9, 9, False),
    (1, 9, True)
])
def test_makes10(a, b, expected):
    actual = ce.makes10(a, b)
    assert actual == expected


@pytest.mark.parametrize("n, expected", [
    (103, True),
    (90, True),
    (89, False)
])
def test_near_hundred(n, expected):
    actual = ce.near_hundred(n)
    assert actual == expected


@pytest.mark.parametrize("a, b, negative, expected", [
    (1, -1, False, True),
    (-1, 1, False, True),
    (-4, -5, True, True)
])
def test_pos_neg(a, b, negative, expected):
    actual = ce.pos_neg(a, b, negative)
    assert actual == expected


@pytest.mark.parametrize("s, expected", [
    ("candy", "not candy"),
    ("x", "not x"),
    ("not bad", "not bad")
])
def test_not_string(s, expected):
    actual = ce.not_string(s)
    assert actual == expected


@pytest.mark.parametrize("string, n, expected", [
    ("kitten", 1, "ktten"),
    ("hello", 0, "ello"),
    ("kitten", 4, "kittn")
])
def test_missing_char(string, n, expected):
    actual = ce.missing_char(string, n)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("code", "eodc"),
    ("a", "a"),
    ("ab", "ba")
])
def test_front_back(string, expected):
    actual = ce.front_back(string)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("Microsoft", "MicMicMic"),
    ("Chocolate", "ChoChoCho"),
    ("at", "atatat")
])
def test_front3(string, expected):
    actual = ce.front3(string)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("cat", "tcatt"),
    ("Hello", "oHelloo"),
    ("a", "aaa")
])
def test_back_around(string, expected):
    actual = ce.back_around(string)
    assert actual == expected


@pytest.mark.parametrize("n, expected", [
    (3, True),
    (5, True),
    (8, False)
])
def test_multiple3or5(n, expected):
    actual = ce.multiple3or5(n)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("hi there", True),
    ("Hi", False),
    ("orange juice", False)
])
def test_start_hi(string, expected):
    actual = ce.start_hi(string)
    assert actual == expected