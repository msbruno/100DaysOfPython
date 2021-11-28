# solution for https://www.hackerrank.com/challenges/crush/problem
# O(len(queries) + n)
def array_manipulation(n, queries):
    max_sum = 0
    array_sum = [0] * n

    for index in range(len(queries)):
        start = queries[index][0]-1
        end = queries[index][1]-1
        number = queries[index][2]
        array_sum[start] += number
        if end + 1 < len(array_sum):
            array_sum[end + 1 ] -= number
    sum = 0 
    print(array_sum)
    for index in range(len(array_sum)):
        sum += array_sum[index]
        if sum > max_sum:
            max_sum = sum
    return max_sum


arr = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
result = array_manipulation(10, arr)
print(result)
assert result == 10

arr = [[2, 6, 8], [3, 5, 7],[1, 8, 1],[5, 9, 15]]
result = array_manipulation(10, arr)
print(result)
assert result == 31
