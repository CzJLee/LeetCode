"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
"""

import collections

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # Store a hash of mod -> index to find sub-arrays

        hash_table = collections.defaultdict(list)
        current_sum = 0

        count = 0

        for i, n in enumerate(nums):
            current_sum = (current_sum + n) % k
            if current_sum == 0:
                count += 1
            if current_sum in hash_table:
                # Count all sub arrays
                count += len(hash_table[current_sum])
            hash_table[current_sum].append(i)

        return count

