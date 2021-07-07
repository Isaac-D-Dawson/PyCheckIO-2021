#In a given list the first element should become the last one. An empty list or list with only one element should stay the same.
#Example: [1,2,3,4] = [2,3,4,1]

#Input: List.
#Output: Iterable.

from typing import Iterable

def replace_first(items: list) -> Iterable:
    '''
        Returns a copy of the input with the first item placed at the end. if the input contains one or less items, it returns unchanged
    '''
    
    
    if len(items) > 1:
        print(items)
        items.append(items[0])
        items  = items[1:]
        print(items)
    
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
