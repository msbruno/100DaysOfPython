def insertion_sort(array:list):
    array_size = len(array)
    result = array.copy()

    for index in range(0, array_size):
        selection = index
        number = array[selection]
        
        for index_comparable in reversed(range(0, index+1)):
            number_comparable = result[index_comparable]

            if number_comparable > number  :
                result[index_comparable] = number
                result[selection] = number_comparable
                selection = index_comparable
    return result
  
  
assert [1,2,3,4,5] == insertion_sort([5,4,3,2,1])
assert [-2,-1,0,1,2,3,4,5,6,7,8,9,10,20] == insertion_sort([5,4,3,2,1,-2,-1,0,20,10,7,8,9,6])
