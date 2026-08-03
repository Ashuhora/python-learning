# loop exercises

def string_times(s: str, n: int) -> str:
    """ Given a string and a non-negative int n, return a larger string 
    that is n copies of the original string. """
    
    pass

def front_times(s: str, n: int) -> str:
    """ Given a string and a non-negative int n, we'll say that the front of 
    the string is the first 3 chars, or whatever is there if the string is less 
    than length 3. Return n copies of the front;
    """
    
    pass

def count_xx(s: str) -> int:
    """ Count the number of "xx" in the given string. We'll say that overlapping is 
    allowed, so "xxx" contains 2 "xx". 
    """
    
    pass

def double_x(s: str) -> bool:
    """ Given a string, return true if the first instance of "x" in the string is 
    immediately followed by another "x". 
    """
    
    pass

def every_other(s: str) -> str:
    """ Given a string, return a new string made of every other char starting with 
    the first, so "Hello" yields "Hlo". 
    """
    
    pass

def string_splosion(s: str) -> str:
    """ Given a non-empty string like "Code" return a string like "CCoCodCode".  
    (first char, first two, first 3, etc) 
    """
    
    pass

def count_last_2(s: str) -> int:
    """ Given a string, return the count of the number of times that a substring 
    length 2 appears in the string and also as the last 2 chars of the string, 
    so "hixxxhi" yields 1 (we won't count the end substring). 
    """
    
    pass

def count_9(numbers: list[int]) -> int:
    """ Given a list of ints, return the number of 9's in the list. """
    
    pass

def array_front_9(numbers: list[int]) -> bool:
    """ Given a list of ints, return true if one of the first 4 elements in the 
    list is a 9. The list length may be less than 4. 
    """
    
    pass

def array_123(numbers: list[int]) -> bool:
    """ Given a list of ints, return true if .. 1, 2, 3, .. appears in the 
    list somewhere. 
    """
    
    pass

def substring_match(a: str, b: str) -> int:
    """ Given 2 strings, a and b, return the number of the positions where they 
    contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
    since the "xx", "aa", and "az" substrings appear in the same place in 
    both strings. 
    """
    
    pass

def string_x(s: str) -> str:
    """ Given a string, return a version where all the "x" have been removed.
    Except an "x" at the very start or end should not be removed. 
    """
    
    pass

def alt_pairs(s: str) -> str:
    """ Given a string, return a string made of the chars at indexes 0,1, 4,5, 
    8,9 ... so "kittens" yields "kien". 
    """
    
    pass

def do_not_yak(s: str) -> str:
    """ Suppose the string "yak" is unlucky. Given a string, return a version where 
    all the "yak" are removed, but the "a" can be any char. The "yak" strings 
    will not overlap. 
    """
    
    pass

def array_667(numbers: list[int]) -> int:
    """ Given a list of ints, return the number of times that two 6's are next to 
    each other in the list. Also count instances where the second "6" is 
    actually a 7.
    """
    
    pass

def no_triples(numbers: list[int]) -> bool:
    """ Given a list of ints, we'll say that a triple is a value appearing 3 times 
    in a row in the list. Return true if the list does not contain any triples. 
    """
    
    pass

def pattern_51(numbers: list[int]) -> bool:
    """ Given a list of ints, return true if it contains a 2, 7, 1 pattern --
    a value, followed by the value plus 5, followed by the value minus 1. 
    """
    
    pass