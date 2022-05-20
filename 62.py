# https://leetcode.com/problems/unique-paths/

import functools

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use Dynamic Programming (simplified from 63)
        # The number of ways to reach (h, w) is equal to the number of ways to get to it's two prior tiles
        height = m
        width = n
        
        @functools.cache
        def visit(h, w):
            if h < 0 or w < 0:
                return 0
            elif h == 0 and w == 0:
                return 1
            return visit(h, w-1) + visit(h-1, w)
        
        return visit(height-1, width-1)