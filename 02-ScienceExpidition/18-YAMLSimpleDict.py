#Have you ever heard of such markup language as YAML ? It’s a friendly data serialization format. In fact it’s so friendly that both people and programs can read it quite well. You can play around with the standard by following this link .
#YAML is a text, and you need to convert it into an object. But I’m not asking you to implement the entire YAML standard, we’ll implement it step by step.
#The first step is the key-value conversion. The key can be any string consisting of Latin letters and numbers. The value can be a single-line string (which consists of spaces, Latin letters and numbers) or a number (int).
#I’ll show some examples:
#name: Alex
#age: 12
#Converted into an object.
#{ 
#  "name": "Alex",
#  "age": 12
#}
# Note that the number automatically gets type int
#Another example shows that the string may contain spaces.
#name: Alex Fox
#age: 12
#class: 12b
#Will be converted into the next object.
#{
#  "age": 12, 
#  "name": "Alex Fox", 
#  "class": "12b"
#}
#Pay attention to a few things. Between the string "age" and the string "class" there is an empty string that doesn’t interfere with parsing. The class starts with numbers, but has letters, which means it cannot be converted to numbers, so its type remains a string (str).

#Input: A format string.
#Output: An object.
#Precondition: YAML 1.2 is being used with JSON Schema .

def yaml(a:str) -> dict:
    '''
        Takes a milti-line-string and converts it into a YAML object
    '''
    
    inval = a.split("\n")
    midval = []
    outval = {}
    
    for i in inval:
        j = i.split(":")
        midval.append(j)
    midval.sort()
    
    for i in midval:
        if i != [""]:
            j = i[0].strip(" ")
            k = i[1].strip(" ")
        
            if k.isnumeric():
                outval[j] = int(k)
            else:
                outval[j] = str(k)
    
    
    return outval
    


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
