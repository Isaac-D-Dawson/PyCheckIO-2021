def remove_brackets(line: str) -> str:
    
    outval = ""
    
    while line != "":
        targets = ["()", "[]", "{}"]
        
        for i in targets:
            j = i[0]
            k = i[1]
            
            if i in line:
                count = line.count(i)
                outval += i * line.count(i)
                line = line.replace(i, "")
                
            if j in line and k not in line:
                line = line.replace(j,"")
                
            if k in line and j not in line:
                line = line.replace(k,"")
    
        print(line)
        print(outval)
    
    return outval

if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
