#Let's continue examining words. You are given two strings with words separated by commas. Try to find what is common between these strings. The words in the same string don't repeat.
#Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

#Input: Two arguments as strings.
#Output: The common words as a string.
#Precondition:
#Each string contains no more than 10 words.
#All words separated by commas.
#All words consist of lowercase latin letters.

def checkio(line1: str, line2: str) -> str:
    '''
        Compares two strings and returns all substrings(seperated by ","s) that occur across both strings.
    '''
    
    firstWords = set(line1.split(","))
    seconWords = set(line2.split(","))
    
    sames = []
    for i in firstWords:
        if i in seconWords:
            sames.append(i)
    
    sames.sort()
    
    outval = ""
    for i in sames:
        outval += f"{i},"
    
    print(outval.strip(","))
    return outval.strip(",")

if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
