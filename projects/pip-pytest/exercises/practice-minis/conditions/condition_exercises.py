def are_we_in_trouble(a_smile: bool, b_smile: bool) -> bool:
    """ We have two children, a and b, and the parameters a_smile and b_smile indicate 
    if each is smiling. We are in trouble if they are both smiling or if neither of 
    them is smiling. 
    
    Return true if we are in trouble. 
    """
    pass


def can_sleep_in(is_weekday: bool, is_vacation: bool) -> bool:
    """ The parameter weekday is true if it is a weekday, and the parameter vacation is true 
    if we are on vacation. We sleep in if it is not a weekday or we're on vacation. 
    
    Return true if we sleep in. 
    """
    pass


def sum_double(a: int, b: int) -> int:
    """ Given two int values, return their sum. However, if the two values are the same, 
    then return double their sum. 
    """
    pass


def diff21(n: int) -> int:
    """ Given an int n, return the absolute value of the difference between n and 21, 
    except return double the absolute value of the difference if n is over 21. 
    """
    pass


def parrot_trouble(is_talking: bool, hour: int) -> bool:
    """ We have a loud talking parrot. The "hour" parameter is the current hour time in 
    the range 0..23. We are in trouble if the parrot is talking and the hour is before 
    7 or after 20. 
    
    Return true if we are in trouble.
    """
    pass


def makes10(a: int, b: int) -> bool:
    """ Given two ints, a and b, return true if one if them is 10 or if their sum is 10. 
    """
    pass


def near_hundred(n: int) -> bool:
    """ Given an int n, return true if it is within 10 of 100 or 200.
    """
    pass


def pos_neg(a: int, b: int, negative: bool) -> bool:
    """ Given two int values, return true if one is negative and one is positive. 
    Except if the parameter "negative" is true, then return true only if both are negative. 
    """
    pass


def not_string(s: str) -> str:
    """ Given a string, return a new string where "not " has been added to the front. However, 
    if the string already begins with "not", return the string unchanged.
    """
    pass


def missing_char(s: str, n: int) -> str:
    """ Given a non-empty string and an int n, return a new string where the char at index n has 
    been removed. The value of n will be a valid index of a char in the original string 
    
    (Don't check for bad index).
    """
    pass


def front_back(s: str) -> str:
    """ Given a string, return a new string where the first and last chars have been exchanged. 
    """
    pass


def front3(s: str) -> str:
    """ Given a string, we'll say that the front is the first 3 chars of the string. If the string 
    length is less than 3, the front is whatever is there. Return a new string which is 3 copies 
    of the front. 
    """
    pass


def back_around(s: str) -> str:
    """ Given a string, take the last char and return a new string with the last char added at the 
    front and back, so "cat" yields "tcatt". 
    
    The original string will be length 1 or more. 
    """
    pass


def multiple3or5(n: int) -> bool:
    """ Return true if the given non-negative number is a multiple of 3 or a multiple of 5. 
    
    Use the % "mod" operator
    """
    pass


def start_hi(s: str) -> bool:
    """ Given a string, return true if the string starts with "hi" and false otherwise. 
    """
    pass