from collections import deque
queue = deque(['1','2','3'])
queue += ['4','5','6']
queue.appendleft(7)
print(queue)
#deque(['7', '1', '2', '3', '4', '5', '6'])

queue.popleft()
print(queue)
#deque(['1', '2', '3', '4', '5', '6'])

queue.append(7)
print(queue)
#deque(['1', '2', '3', '4', '5', '6', '7'])

queue.popleft()
print(queue)
#deque(['1', '2', '3', '4', '5', '6'])
