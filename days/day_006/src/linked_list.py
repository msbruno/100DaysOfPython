#Using __next__ and __iter__ to create a iterable list 

class Node:

    def __init__(self, value):
        self.__next = None
        self.value = value

    def set_next(self, next_node):
        self.__next = next_node
        
    def get_next(self):
        return self.__next

class LinkedList:

    def __init__(self, head:Node):
        self.__head = head
        self.actual = None

    def __iter__(self):
        self.__actual = self.__head
        return self
    
    
    def __next__(self):

        if self.__actual == None:
            raise StopIteration
        result = self.__actual
        self.__actual = result.get_next()
        return result

    
#create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#create linked list
linked_list = LinkedList(node1)
node1.set_next(node2)
node2.set_next(node3)

#test
iterator = iter(linked_list)
node = next(iterator)
assert node.value == 1
node = next(iterator)
assert node.value == 2
node = next(iterator)
assert node.value == 3



