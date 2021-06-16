#You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

#Input: Array.
#Output: Array or two arrays.

def split_list(items: list) -> list:
    '''
        Evenly divides a list in two. If they cannot be divided evenly, the first lsit will be larger.
        If the input is empty, two empty lists are returned.
    '''
    
    outval = [[], []]
    
    if items != []:
        if len(items) % 2 == 1:
            i = 0
            j = -i-1
            while i < int(len(items)/2):
                outval[0].append(items[i])
                outval[1].append(items[j])
                i += 1
                j -= 1
            
            outval[0].append(items[i])
            outval[1].reverse()
        else:
            for i in range(0, int(len(items)/2)):
                outval[0].append(items[i])
            for j in range(int(len(items)/2), len(items)):
                outval[1].append(items[j])
    
    return outval


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
