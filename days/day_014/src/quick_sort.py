def quick_sort(array:list):

    if len(array) <2 :
        return array
        
    pivot_index = int(len(array)/2)
    number = array[pivot_index]
    smallers = [n for n in array if n < number]
    biggers = [n for n in array if n > number]
    result = quick_sort(smallers)
    result.append(number)
    result.extend(quick_sort(biggers))
    return result



assert [1,2,3,4,5] == quick_sort([5,2,3,4,1])
assert [1,2,3,4,5,6,7,8,9,10] == quick_sort([5,2,3,4,1,11,9,8,7,10,6])

