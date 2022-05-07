# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # BFS
        if root is None:
            return root
        
        levels = []
        
        queue = [root]
        
        while queue:
            layer = queue
            queue = []
            nodes = []
            for node in layer:
                queue.extend(node.children)
                nodes.append(node.val)
            levels.append(nodes)
            
        return levels
            