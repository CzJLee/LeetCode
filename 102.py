# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS.
        if root is None:
            return []

        level_order = []

        queue = [root, None]

        node = queue.pop(0)
        current_level = []
        while queue:
            if node:
                print(node.val)
                current_level.append(node.val)

            if node is None:
                current_level = []
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
            if node is None:
                level_order.append(current_level)

        return level_order
