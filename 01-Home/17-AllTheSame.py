#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#In this mission you should check if all elements in the given list are equal.

#Input: List.
#Output: Bool.
#Precondition: all elements of the input list are hashable

#Part of the original setup
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    '''
        Takes a list of elements and returns True if they are all equal.
        Otherwise returns False.
    '''
    
    outval = True						#assume they all natch until proven wrong.
    for i in range(0, len(elements)-1):	#cycle through the list.
        if elements[i] != elements[i+1]:#if an item and it's sucessor aren't equal, the result is instantly false.
            outval = False
			#cout probaably make this a little more efficient, but not my job rn...
    
    return outval        


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
