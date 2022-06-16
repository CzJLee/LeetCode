# https://leetcode.com/problems/climbing-stairs/
from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import math
import bisect
import sys

phi = (1 + math.sqrt(5)) / 2
sqrt_5 = math.sqrt(5)
def fib(n):
    return int((phi ** n - (-1 / phi) ** n) / sqrt_5)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Math
        return fib(n+1)

class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        if n == 1:
            return 1
        steps = [0 for _ in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n-1]

x = [fib(i) for i in range(47)]
print(x)