# A collection of string manipulation exercises

def say_hi(name: str) -> str:
    """ Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!". """
    pass

def abba(a: str, b: str) -> str:
    """ Given two strings, a and b, return the result of putting them together in the order 
     abba, e.g. "Hi" and "Bye" returns "HiByeByeHi". 
    """
    pass

def make_tags(tag: str, content: str) -> str:
    """ The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
     In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and 
     word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>". 
    """
    pass

def insert_word(container: str, word: str) -> str:
    """ Given an "out" string length 4, such as "<<>>", and a word, return a new string where 
     the word is in the middle of the out string, e.g. "<<word>>".
     Hint: Substrings are your friend here 
    """
    pass

def multiple_endings(str_val: str) -> str:
    """ Given a string, return a new string made of 3 copies of the last 2 chars of the original 
     string. The string length will be at least 2. 
    """
    pass

def first_half(str_val: str) -> str:
    """ Given a string of even length, return the first half. So the string "WooHoo" yields "Woo". """
    pass

def trim_one(str_val: str) -> str:
    """ Given a string, return a version without the first and last char, so "Hello" yields "ell". 
     The string length will be at least 2. 
    """
    pass

def long_in_middle(a: str, b: str) -> str:
    """ Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string 
     on the outside and the longer string on the inside. The strings will not be the same length, but 
     they may be empty (length 0). 
    """
    pass

def rotate_left2(str_val: str) -> str:
    """ Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
     The string length will be at least 2. 
    """
    pass

def rotate_right2(str_val: str) -> str:
    """ Given a string, return a "rotated right 2" version where the last 2 chars are moved to the start. 
     The string length will be at least 2. 
    """
    pass

def middle_two(str_val: str) -> str:
    """ Given a string of even length, return a string made of the middle two chars, so the string "string" 
     yields "ri". The string length will be at least 2. """
    pass

def ends_with_ly(str_val: str) -> bool:
    """ Given a string, return true if it ends in "ly". """
    pass

def front_and_back(str_val: str, n: int) -> str:
    """ Given a string and an int n, return a string made of the first and last n chars from the string. 
     The string length will be at least n. 
    """
    pass

def take_two_from_position(str_val: str, n: int) -> str:
    """ Given a string and an index, return a string length 2 starting at the given index. If the index is 
     too big or too small to define a string length 2, use the first 2 chars. The string length will be at least 2. 
    """
    pass

def has_bad(str_val: str) -> bool:
    """ Given a string, return true if "bad" appears starting at index 0 or 1 in the string, such as with "badxxx" or 
     "xbadxx" but not "xxbadxx". The string may be any length, including 0. 
    """
    pass