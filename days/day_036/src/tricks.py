
# Sorting
lst = [[5,5],[1,2],[3,3],[2,2],[4,4]]
lst.sort(key = lambda inner: inner[0])
print(lst)
#[[1, 2], [2, 2], [3, 3], [4, 4], [5, 5]]

# arg packing
def multi(*args):
    result = 1

    for arg in args:
        result = result * arg
    return result

print(multi(1,2,5))
#10

# Decompose
tpl = (1,2)
x,y = tpl
print(x,y)
# 1 2