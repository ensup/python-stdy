def is_pal_v1(str):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_pal_v1('noon')
    True
    >>> is_pal_v1('racecar')
    True
    >>> is_pal_v1('dented')
    False
    """
    return str == reverse(str)
def reverse(str):
    rev=''
    for char in str:
        rev=char+rev
    return rev
