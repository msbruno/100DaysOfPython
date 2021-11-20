#https://www.hackerrank.com/challenges/new-year-chaos/problem
  
def is_chaotic(current, expected):
    return current - expected > 2

def minimumBribes(q):
    bribes = 0
    size = len(q)

    for index in reversed(range(0, size)):
        current = q[index]
        expected = index + 1
        
        if is_chaotic(current, expected) > 2:
            return "Too chaotic"

        max_bribe = max(q[index] -2, 0)

        for next_index in range(max_bribe, index):
            next_number = q[next_index] 
            if next_number > current:
                bribes += 1

    return bribes
