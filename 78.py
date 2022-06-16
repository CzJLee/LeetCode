# https://leetcode.com/problems/subsets/
from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import math
import bisect
import sys

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Using python methods
        subsets = []
        for i in range(len(nums) + 1):
            subsets.extend(list(combinations(nums, i)))
        return subsets