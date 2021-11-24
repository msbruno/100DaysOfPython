def merge_sort(array:list):
    print(array)
    
    if len(array) < 2:
        return array

    pivot_index = len(array)//2
    left_array = array[:pivot_index]
    right_array = array[pivot_index:]

    merged_left  = merge_sort(left_array)
    merged_right = merge_sort(right_array)
    
    result = list()
    left_index = right_index =  0

    while left_index < len(merged_left) and right_index < len(merged_right):
        
        from_left = merged_left[left_index]
        from_right = merged_right[right_index]

        if from_left < from_right:
            result.append(from_left)  
            left_index += 1
        else:
            result.append(from_right)  
            right_index += 1
    
    
    if left_index < len(merged_left):
        result.extend(merged_left[left_index:])

    if right_index < len(merged_right):
        result.extend(merged_right[right_index:])

    return result
    

result = merge_sort([5,2,3,4,1])
assert [1,2,3,4,5] == result
