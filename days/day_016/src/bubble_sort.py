def bubble_sort(array:list):
    swapped = True
    result = array.copy()

    while swapped:

        swapped = False

        for index in range(0, len(result)-1):
            current = result[index]
            next = result[index+1]

            if current > next:
                swapped = True
                result[index] = next
                result[index+1] = current 
    return result


assert [1,2,3,4,5] == bubble_sort([5,2,3,4,1])
assert [1,2,3,4,5,6,7,8,9,10, 11] == bubble_sort([5,2,3,4,1,11,9,8,7,10,6])
