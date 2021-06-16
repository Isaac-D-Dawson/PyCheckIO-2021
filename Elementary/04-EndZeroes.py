# Try to find out how many zeros a given number has at the end.

# Input: A positive Int
# Output: An Int.

def end_zeros(num: int) -> int:
	'''
		Returns the number of "0" characters present on the end of an int
	'''
    
    inval = str(num)
    outval = 0
    
    while len(inval) > 0 and inval[-1] == "0":
        outval += 1
        inval = f"{inval[0:-1]}"
        
    
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
