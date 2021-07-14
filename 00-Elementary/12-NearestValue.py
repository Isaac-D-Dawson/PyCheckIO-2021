#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#Find the nearest value to the given one.
#You are given a list of values as set form and a value for which you need to find the nearest one.
#For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. If we sort this set in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.
#A few clarifications:
#If 2 numbers are at the same distance, you need to choose the smallest one;
#The set of numbers is always non-empty, i.e. the size is >=1;
#The given value can be in this set, which means that it’s the answer;
#The set can contain both positive and negative numbers, but they are always integers;
#The set isn’t sorted and consists of unique numbers.

#Input: Two arguments. A list of values in the set form. The sought value is an int.
#Output: Int.

def nearest_value(values: set, one: int) -> int:
    '''
        Returns the nearest item in a ist to the provided value.
        If the number is not present in the list, the next nearest is returned.
        If there are multiple equally close itmes, the lowest one is returned.
    '''
    
    
    oneDo = one	#short for one down, this var keeps track of the lowest number to check
    oneUp = one			# meanwhile, this var keeps track of the highest number to check
    
    while True:				#an infinite loop. hindsight tells me this could hang on an empty list, but... Wasn't in the requirements or the checks.
        if oneDo in values:	#if the lower value is in the input, return it
            return oneDo
        if oneUp in values:	#if the higher value is in the input, return it.
            return oneUp
        oneDo -= 1			#if neither were, then we can reduce the lower check by one.
        oneUp += 1			#and increase the higher check by one. Repeat until we find something present in the input.

if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
