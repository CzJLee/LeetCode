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
        dp = [False for _ in nums]
        dp[0] = True
        
        for i in range(1, len(nums)):
            for j in reversed(range(0, i)):
                jump_target = i - j
                if dp[j] and nums[j] >= jump_target:
                    dp[i] = True
                    break
        return dp[-1]