# https://www.hackerrank.com/challenges/minimum-swaps-2

def minimum_swaps(arr:list):
    result = 0

    for index in range(0, len(arr)):

        while(index + 1 != arr[index]):
            correct_index_of_current_number = arr[index] - 1 
            current_number = arr[index] 
            number_at_index_of_current_number = arr[correct_index_of_current_number] 
            arr[index] = number_at_index_of_current_number 
            arr[correct_index_of_current_number] = current_number 
            result += 1
            
        index+=1
    return result

assert minimum_swaps([7, 1, 3, 2, 4, 5, 6]) == 5
