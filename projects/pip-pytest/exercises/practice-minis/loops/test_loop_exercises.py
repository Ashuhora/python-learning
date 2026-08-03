import pytest
import loop_exercises as le
    
@pytest.mark.parametrize("s, n, expected", [
    ("Hi", 2, "HiHi"),
    ("Hi", 3, "HiHiHi"),
    ("Hi", 1, "Hi")
])
def test_string_times(s, n, expected):
    actual = le.string_times(s, n)
    assert actual == expected

@pytest.mark.parametrize("s, n, expected", [
    ("Chocolate", 2, "ChoCho"),
    ("Chocolate", 3, "ChoChoCho"),
    ("Abc", 3, "AbcAbcAbc")
])
def test_front_times(s, n, expected):
    actual = le.front_times(s, n)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("abcxx", 1),
    ("xxxx", 3),
    ("ab", 0)
])
def test_count_xx(s, expected):
    actual = le.count_xx(s)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("axxbb", True),
    ("axaxxax", False),
    ("xxxxx", True)
])
def test_double_x(s, expected):
    actual = le.double_x(s)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("Hello", "Hlo"),
    ("Hi", "H"),
    ("Heeololeo", "Hello")
])
def test_every_other(s, expected):
    actual = le.every_other(s)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("Code", "CCoCodCode"),
    ("abc", "aababc"),
    ("ab", "aab")
])
def test_string_splosion(s, expected):
    actual = le.string_splosion(s)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("hixxhi", 1),
    ("xaxxaxaxx", 1),
    ("axxxaaxx", 2)
])
def test_count_last_2(s, expected):
    actual = le.count_last_2(s)
    assert actual == expected

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 9], 1),
    ([1, 9, 9], 2),
    ([1, 9, 9, 3, 9], 3)
])
def test_count_9(numbers, expected):
    actual = le.count_9(numbers)
    assert actual == expected

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 9, 3, 4], True),
    ([1, 2, 3, 4, 9], False),
    ([1, 2, 3, 4, 5], False)
])
def test_array_front_9(numbers, expected):
    actual = le.array_front_9(numbers)
    assert actual == expected

@pytest.mark.parametrize("numbers, expected", [
    ([1, 1, 2, 3, 1], True),
    ([1, 1, 2, 4, 1], False),
    ([1, 1, 2, 1, 2, 3], True)
])
def test_array_123(numbers, expected):
    actual = le.array_123(numbers)
    assert actual == expected

@pytest.mark.parametrize("a, b, expected", [
    ("xxcaazz", "xxbaaz", 3),
    ("abc", "abc", 2),
    ("abc", "axc", 0)
])
def test_substring_match(a, b, expected):
    actual = le.substring_match(a, b)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("xxHxix", "xHix"),
    ("abxxxcd", "abcd"),
    ("xabxxxcdx", "xabcdx")
])
def test_string_x(s, expected):
    actual = le.string_x(s)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("kitten", "kien"),
    ("Chocolate", "Chole"),
    ("CodingHorror", "Congrr")
])
def test_alt_pairs(s, expected):
    actual = le.alt_pairs(s)
    assert actual == expected

@pytest.mark.parametrize("s, expected", [
    ("yakpak", "pak"),
    ("pakyak", "pak"),
    ("yak123ya", "123ya")
])
def test_do_not_yak(s, expected):
    actual = le.do_not_yak(s)
    assert actual == expected

@pytest.mark.parametrize("numbers, expected", [
    ([6, 6, 2], 1),
    ([6, 6, 2, 6], 1),
    ([6, 7, 2, 6], 1)
])
def test_array_667(numbers, expected):
    actual = le.array_667(numbers)
    assert actual == expected

@pytest.mark.parametrize("numbers, expected", [
    ([1, 1, 2, 2, 1], True),
    ([1, 1, 2, 2, 2, 1], False),
    ([1, 1, 1, 2, 2, 2, 1], False)
])
def test_no_triples(numbers, expected):
    actual = le.no_triples(numbers)
    assert actual == expected

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 7, 1], True),
    ([1, 2, 8, 1], False),
    ([2, 7, 1], True)
])
def test_pattern_51(numbers, expected):
    actual = le.pattern_51(numbers)
    assert actual == expected