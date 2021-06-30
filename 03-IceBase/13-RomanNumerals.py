#Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:
#I, II, III, IV, V, VI, VII, VIII, IX, and X.
#The Roman numeral system is decimal based, but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:
#Numeral Value
#I   	1 (unus)
#V	    5 (quinque)
#X	    10 (decem)
#L	    50 (quinquaginta)
#C	    100 (centum)
#D	    500 (quingenti)
#M	    1,000 (mille)
#More additional information about Roman numerals can be found on the Wikipedia article.
#For this task, you should return a Roman numeral using the specified integer value ranging from 1 to 3999.

#Input: A number as an integer.
#Output: The Roman numeral as a string.
#Precondition: 0 < number < 4000

def checkio(data:int) -> str:
    '''
        A minimally viable roman-numeral encoder. Converts an int into a string of roman numerals
    '''
    
    outval = ""
    roman = {
        1000 : "M", 900 : "CM", 500 : "D", 400 : "CD",
         100 : "C",  90 : "XC",  50 : "L",  40 : "XL",
          10 : "X",   9 : "IX",   5 : "V",   4 : "IV",
           1 : "I"
        }
    
    for i in roman.keys():
        while data >= i:
            data -= i
            outval += roman[i]
    
    return outval
        
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')