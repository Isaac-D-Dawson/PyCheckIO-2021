#See also: 
Acceptable Password I	(00-elementary			/	02-AcceptablePasswordV1.py),
Acceptable Password II	(04-ElectronicsStation	/	03-AcceptablePasswordV2.py)

#In this mission you need to create a password verification function.
#Those are the verification conditions:

#the length should be bigger than 6;
#should contain at least one digit, but cannot consist of just digits.

#Input: A string.
#Output: A bool.


def is_acceptable_password(password: str) -> bool:
    '''
        Checks if a password meets a list of conditions
    '''
    
    outval = []
    
    if len(password) > 6:
        outval.append(True)
    else:
        outval.append(False)
    
    digitCheck = []
    for i in range(0, 10):
        if str(i) in password:
            digitCheck.append(True)
    if len(digitCheck) > 0:
        outval.append(True)
    else:
        outval.append(False)
    
    letterCheck = []
    for i in "a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z".split("."):
        if i in password:
            letterCheck.append(True)
    if len(letterCheck) > 0:
        outval.append(True)
    else:
        outval.append(False)
    
    if False not in outval:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
