# https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nset = set(range(1, len(nums)+2))
        
        for n in nums: 
            nset.discard(n)
        
        return min(nset)