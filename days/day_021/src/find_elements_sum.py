# Find elements where in array where sum is pre-defined

def find_elements_sum_is(arr:list, sum:int):
    number_dict = {}

    for number in arr:
        complement = sum - number 

        if complement in number_dict:
            return [number, complement]
            
        number_dict[number] = True
    return []


assert find_elements_sum_is([5,3,4,5], 10) == [5,5]
assert find_elements_sum_is([10, 0,3,4,5], 10) == [0, 10]
assert find_elements_sum_is([10], 10) == []
assert find_elements_sum_is([10, 0], 10) == [0, 10]
