# You should return a given string in reverse order.

# Input: A string.
# Output: A string.

def backward_string(val: str) -> str:
	'''
		Returns a reversed copy of the input string ("string" = "gnirts")
	'''
    
    outval = ""
    
    while len(val) > 0:
        outval += val[-1]
        val     = f"{val[0:-1]}"
    
    return outval


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
