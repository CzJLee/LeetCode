"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))

        longest_sequence_length = 1

        prev = sorted_nums.pop(0)

        current_sequence_length = 1
        for n in sorted_nums:
            print(n)
            if n == prev + 1:
                current_sequence_length += 1
                longest_sequence_length = max(longest_sequence_length, current_sequence_length)
            else:
                current_sequence_length = 1
            
            prev = n

        return longest_sequence_length