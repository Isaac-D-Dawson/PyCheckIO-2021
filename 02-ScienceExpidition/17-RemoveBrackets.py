def remove_brackets(line: str) -> str:
    
    inval = [i for i in line]
    
    counts = {
        "()" : 0,
        "[]" : 0,
        "{}" : 0
        }
    for i in line:
        if i == "(":
            counts["()"] += 1
        if i == ")":
            counts["()"] -= 1
        if i == "[":
            counts["[]"] += 1
        if i == "]":
            counts["[]"] -= 1
        if i == "{":
            counts["{}"] += 1
        if i == "}":
            counts["{}"] -= 1
    
    
    for i in counts.keys():
        while counts[i] != 0:
            if i[0] in inval and counts[i] > 0:
                inval.pop(inval.index(i[0]))
                counts[i] -= 1
            if i[1] in inval and counts[i] < 0:
                inval.pop(inval.index(i[1]))
                counts[i] += 1
    
    outval = ""
    for i in inval:
        outval += i
            
        
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
