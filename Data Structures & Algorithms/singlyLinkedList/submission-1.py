class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if self.tail == self.head:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode


    def remove(self, index: int) -> bool:
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if not curr or not curr.next:
            return False

        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
        
