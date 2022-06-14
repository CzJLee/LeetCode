class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force (Time exceeded)
        max_sum = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                max_sum = max(sum(nums[i:j]), max_sum)
                
        return max_sum

from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP approach
        # Calculate the max sub array of sublist length i
        # When you add a new element, find the max of all elements, or the new element combined with the sum of the previous 
        # Max sum at i represents the max sum ending with i'th element
        max_sum = list(nums)

        for n in range(1, len(nums)):
            max_sum[n] = max(max_sum[n], max_sum[n-1] + max_sum[n])

        return max(max_sum)

