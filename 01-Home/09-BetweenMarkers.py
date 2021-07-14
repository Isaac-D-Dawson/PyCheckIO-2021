#V2.0: initial program, improved from V1.0, which meets all requirements provided.
#V2.1: added comments explaining logic.

#This is a more advanced version of "13-BetweenMarkers-simple.py" from the "Elementary" folder.
#This was written from scratch, with no input from that file, but if you want to go look at it, you know where it is now.

#You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
#The initial and final markers are always different.
#If there is no initial marker, then the first character should be considered the beginning of a string.
#If there is no final marker, then the last character should be considered the ending of a string.
#If the initial and final markers are missing then simply return the whole string.
#If the final marker comes before the initial marker, then return an empty string.

#Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#Output: A string.
#Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    
    if begin in text:
        begin = text.index(begin) + len(begin)	#if there's a valid beginning character, grab it's index
    else:										#Note we subtract the length of the beginning, as it's exclusive, not inclusive.
        begin = 0								#if not, assume it starts at the start.
    
    if end in text:
        endin = text.index(end)					#if the end char is valid, save that as the end.
    else:
        return text[begin:]						#otherwise, just return it from the beginning
		#The end is already the end and it saves us dealing with everything else.
        
    if begin < endin:
        return text[begin:endin]				#Return the values between the beginning and the end, if the beginning is before the end.
    else:
        return ""								#optherwise, return nothing
        


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
