#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#Let's teach the Robots to distinguish words and numbers.
#You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession . For example, the string "start 5 one two three 7 end" contains three words in succession.

#Input: A string with words.
#Output: The answer as a boolean.
#Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
#0 < len(words) < 100

def checkio(words: str) -> bool:
    '''
        Returns True if the string contains at least three words in a row. Otherwise returns False
    '''
    
    counter = 0
    
    for i in words.split(" "):		#split the input into words.
        if i.isnumeric() == False:	#check it's a word and not a number
            counter += 1
        else:
            counter = 0
            
        if counter == 3:	#if we find three in a row, return True.
            return True
    
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
