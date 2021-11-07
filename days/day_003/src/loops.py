
items:list = (5,4,3,2,1)

#foreach
def sum_greaters_than_three_using_for(items_list):
    result = 0
    for item in items_list:
        if item <= 3:
            result += item
    return result

def sum_greaters_than_three_using_comprehension(items_list):
    result = 0
    [result:= result + item if item <= 3 else 0 for item in items_list ]
    return result


assert sum_greaters_than_three_using_for(items) == 6
assert sum_greaters_than_three_using_comprehension(items) == 6