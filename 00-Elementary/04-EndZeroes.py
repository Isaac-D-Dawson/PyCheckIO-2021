#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

# Try to find out how many zeros a given number has at the end.

# Input: A positive Int
# Output: An Int.

def end_zeros(num: int) -> int:
	'''
		Returns the number of "0" characters present on the end of an int
	'''
    
	#assign variables
    inval = str(num)
    outval = 0
    
	#loop for as long as the number ends in "0" chars (And as long as there is a number to check)
    while len(inval) > 0 and inval[-1] == "0":
        outval += 1					#increase our count by one.
        inval = f"{inval[0:-1]}"	#Re-assign our input to remove the last char(the one we just counted)
        
    
    return outval


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
