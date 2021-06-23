#You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
#- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
#- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
#Here you can find some useful information about the 12-hour format .

#Input: Time in a 24-hour format (as a string).
#Output: Time in a 12-hour format (as a string).
#Precondition :
#'00:00' <= time <= '23:59'

def time_converter(time:str) -> str:
    '''
        Takes a human-readable time in 24 hour format as a string and 
        returns the same string in 12-hour format
    '''
    
    hours    = int( time[0:2] )
    minuites =      time[3:]
    
    if hours      >  11:
        outval    =  " p.m."
    else:
        outval    =  " a.m."
    if hours      >  12:
        hours     = f"{int(hours)-12}"
    if hours      == 0:
        hours     =  12
    
    outval = f"{hours}:{minuites}{outval}"
    
    return outval
    

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    
    assert time_converter("00:00") == "12:00 a.m.", "Midnight check, Initially failed this"
    print("Coding complete? Click 'Check' to earn cool rewards!")