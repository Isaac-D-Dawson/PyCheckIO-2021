#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

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
    
    if len(a) % 2 == 1:	#Check if the input is even
        a  += "_"		#if not, make it even with a blank character
        
	#assign an output variable
    outval  = []		
    
    while len(a) > 1:					#as long as there's something to work with (since 0 is technically even this is needed for blank strings)
        outval.append(f"{a[0]}{a[1]}")	#append the first two characters into the outval
        a = a[2:]						#Reset the input to remove the two chars we just added.
        
        
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
