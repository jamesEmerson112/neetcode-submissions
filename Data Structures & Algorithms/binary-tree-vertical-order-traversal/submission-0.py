# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# import queue (dequeue)
from collections import deque, defaultdict
from typing import List, Optional

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # implment BFS
        if not root:
            return []
        
        # BFS the root
        q = deque()
        q.append((root, 0))  # (node, column)
        # traverse the tree and print out the node
        # Since columns can be negative (like the -1 you're generating for left children), a defaultdict(list) would be perfect for collecting the node.val associated with each col index as you traverse.
        col_table = defaultdict(list)
        while q:
            node, col = q.popleft()
            if node:
                col_table[col].append(node.val)
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        sorted_keys = sorted(col_table.keys())

        return [col_table[k] for k in sorted_keys]