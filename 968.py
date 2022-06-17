# https://leetcode.com/problems/binary-tree-cameras/
from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import math
import bisect
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # Combine Dynamic programming with BFS traversal 

        # Rules:
        # Use BFS to start from the children and work your way up
        # If a node has no descendants, give it's parent a camera
        # If a node has children, and no children have cameras, give the node a camera

        # Use Recursion
        # Base Case: A node has no children -> Tell its parent to use a camera 
        # At each step, check if node has children. 
            # If not, then tell its parents to use a camera
            # Else, add a camera to the node if none of the children have cameras 
        # All node values are initiated to 0. Use node.val = 1 to mark it as a camera 

        # BFS Queue to step through the tree
        queue = deque()
        queue.append(root)

        # Counter to keep track of number of cameras added
        num_cameras = 0

        # node = root

        # if node.left is None and node.right is None:
        #     # Node has no children 
        #     # Use -1 to mark a node with no children 
        #     node.val = -1
        #     return

        # left, right = get_child_values(node)
        # if left is None and right is None:
        #     # Node has no children 
        #     # Use -1 to mark a node with no children 
        #     node.val = -1
        #     return
        # elif left == -1 or right == -1:
        #     # It is the parent of a node with no children
        #     # Following the rule, give this a camera
        #     node.val = 1
        #     num_cameras += 1
        #     return
        # elif not left and not right:
        #     # Both left and right are either 0 or None
        #     # Following the rule, give this a camera
        #     node.val = 1
        #     num_cameras += 1
        #     return

        # if left is None and right is None:
        #     # Node has no children 
        #     # Use -1 to mark a node with no children 
        #     return -1
        # if left + right <= 0:
        #     # Add a camera
        #     return 1
        # elif left == -1 or right == -1:
        #     # It is the parent of a node with no children
        #     # Following the rule, give this a camera
        #     node.val = 1
        #     num_cameras += 1
        #     return

        
        # def get_child_values(node):
        #     left_value = node.left.val if node.left else None
        #     right_value = node.right.val if node.right else None
        #     return (left_value, right_value)

        def mark_node(node):
            if node is None:
                # Base case
                return None, 0

            left_mark, left_cameras = mark_node(node.left)
            right_mark, right_cameras = mark_node(node.right)
            if left_mark is None and right_mark is None:
                # Base case
                # node.val = -1
                return -1, 0
            if left_mark == -1 or right_mark == -1:
                # It is the parent of a node with no children
                # Following the rule, give this a camera
                # node.val = 1
                # num_cameras += 1
                return 1, 1 + left_cameras + right_cameras
            if not left_mark and not right_mark:
                # Both left and right are either 0 or None
                # Following the rule, give this a camera
                # node.val = 1
                # num_cameras += 1
                return 1, 1 + left_cameras + right_cameras
            else:
                # At least one child has a camera, do not give this node a camera
                return 0, left_cameras + right_cameras

        if root.left is None and root.right is None:
            return 1

        mark, num_cameras = mark_node(root)

        return num_cameras

            
            # # Add a camera to the node if none of its children have cameras 
            # if mark_node(node.left) == -1 or mark_node(node.right) == -1:
            #     # It is the parent of a node with no children
            #     # Following the rule, give this a camera
            #     node.val = 1
            #     num_cameras += 1
            #     return 1
            
            # elif not mark_node(node.left) and not mark_node(node.right):
            #     # Both left and right are either 0 or None
            #     # Following the rule, give this a camera
            #     node.val = 1
            #     num_cameras += 1
            #     return


