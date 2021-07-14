#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#In a given string you should reverse every word, but the words should stay in their places.

#Input: A string.
#Output: A string.
#Precondition: The line consists only from alphabetical symbols and spaces.

def backward_string_by_word(text: str) -> str:
    '''
        Reverses all substrings separated by spaces present in the input string.
    '''
    
    inval = text.split(" ")			#separates all words
    
    for i in range(0, len(inval)):	#gets the index of each word
        inval[i] = inval[i][::-1]	#assigns the item at each index to be a reverse of itself.
		#This reverse slice is really clever, and it pops up a lot more later on.
		#After all, once you find a handy tool, you try to use it everywhere
    
    outval = ""				#start with a blank output
    for i in inval:			#for each reversed word in the input
        outval += f"{i} "	#add it to the output, with a space on the end.
    
    return outval.strip()	#return the output, and remove that extra space right on the end.


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
    assert backward_string_by_word('velask friend') == 'ksalev dneirf'
