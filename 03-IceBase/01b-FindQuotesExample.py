#Your task at hand is to find all the quotes in a given text. And, as per usual, do everything as quickly as possible. 😉
#You are given a string that consists of characters and a paired number of quotation marks. You need to return an Iterable consisting of the texts inside the quotation marks. But choose only quotes with double quotation marks ("). Single quotation marks (') aren’t appropriate.

#Input: A string.
#Output: An iterable.

def find_quotes(a:str) -> list:
	'''
		This is an example function that shows the hubris of the ".index()" method. Duplicate items cause this function to break.
		Head my words and learn from thy mistakes.
	'''
    
    #sperates the input by " characters
    inval = a.split('"')
    print("Inval looks like")
    print(inval)
    #Assigns output as an empty list
    outval = []
    
    #If there is more than one item in the input variable...
    if len(inval) > 1:
        pass
        
        #outval = [ i for i in inval if inval.index(i) % 2 == 1 ]
        #outval = [ i if (inval.index(i) % 2 == 1) for i in inval ]
        
        #...Cycle through all items in the input variable...
        for i in inval:
            
            print("index of i is:")
            print(inval.index(i))
            #... and if they are odd...
            if inval.index(i) % 2 == 1:
                print(f"{i} added to outval")
                #...Apend them to the output variable
                outval.append(i)
            else:
                print(f"{i} WAS NOT added to inval")
    
    #print the input and output variables, return the output variable.
    print("input was")
    print(inval)
    print("output is")
    print(outval)
    return outval
    
    print(0%2)
    print(1%2)
    print(2%2)
    print(-1%2)
    
if __name__ == '__main__':
    print("Example:")
    print(find_quotes('"Greetings"'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
 'of the printing and typesetting '
 'industry. Lorem Ipsum has been the '
 '"industry\'s standard dummy text '
 'ever since the 1500s", when an '
 'unknown printer took a galley of '
 'type and scrambled it to make a type '
 'specimen book. It has survived not '
 'only five centuries, but also the '
 'leap into electronic typesetting, '
 'remaining essentially unchanged. "It '
 'was popularised in the 1960s" with '
 'the release of Letraset sheets '
 'containing Lorem Ipsum passages, and '
 'more recently with desktop '
 'publishing software like Aldus '
 'PageMaker including versions of '
 'Lorem Ipsum.') == ['Lorem Ipsum',
 "industry's standard dummy text ever "
 'since the 1500s',
 'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == [''], "Return single empty"
    print("Coding complete? Click 'Check' to earn cool rewards!")
