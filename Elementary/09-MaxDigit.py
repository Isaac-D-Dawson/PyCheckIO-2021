#You have a number and you need to determine which digit in this number is the biggest.

#Input: A positive int.
#Output: An Int (0-9).

def max_digit(number: int) -> int:
    '''
        Returns the largest digit component of a given integer. If there is only one digit, it will return that instead.
    '''
    
    
    inval = [i for i in str(number)]
    
    inval.sort()
    
    return int(inval[-1])


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
