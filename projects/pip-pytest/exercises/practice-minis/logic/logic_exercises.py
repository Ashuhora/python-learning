# Logic exercise functions for Python practice

def love_six(a: int, b: int) -> bool:
    """
    The number 6 is a truly great number. Given two int values, a and b, return true if either one is 6.
    Or if their sum or difference is 6.
    """
    pass


def can_haz_table(your_style: int, date_style: int) -> int:
    """
    You and your date are trying to get a table at a restaurant. The
    parameter "your_style" is the stylishness of your clothes, in the range 0..10,
    and "date_style" is the stylishness of your date's clothes. The result getting
    the table is encoded as an int value with 0=no, 1=maybe, 2=yes.
    
    If either of you is very stylish, 8 or more, then the result is 2 (yes).
    With the exception that if either of you has style of 2 or less, then the result is 0 (no).
    Otherwise the result is 1 (maybe).
    """   
    pass


def play_outside(temp: int, is_summer: bool) -> bool:
    """
    The children in Cleveland spend most of the day playing outside. In particular,
    they play if the temperature is between 60 and 90 (inclusive). Unless it is summer,
    then the upper limit is 100 instead of 90. Given an int temperature and a bool is_summer,
    return true if the children play and false otherwise.
    """  
    pass


def caught_speeding(speed: int, is_birthday: bool) -> int:
    """
    You are driving a little too fast, and a police officer stops you. Write code to compute
    the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
    
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
    """
    pass


def skip_sum(a: int, b: int) -> int:
    """
    Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive are forbidden,
    so in that case just return 20.
    """
    pass


def alarm_clock(day: int, vacation: bool) -> str:
    """
    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are
    on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays,
    the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then
    on weekdays it should be "10:00" and weekends it should be "off".
    """
    pass


def in_range(n: int, outside_mode: bool) -> bool:
    """
    Given a number n, return true if n is in the range 1..10, inclusive. Unless "outside_mode" is true,
    in which case return true if the number is less or equal to 1, or greater or equal to 10.
    """
    pass


def special_eleven(n: int) -> bool:
    """
    We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11.
    Return true if the given non-negative number is special. Use the % "mod" operator
    """
    pass


def mod_20(n: int) -> bool:
    """
    Return true if the given non-negative number is 1 or 2 more than a multiple of 20.
    Use the % "mod" operator
    """
    pass


def mod_35(n: int) -> bool:
    """
    Return true if the given non-negative number is a multiple of 3 or 5, but not both.
    Use the % "mod" operator
    """
    pass


def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
    """
    Your cell phone rings. Return true if you should answer it. Normally you answer,
    except in the morning you only answer if it is your mom calling.
    In all cases, if you are asleep, you do not answer.
    """
    pass


def two_is_one(a: int, b: int, c: int) -> bool:
    """
    Given three ints, a b c, return true if it is possible to add any two of the ints
    to get the third.
    """
    pass


def last_digit(a: int, b: int, c: int) -> bool:
    """
    This one is tricky! Given three ints, a b c, return true if two or more of them have
    the same rightmost digit. The ints are non-negative.
    """
    pass