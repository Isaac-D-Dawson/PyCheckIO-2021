#Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

#Input: A string.
#Output: An iterable of strings.
#Precondition: 0<=len(str)<=100

def split_pairs(a: str) -> list:
    '''
        Takes a string as an input, and divides it into strings of length two.
        If the string is an odd length the final letter will be paired with an "_2 character.
        If the string is empty an empty list will be returned instead.
    '''
    
    if len(a) % 2 == 1:
        a  += "_"
        
    outval  = []
    
    while len(a) > 1:
        outval.append(f"{a[0]}{a[1]}")
        a = a[2:]
        
        
    return outval

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
