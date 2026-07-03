# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs the left then dsf the right at that node to calculate the distance from the deepest left leaf to the deepest right leaf
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # update diameter at this node
            diameter = max(diameter, left_depth + right_depth)

            # return the max depth of the tree rooted at this node
            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return diameter

