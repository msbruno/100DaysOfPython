def quick_sort(array:list):

    if len(array) <2 :
        return array
        
    pivot_index = int(len(array)/2)
    number = array[pivot_index]
    smallers = [n for n in array if n < number]
    biggers = [n for n in array if n > number]
    equals = [n for n in array if n == number]
    result = quick_sort(smallers)
    result.extend(equals)
    result.extend(quick_sort(biggers))
    return result

test = quick_sort([1,5,2,3,3,6])
assert[1,2,3,3,5,6] == test, 'test: "%s"' % test

test = quick_sort([1,5,2,3,4,6])
assert[1,2,3,4,5,6] == test, 'test: "%s"' % test
