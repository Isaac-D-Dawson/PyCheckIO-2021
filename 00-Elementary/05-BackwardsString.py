#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

# You should return a given string in reverse order.

# Input: A string.
# Output: A string.

def backward_string(val: str) -> str:
	'''
		Returns a reversed copy of the input string ("string" = "gnirts")
	'''
    
    outval = ""	#assign an output var
    
    while len(val) > 0:			#as long as our input exists(or isn't empty)
        outval += val[-1]		#add the last char of the input to the output.
        val     = f"{val[0:-1]}"#remove the last item of input now we've checked it
    
	#Hindsight tells me that there's a much nicer way to do this with string slices, but I'm not here to improve my code, just document it :P
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
