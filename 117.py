# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Simple modification of 116
        # BFS
        # Encounter each layer in a row, shift node
        
        # Start by adding root, then None
        # Then BFS
        # When None is encountered, make it the right node, then add it back to the queue 
        
        if root is None:
            return root
        
        queue = [root, None]
        
        node = queue.pop(0)
        
        while queue:
            print(node)
            if node is None:
                if len(queue) > 0:
                    queue.append(None)
                    node = queue.pop(0)
                continue
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
            next_node = queue.pop(0)
            node.next = next_node
            node = next_node
        
        return root
                