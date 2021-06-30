#I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?

#Input: A quantity of portions wheat as a positive integer.
#Output: The number of fed pigeons as an integer.
#Precondition: 0 < N < 10 5 .

def checkio(number:int) -> int:
    '''
    Takes in an amount of food, and returns the number of birds feedable with that food
    Assumes that every minute the number of birds increases by n+1
    '''
    
    birds = [0]
    bird_incoming = 2
    
    while number > 0:
        if number > len(birds):
            number -= len(birds)
            birds = [ i+1 for i in birds ]
        else:
            for i in range(0, len(birds)):
                if number > 0:
                    birds[i] += 1
                    number   -= 1
        
        birds.extend( [ 0 for i in range(0, bird_incoming) ] )
        bird_incoming += 1
    
    print(birds)
    return len( [i for i in birds if i != 0 ] )
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"