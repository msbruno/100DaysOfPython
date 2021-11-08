
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        node = self.head
        nodes = list()

        while node is not None:
            nodes.append(node.data)
            node = node.next
        return ",".join(nodes)

   
linked = LinkedList()
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")

linked.head = node1
node1.next = node2
node2.next = node3

assert node1.next == node2
assert node2.next == node3
assert node3.next == None
assert "1,2,3" == str(linked)