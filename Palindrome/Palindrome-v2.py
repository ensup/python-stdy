def is_pal_v2(str):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_pal('noon')
    True
    >>> is_pal('racecar')
    True
    >>> is_pal('dented')
    False
    """
    l=len(str)
    return str[:l//2]==reverse(str[l-l//2:])
def reverse(str):
    rev=''
    for char in str:
        rev=char+rev
    return rev
