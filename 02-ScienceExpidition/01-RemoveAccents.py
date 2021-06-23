#Assuming you are developing a user based system like facebook, you will want to provide the functionality to search for other members regardless of the presence of accents in a username. Without using a 3rd party collation library, you will need to remove the accents from the username before the comparison.
#é - letter with an accent; e - letter without an accent; ̀ and ́ - the stand alone accents;

#Input: A phrase as a string (unicode).
#Output: An accent free Unicode string.
#How it is used: It might be a part of a username verification process or a system that proposes the username based on the first and last name of a user.
#Precondition: 0≤|input|≤40

#There's...some irony here.
def checkio(in_string: str) -> str:
    '''
        Strips out unicode characters and replaces them with ASCII equivilents.
    '''
    import unicodedata as ud
    
    outval = ud.normalize('NFKD', in_string) #what is the NFKD format??
    return u"".join([c for c in outval if not ud.combining(c)]) #okay, so this is copying everything that's not a diacritic char?

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')

#I don't entirely understand how this works, though I find it ironic that "You shouldn't use third aprty libraries".