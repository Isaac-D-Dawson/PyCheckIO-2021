#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.

#Input: An int.
#Output: A bool.
#Precondition: both given ints should be between -1000 and 1000

def is_even(num: int) -> bool:
    '''
        Returns True if the provided number is even.
        Otherwise, returns False.
    '''
    
    return num %2 == 0	#returns True if the input is divisible by 2.


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
