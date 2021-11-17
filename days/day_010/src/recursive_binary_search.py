def recursive_binary_search(array:list, element_to_find:int, start:int=0, end:int=len(array)-1, leaps:int=0):
    if start == end:
        return None, leaps

    selected_index = int((start + end) / 2)
    selected_element = array[selected_index]
    leaps += 1

    if selected_element == element_to_find:
        return selected_index, leaps

    elif element_to_find < selected_element:
        end = selected_index 
    elif element_to_find > selected_element:
        start = selected_index

    return recursive_binary_search(array, element_to_find, start, end, leaps)

array = [1,2,3,4,5,6,7,8,9,10]
index, leaps =  recursive_binary_search(array, 3)

assert 2 == index
assert 2 == leaps

index, leaps =  recursive_binary_search(array, 5)
assert 4 == index
assert 1 == leaps

index, leaps =  recursive_binary_search(array, 9)
print(index)
print(leaps)
assert 8 == index
assert 4 == leaps    
