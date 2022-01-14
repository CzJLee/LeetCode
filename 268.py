# https://leetcode.com/problems/missing-number/submissions/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        all_n = set(range(n + 1))
        missing = all_n - nums
        return missing.pop()