def is_pal_v2(str):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_pal_v2('noon')
    True
    >>> is_pal_v2('racecar')
    True
    >>> is_pal_v2('dented')
    False
    """
    l=len(str)
    return str[:l//2]==reverse(str[l-l//2:])
def reverse(str):
    rev=''
    for char in str:
        rev=char+rev
    return rev
