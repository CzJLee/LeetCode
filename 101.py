# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False

            return (
                left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        return is_mirror(root.left, root.right)
