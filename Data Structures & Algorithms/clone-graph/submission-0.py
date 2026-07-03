"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone_node = {} # original node to cloned node mapping

        def dfs(node):
            if node in clone_node:
                return clone_node[node]
            
            copy = Node(node.val)
            clone_node[node] = copy # map original node to cloned node
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        clone = dfs(node)

        print(clone_node)
        
        return clone

