#V1.0. A future puzzle uses this same mechanic, and this file may be referred back to.
#V1.1: added comments explaining logic.

#You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.
#This is a simplified version of the Between Markers mission.
#The initial and final markers are always different.
#The initial and final markers are always 1 char size.
#The initial and final markers always exist in a string and go one after another.

#Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#Output: A string.
#Precondition: There can't be more than one final and one initial markers.

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    
    inval = text.split(begin)		#split the text on the beginning marker
    return inval[-1].split(end)[0]	#Grab the latter half of that text, and then split that on the ending marker and return the first half of that.


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
