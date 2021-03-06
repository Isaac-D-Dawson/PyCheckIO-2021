#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#You are given a string where you have to find its first word.
#When solving a task pay attention to the following points:
#There can be dots and commas in a string.
#A string can start with a letter or, for example, a dot or space.
#A word can contain an apostrophe and it's a part of a word.
#The whole text can be represented with one word and that's it.

#Input: A string.
#Output: A string.
#Precondition: the text can contain a-z A-Z , . '

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text = [i for i in text.split(".")]	#split sentences by "." chars (why...did I use a comprehension?)
    
	#glues those string back together with a loop and spaces.
    inval = ""
    for i in text:
        inval += f" {i}"
    text = inval
    
    text = [f"{i} " for i in text.split(",")]	#splits it again in the same way, sticks it back togethe too...Hmm.
    inval = ""
    for i in text:
        inval += f" {i}"
    text = inval
    
    text = text.split(" ")	#Finally, a sane split.
    
    while text[0] == "":	#Deletes all empty intro sections.
        text.pop(0)
   
    return text[0] #returns the first word it finds.


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
