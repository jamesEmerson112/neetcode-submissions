class Node:
    def __init__(self, key, val, left = None, right = None):
        self.key = key # order
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if self.root is None:
            self.root = newNode
            return

        current = self.root
        while current is not None:
            if key < current.key:
                if current.left is None:
                    current.left = newNode
                    return
                current = current.left
            
            elif key > current.key:
                if current.right is None:
                    current.right = newNode
                    return
                current = current.right
            
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        if self.root is None:
            return -1

        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        
        return -1

    def getMin(self) -> int:
        if self.root is None:
            return -1

        current = self.root
        while current is not None:
            if current.left is None:
                return current.val
            current = current.left

        return -1

    def getMax(self) -> int:
        if self.root is None:
            return -1

        current = self.root
        while current is not None:
            if current.right is None:
                return current.val
            current = current.right
        return -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, current: Node, key: int) -> Node:
        if not current:
            return None

        if key > current.key:
            current.right = self.removeHelper(current.right, key)
        elif key < current.key:
            current.left = self.removeHelper(current.left, key)
        else:
            # No left child
            if current.left is None:
                return current.right

            # no right child
            if current.right is None:
                return current.left

            # Case 
            successor = self.findMinNode(current.right)

            current.key = successor.key
            current.val = successor.val

            current.right = self.removeHelper(current.right, successor.key)
        return current

    def findMinNode(self, current: Node) -> Node:
        while current.left is not None:
            current = current.left

        return current

    def getInorderKeys(self) -> List[int]:
        keys = []
        def inorder(current):
            if current is None:
                return

            inorder(current.left)
            keys.append(current.key)
            inorder(current.right)

        inorder(self.root)
        return keys
