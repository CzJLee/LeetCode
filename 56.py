# https://leetcode.com/problems/merge-intervals/
from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import math
import bisect
import sys

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        slots = []
        for i, (start, end) in enumerate(intervals):
            slots.append((start, 0, i))
            slots.append((end, 1, i))
            
        slots.sort()

        active = set()
        merged_intervals = []

        # print(slots)

        # Iterate through slots
        start = 0
        end = 0
        for slot, toggle, idx in slots:
            if toggle == 0:
                # If starting
                if len(active) == 0:
                    # If no active, create a new start
                    start = slot
                # Add the index
                active.add(idx)
            else:
                # If ending
                # Remove index
                active.remove(idx)
                if len(active) == 0:
                    # If no more slots active
                    end = slot
                    interval = [start, end]
                    merged_intervals.append(interval)

        # print(merged_intervals)
        return merged_intervals


if __name__ == "__main__" and sys.platform == "darwin":
    sol = Solution()
    sol.merge([[1,3],[2,6],[8,10],[15,18]])