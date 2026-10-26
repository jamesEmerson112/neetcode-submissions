class Node:
    def __init__(self, val, nextNode = None, prevNode = None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        newNode = Node(value)
        last = self.tail.prev

        last.next = newNode
        newNode.prev = last
        newNode.next = self.tail
        self.tail.prev = newNode


    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        first = self.head.next

        first.prev = newNode
        newNode.prev = self.head
        newNode.next = first
        self.head.next = newNode
        

    def pop(self) -> int:
        # check if it is empty:
        if self.isEmpty():
            return -1

        temp = self.tail.prev
        value = temp.val
        prev_node = temp.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        temp    = self.head.next
        value   = temp.val
        next_node = temp.next

        next_node.prev = self.head
        self.head.next = next_node

        return value

        
