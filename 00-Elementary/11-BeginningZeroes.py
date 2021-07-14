#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

#Input: A string, that consist of digits.
#Output: An Int.
#Precondition: 0-9

def beginning_zeros(number: str) -> int:
    '''
        Returns the number of "0" chars present at the beginning of a string.
    '''
    
    i = 0	#create our output variable
    
    if len(set(number)) > 1:	#check that there are two different digits in the number.
    
        while number[i] == "0":	#if there are, cycle through them until you find something that isn't 0
            i += 1				#and add one to our count (which also serves as an index, since w're starting form the start of the number, nifty
    
    else:						#otherwise... there's only one type of digit present
        if "0" in set(number):	#so we see if 0 is that type
            i = len(number)		#and if it is we can just return the length of the number, as it's all "0"s.
    
    return i


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
