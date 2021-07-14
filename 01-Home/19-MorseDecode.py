#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#Your task is to decrypt the secret message using the Morse code .
#The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
#If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

#Input: The secret message.
#Output: The decrypted text.
#Precondition :
#0 < len(message) < 100
#The message will consists of numbers and English letters only.

#And spaces, you didn't mention those!


#Thankfully included by default, saves me thing to build my own morse Dictionary >.>
MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9',
         '': ' '
        }
        #Okay, i was mistaken, I had to add a "Space" code, but that's besides the point.

def morse_decoder(code):
    '''
        Takes a string of Morse code and converts it into english text.
    '''
    
    inval = code.split(" ") #split all the letters appart.
    outval = ""
    
    for i in inval:
        outval += (f"{MORSE[i]}")	#convert each letter with the dictionary.
    
	#strip all the extra spaces between the letters and the words.
    outval = outval.replace("  ", " ") #I'm surprised this works? either the check is recursive...
    #...or I've not given it anything with needless extra spaces.
    outval = f"{outval[0].upper()}{outval[1:]}"	#quickly edit in a capital to start the sentence.
    
    return outval 

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    #Note that I've had some instances where code similar to this somehow locked into an infinite loop.
    #I'm not sure why this iteraction doesn't, but be aware this iss has existed.
