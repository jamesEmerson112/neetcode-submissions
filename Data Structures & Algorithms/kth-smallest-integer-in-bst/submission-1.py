# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # k = 1                     => smallest value
        # k = number of tree nodes  => largest value
        # an array that auto sort
        # an array where parent is i, left node is (2i-1)
        # right node is (2i + 1)?

        visited_node = []

        def inorder_traverse(node):
            global visisted_node
            if not node:
                return
            
            inorder_traverse(node.left)
            visited_node.append(node.val)
            inorder_traverse(node.right)

        inorder_traverse(root)

        return visited_node[k-1]