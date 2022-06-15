# https://leetcode.com/problems/jump-game/
from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import math
import bisect
import sys

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP Tabular solution
        dp = [False for _ in nums]
        dp[0] = True
        
        for i in range(1, len(nums)):
            for j in reversed(range(0, i)):
                jump_target = i - j
                if dp[j] and nums[j] >= jump_target:
                    dp[i] = True
                    break
        return dp[-1]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # If nums does not contain zero, then it is always true
        if 0 not in nums:
            return True

        # Greedy solution
        steps_remaining = 0

        for n in nums:
            # Base case
            if steps_remaining < 0:
                return False
            # Greedy: if larger step is avl, land here and take it
            steps_remaining = max(n, steps_remaining)
            # Take step to next spot
            steps_remaining -= 1
        # Reached the end
        return True