# This is a continuation of 18-YAMLSimpleDict, and is mostly an expanded rewrite. Check that file in the same directory for more info

# This is the second task on parsing YAML. It represents the next step where parsing gets more complicated. The data types, such as null and bool, are being added, and besides that, you’re getting the ability to use quotes in strings.
# Here are some of the examples:

# name: "Bob Dylan"
# children: 6
# {
  # "name": "Bob Dylan", 
  # "children": 6
# }

# As you can see, the string can be put in quotes. It can be both double and single quotes.

# name: "Bob Dylan"
# children: 6
# alive: false
# {
  # "name": "Bob Dylan", 
  # "alive": False, 
  # "children": 6
# }
# true and false are the keywords defining the boolean type.

# name: "Bob Dylan"
# children: 6
# coding:
# {
  # "coding": None, 
  # "name": "Bob Dylan", 
  # "children": 6
# }
# If no value is specified, it becomes undefined. There also is a keyword for this - null.

# Input: A format string.
# Output: An object.
# Precondition: YAML 1.2 is being used with JSON Schema .


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


def sub_check(a) -> bool:
    '''
        Returns if an objet is subscriptable
        A less bulky alternative to "has __getattribute__"
        
        Ideally would be a method call but i'm not touching that right now.
    '''
    return hasattr(a, '__getitem__')

def yaml(a):
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
            j = [x for x in i[0].strip(" ") if x not in ['\\'] ]
            k = [x for x in i[1].strip(" ") if x not in ['\\'] ]
            
            print(j)
            print(k)
            
            j2 = ""
            k2 = ""
            
            for x in j:
                j2 += str(x)
            for x in k:
                k2 += str(x)
            
            
            if   k2 == "false":
                 k2  =  False
            elif k2 == "":
                 k2  =  None
            elif k2 == "null" and k2 != '"null"':
                 k2  =  None
            elif k2 == '"null"':
                 k2  =  "null"
            
            
            if  j2[0] == '"':
                j2    = j2[1:-1]
            if  sub_check(k2) and k2[0] == '"':
                k2    = k2[1:-1]
            
            
            if sub_check(k2) and k2.isnumeric():
                k2 = int(k2)
            
            
            
            print(j2)
            print(k2)
            
            outval[j2] = k2
            
    
    print(outval)
    return outval


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}, "false equals False"
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}, "'' Equals None"
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}, "null = None"
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}, "\"null\" equals null" #Need to move the "null" check to before the " strip.
    print("Coding complete? Click 'Check' to earn cool rewards!")
