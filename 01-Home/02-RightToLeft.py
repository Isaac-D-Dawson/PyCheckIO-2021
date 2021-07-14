#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce instructions on how to get around the ship.
But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.
#You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.

#Input: A sequence of strings.
#Output: The text as a comma-separated string.
#Precondition:
#0 < len(phrases) < 42

def left_join(phrases: tuple) -> str:
    """
        Joins strings and replaces "right" with "left"
    """
    
    inval = ""
    for i in phrases:	#sort inval into individual words real quick.
        inval += f",{i}"
    inval = inval[1:]

    outval = inval			#copy that to outval, and check if it has the word right in it. if it does...
    if "right" in inval:
        outval = ""
        for i in inval.split("right"):		#split on all instances of "right", and glue it back together with the word "left".
            outval = f"{outval}{i}left"
        outval = outval[0:-4]
        
    return outval

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    
    #Beep Boop Beep Boop is robot for "We Support Equality!"
