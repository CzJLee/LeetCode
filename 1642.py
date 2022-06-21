from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import heapq
import math
import bisect
import sys

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Solve by tracking whenever you increase in elevation
        # Use a heap
        gains = []

        for i, h in enumerate(heights[:-1]):
            height_diff = heights[i+1] - h
            if height_diff <= 0:
                # If next building is equal or lower
                continue
            
            # Push ladders onto the heap
            # Once heap is full, push the next, and pull the min
            # Remove min from the bricks
            # Return when bricks reaches zero 

            if len(gains) < ladders:
                # Fill the heap up to ladders
                heapq.heappush(gains, height_diff)
            else:
                min_gains = heapq.heappushpop(gains, height_diff)
                bricks -= min_gains
                if bricks < 0:
                    return i

        return len(heights) - 1