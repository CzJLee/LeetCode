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

node_info = namedtuple("Node", ["has_camera", "covered", "num_cameras"])

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def mark_node(node) -> node_info:
            """
            Recursive function to keep track of which nodes have a camera, and which are covered. 
            """
            # Rule 1: If a node has no descendants, give its parent a camera
            # Rule 2: Only give a node a camera if one of its children are uncovered

            # Base case
            if node is None:
                # Return covered = True, so that any leaf node (with no children) will default to no camera and no coverage, forcing the parent to have a camera. This follows rule 1. 
                return node_info(has_camera=False, covered=True, num_cameras=0)

            # Recursive calls, update left and right, and get values
            left_has_camera, left_covered, left_num_cameras = mark_node(node.left)
            right_has_camera, right_covered, right_num_cameras = mark_node(node.right)

            # Keep track of total number of cameras added so far
            total_num_cameras = left_num_cameras + right_num_cameras

            # Rule 2: Only give a node a camera if at least one of its children are uncovered
            if left_covered and right_covered:
                # If all children are covered, we do not need to have a camera
                has_camera = False
                if left_has_camera or right_has_camera:
                    # If any children has a camera, the parent is covered
                    covered = True
                else:
                    covered = False
            else:
                # At least one child is uncovered, we need to have a camera
                has_camera = True
                covered = True
                # Increase camera count
                total_num_cameras += 1
            
            return node_info(has_camera, covered, total_num_cameras)

        root_has_camera, root_covered, total_num_cameras = mark_node(root)
        if not root_covered:
            total_num_cameras += 1

        return total_num_cameras