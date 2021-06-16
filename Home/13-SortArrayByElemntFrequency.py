#Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

#Input: Iterable
#Output: Iterable
#Precondition: elements can be ints or strings

def freq_subsort(a: list, b) -> tuple:
    '''
        A subfunction designed to return the count and index of a given item from a given list.
        Designed to be used in a lambda funtion as a sort key.
    '''
    
    return (-a.count(b), a.index(b) )

def frequency_sort(items: list) -> list:
    '''
        Sorts items by their frequency. Items with the same frequency occur in the order they apper in the original list
    '''
    
    #outval = sorted(items, key = lambda i:( -items.count(i), items.index(i)))
    outval = sorted(items, key = lambda i:freq_subsort(items, i) )
    
    return outval


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
