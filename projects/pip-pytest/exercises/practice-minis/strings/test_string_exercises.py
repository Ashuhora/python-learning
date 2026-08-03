import pytest
import string_exercises as se

@pytest.mark.parametrize("name, expected", [
    ("Bob", "Hello Bob!"),
    ("Alice", "Hello Alice!"),
    ("X", "Hello X!")
])
def test_say_hi(name, expected):
    actual = se.say_hi(name)
    assert actual == expected

@pytest.mark.parametrize("a, b, expected", [
    ("Hi", "Bye", "HiByeByeHi"),
    ("Yo", "Alice", "YoAliceAliceYo"),
    ("What", "Up", "WhatUpUpWhat")
])
def test_abba(a, b, expected):
    actual = se.abba(a, b)
    assert actual == expected

@pytest.mark.parametrize("tag, content, expected", [
    ("i", "Yay", "<i>Yay</i>"),
    ("i", "Hello", "<i>Hello</i>"),
    ("cite", "Yay", "<cite>Yay</cite>")
])
def test_make_tags(tag, content, expected):
    actual = se.make_tags(tag, content)
    assert actual == expected

@pytest.mark.parametrize("container, word, expected", [
    ("<<>>", "Yay", "<<Yay>>"),
    ("<<>>", "WooHoo", "<<WooHoo>>"),
    ("[[]]", "word", "[[word]]")
])
def test_insert_word(container, word, expected):
    actual = se.insert_word(container, word)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("Hello", "lololo"),
    ("ab", "ababab"),
    ("Hi", "HiHiHi")
])
def test_multiple_endings(str_val, expected):
    actual = se.multiple_endings(str_val)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("WooHoo", "Woo"),
    ("HelloThere", "Hello"),
    ("abcdef", "abc")
])
def test_first_half(str_val, expected):
    actual = se.first_half(str_val)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("Hello", "ell"),
    ("java", "av"),
    ("coding", "odin")
])
def test_trim_one(str_val, expected):
    actual = se.trim_one(str_val)
    assert actual == expected

@pytest.mark.parametrize("a, b, expected", [
    ("Hello", "hi", "hiHellohi"),
    ("hi", "Hello", "hiHellohi"),
    ("aaa", "b", "baaab")
])
def test_long_in_middle(a, b, expected):
    actual = se.long_in_middle(a, b)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("Hello", "lloHe"),
    ("java", "vaja"),
    ("Hi", "Hi")
])
def test_rotate_left2(str_val, expected):
    actual = se.rotate_left2(str_val)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("Hello", "loHel"),
    ("java", "vaja"),
    ("Hi", "Hi")
])
def test_rotate_right2(str_val, expected):
    actual = se.rotate_right2(str_val)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("string", "ri"),
    ("code", "od"),
    ("Practice", "ct")
])
def test_middle_two(str_val, expected):
    actual = se.middle_two(str_val)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("oddly", True),
    ("y", False),
    ("oddy", False)
])
def test_ends_with_ly(str_val, expected):
    actual = se.ends_with_ly(str_val)
    assert actual == expected

@pytest.mark.parametrize("str_val, n, expected", [
    ("Hello", 2, "Helo"),
    ("Chocolate", 3, "Choate"),
    ("Chocolate", 1, "Ce")
])
def test_front_and_back(str_val, n, expected):
    actual = se.front_and_back(str_val, n)
    assert actual == expected

@pytest.mark.parametrize("str_val, n, expected", [
    ("java", 0, "ja"),
    ("java", 2, "va"),
    ("java", 3, "ja")
])
def test_take_two_from_position(str_val, n, expected):
    actual = se.take_two_from_position(str_val, n)
    assert actual == expected

@pytest.mark.parametrize("str_val, expected", [
    ("badxx", True),
    ("xbadxx", True),
    ("xxbadxx", False)
])
def test_has_bad(str_val, expected):
    actual = se.has_bad(str_val)
    assert actual == expected