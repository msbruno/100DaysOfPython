def binary_search(array:list, element_to_find:int):
    start = 0
    end = len(array) - 1
    count = 0
    
    while start < end:
        selected_index = int((start + end)/ 2)
        selected = array[selected_index]
        count += 1

        if selected > element_to_find:
            end = selected_index
        elif selected < element_to_find:
            start = selected_index
        elif selected == element_to_find:
            return selected_index, count
    return None, count

array = [1,2,3,4,5,6,7,8,9,10]
index, leaps =  binary_search(array, 3)
assert 2 == index
assert 2 == leaps

index, leaps =  binary_search(array, 5)
assert 4 == index
assert 1 == leaps

index, leaps =  binary_search(array, 9)
assert 8 == index
assert 4 == leaps    
