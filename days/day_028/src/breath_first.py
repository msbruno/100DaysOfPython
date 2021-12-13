from collections import deque
from dataclasses import dataclass

graph = {
    'root': 'A',
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : [],
    'E' : ['F', 'G'],
    'F' : [],
    'G' : []
} 

is_on = {
    'A':False,
    'B': False,
    'C': False,
    'D': True,
    'E': False,
    'F': False,
    'G': False,
    }


@dataclass
class Result:
    node: float
    visited_nodes_count: int

class ElementNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__("No element ON was found!")
  

def find_is_on_breath_first(graph:dict, is_on:dict):
    queue = deque(graph['root'])
    count = 0

    while len(queue) > 0:
        element = queue.popleft()
        count += 1

        if is_on[element]:
            return Result(element, count)
        queue += graph[element]
    raise ElementNotFoundException()

result = find_is_on_breath_first(graph, is_on)
assert result == Result('D', 4)

is_on['D'] = False
is_on['G'] = True
result = find_is_on_breath_first(graph, is_on)
assert result == Result('G', 7)

is_on['G'] = False
try:
    result = find_is_on_breath_first(graph, is_on)
    raise Exception("It was expected an exception in program.")
except Exception as e:
    assert type(e) is ElementNotFoundException 
