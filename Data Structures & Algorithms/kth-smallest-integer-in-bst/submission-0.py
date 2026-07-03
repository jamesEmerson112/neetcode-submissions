# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 0
        self.result = None

        def traverse(node):
            if not node or self.result is not None:
                return 

            traverse(node.left)
            
            self.index += 1
            if k == self.index:
                self.result = node.val
                return

            traverse(node.right)

        traverse(root)
        return self.result