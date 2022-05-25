# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        root = x
        while root*root > x:
            root /= 2
        root = int(root)
        while root*root <= x:
            root += 1
        return int(root - 1)