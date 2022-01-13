# https://leetcode.com/problems/deepest-leaves-sum/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        level_sum = {}
        def sum_level(root, level):
            if level in level_sum:
                level_sum[level] += root.val
            else:
                level_sum[level] = root.val
            
            if root.left:
                sum_level(root.left, level + 1)
            if root.right:
                sum_level(root.right, level + 1)
        
        sum_level(root, 0)
        
        sorted(list(level_sum.keys()))
        return level_sum[sorted(list(level_sum.keys()))[-1]]
        
                