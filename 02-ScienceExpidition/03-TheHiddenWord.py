#Nicola has solved this puzzle (and I am sure that you will do equally well). To be prepared for more such puzzles, Nicola wants to invent a method to search for words inside poetry. You can help him create a function to search for certain words.
#You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n). Casing does not matter for your search, but whitespaces should be removed before your search. You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines. For this you need envision the rhyme as a matrix (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces).
#The result must be represented as a list -- [row_start,column_start,row_end,column_end] , where
#row_start is the line number for the first letter of the word.
#column_start is the column number for the first letter of the word.
#row_end is the line number for the last letter of the word.
#column_end is the column number for the last letter of the word.
#Counting of the rows and columns start from 1.

#Input: Two arguments. A rhyme as a string and a word as a string (lowercase).
#Output: The coordinates of the word.
#Precondition: The word is given in lowercase
#0 < |word| < 10
#0 < |rhyme| < 300


from itertools import zip_longest

def checkio(text: str, word: str) -> list:
    
    outval = []
    
    text = text.lower().split(" ")
    temp = ""
    for i in text:
        temp += i
    
    inval = [f" {i}" for i in temp.split("\n") ]
    inval.insert(0, " ")
    
    for i in inval:
        if word in i:
            outval = [inval.index(i), i.index(word), inval.index(i), i.index(word) + len(word) -1 ]
    
    if outval == []:
        temp = ""
        for line in zip_longest(*inval, fillvalue='-'):
            #print(line)
            for i in line:
                temp += i
            temp += "\n"
        temp = temp.split("\n")
        
        
        for i in temp:
            if word in i:
                outval = [i.index(word),temp.index(i) , i.index(word) + len(word) -1, temp.index(i) ]
    
    
    return outval

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
