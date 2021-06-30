def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    
    if line != "":
        outval = [1]
    else:
        outval = [0]
    
    
    last = ""
    
    for i in line:
        if i == last:
            outval[-1] += 1
        else:
            last = i
            outval.append(1)
    
    outval.sort()
    print(outval)
    return outval[-1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
