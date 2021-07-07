def is_all_upper(text: str) -> bool:
    
    inval = False
    for i in "a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z".split("."):
        if i in text.lower():
            inval = True
    if inval == False:
        return False
    
    if len(text) == 0:
        return False
    return text == text.upper()
    
if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    
    assert is_all_upper("     ") == False , "Truly Empty String"
    print("Coding complete? Click 'Check' to earn cool rewards!")
