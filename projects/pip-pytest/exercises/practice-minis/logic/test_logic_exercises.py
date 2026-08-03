import pytest
import logic_exercises as le

    
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 4, True),
        (4, 5, False),
        (1, 5, True)
    ]
)
def test_love_six(a, b, expected):
    assert le.love_six(a, b) == expected


@pytest.mark.parametrize(
    "your_style, date_style, expected",
    [
        (5, 10, 2),
        (5, 2, 0),
        (5, 5, 1)
    ]
)
def test_can_haz_table(your_style, date_style, expected):
    assert le.can_haz_table(your_style, date_style) == expected


@pytest.mark.parametrize(
    "temp, is_summer, expected",
    [
        (70, False, True),
        (95, False, False),
        (95, True, True)
    ]
)
def test_play_outside(temp, is_summer, expected):
    assert le.play_outside(temp, is_summer) == expected


@pytest.mark.parametrize(
    "speed, is_birthday, expected",
    [
        (60, False, 0),
        (65, False, 1),
        (65, True, 0)
    ]
)
def test_caught_speeding(speed, is_birthday, expected):
    assert le.caught_speeding(speed, is_birthday) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 7),
        (9, 4, 20),
        (10, 11, 21)
    ]
)
def test_skip_sum(a, b, expected):
    assert le.skip_sum(a, b) == expected


@pytest.mark.parametrize(
    "day, vacation, expected",
    [
        (1, False, "7:00"),
        (5, False, "7:00"),
        (3, True, "10:00")
    ]
)
def test_alarm_clock(day, vacation, expected):
    assert le.alarm_clock(day, vacation) == expected


@pytest.mark.parametrize(
    "n, outside_mode, expected",
    [
        (5, False, True),
        (11, False, False),
        (11, True, True)
    ]
)
def test_in_range(n, outside_mode, expected):
    assert le.in_range(n, outside_mode) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (22, True),
        (23, True),
        (24, False)
    ]
)
def test_special_eleven(n, expected):
    assert le.special_eleven(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (20, False),
        (21, True),
        (22, True)
    ]
)
def test_mod_20(n, expected):
    assert le.mod_20(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, True),
        (10, True),
        (15, False)
    ]
)
def test_mod_35(n, expected):
    assert le.mod_35(n) == expected


@pytest.mark.parametrize(
    "is_morning, is_mom, is_asleep, expected",
    [
        (False, False, False, True),
        (False, False, True, False),
        (True, False, False, False)
    ]
)
def test_answer_cell(is_morning, is_mom, is_asleep, expected):
    assert le.answer_cell(is_morning, is_mom, is_asleep) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 3, True),
        (3, 1, 2, True),
        (3, 2, 2, False)
    ]
)
def test_two_is_one(a, b, c, expected):
    assert le.two_is_one(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (23, 19, 13, True),
        (23, 19, 12, False),
        (23, 19, 3, True)
    ]
)
def test_last_digit(a, b, c, expected):
    assert le.last_digit(a, b, c) == expected