#This program was originally written in june of 2020, and was only lightly touched up to make it pass checks in 2021.

# You are given a list of files. You need to sort this list by the file extension. The files with the same extension should be sorted by name.

# Some possible cases:

# Filename cannot be an empty string;
# Files without the extension should go before the files with one;
# Filename ".config" has an empty extension and a name ".config";
# Filename "config." has an empty extension and a name "config.";
# Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
# Filename ".imp.xls" has an extension "xls" and a name ".imp".
# Input: A list of filenames.

# Output: A list of filenames.

from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    
    #Define variables:
    inval = [i for i in files]  #list-comprehension to avoid editing the original list
    outval = []
    
    #Create a searching function
    def locate(a: str) -> int:
        for i in range(len(a)-1, -1, -1):  #go backwards through the string)
            if a[i] == ".":
                return(i)
    
    print(inval)
    
    for i in range(len(inval)):
        if locate(inval[i]) != 0:
            inval[i] = [inval[i][0:locate(inval[i])], inval[i][locate(inval[i]):]]
            print("ping!")
            print(locate(inval[i]))
        else:
            inval[i] = [inval[i][locate(inval[i]):], ""]
            print("Pong!")
    
    print(inval)
    
    
    #for i in sorted(inval, key = lambda x: x[1]):			#Original version
    for i in sorted(inval, key = lambda x: (x[1], x[0])):	#Touched up version
        if i[1] == "":
            outval.append(f"{i[0]}")
        else:
            outval.append(f"{i[0]}{i[1]}")
    
    print(outval)
    return(outval)
    
if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    
    assert sort_by_ext(["1.cad","2.bat","1.aa","1.bat"]) == ["1.aa","1.bat","2.bat","1.cad"], "Extra 2/2, Retaining order of titles"
    print("Coding complete? Click 'Check' to earn cool rewards!")