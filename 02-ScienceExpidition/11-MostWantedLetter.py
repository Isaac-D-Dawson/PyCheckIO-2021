#You are given a text, which contains different English letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
#While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
#If you have two or more letters with the same frequency , then return the letter which comes first in the Latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

#Input: A text for analysis as a string.
#Output: The most frequent letter in lower case as a string.
#Precondition :
#A text contains only ASCII symbols.
#0 < len(text) ≤ 10^5

def checkio(text: str) -> str:
    '''
        Takes a piece of text and returns the most common letter inside.
        If all letters have the same value, returns the one that comes first in the latin alphabet
    '''
    
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
    
    text = text.lower()
    counts = []
    
    for i in set(text):
        if i in alphabet:
            counts.append([i, text.count(i)])
    counts = sorted(counts, key = lambda i: (i[1], -alphabet.index(i[0])))
    
    return counts[-1][0]
    

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    
    assert checkio("abbcc") == "b", "Just to make sure it doesn't skip letters"
    print("The local tests are done.")
