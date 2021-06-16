#Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
#Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
#Your task is simple - convert the input date and time from computer format into a "human" format.

#Input: Date and time as a string
#Output: The same date and time, but in a more readable format
#Precondition :
#0 < date <= 31
#0 < month <= 12
#0 < year <= 3000
#0 < hours < 24
#0 < minutes < 60

#Technically there's a precondition about the order the data is formatted in, but still nigh impossible to check sanely.
def date_time(time: str) -> str:
    '''
        Takes a date and time as a string, and returns them in a human-readable format.
    '''
    
    
    months = {
        "01" : "January"    ,
        "02" : "Febuary"    ,
        "03" : "March"      ,
        "04" : "April"      ,
        "05" : "May"        ,
        "06" : "June"       ,
        "07" : "July"       ,
        "08" : "August"     ,
        "09" : "September"  ,
        "10" : "October"    ,
        "11" : "November"   ,
        "12" : "December"
             }
    
    date = time.split(" ")[0].split(".")
    time = time.split(" ")[1].split(":")
    
    if time[0] == "01":
        time.append("hour")
    else:
        time.append("hours")
        
    if time[1] == "01":
        time.append("minute")
    else:
        time.append("minutes")

    return f"{int(date[0])} {months[date[1]]} {date[2]} year {int(time[0])} {time[2]} {int(time[1])} {time[3]}"

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    
    assert date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute", "Failed Check 1, time/s"
    print("Coding complete? Click 'Check' to earn cool rewards!")
