# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        
        print(sorted_nums)
        
        sub_first = None
        sub_last = None
        
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                sub_first = i
                break
                
        for i in reversed(list(range(len(nums)))):
            if sorted_nums[i] != nums[i]:
                sub_last = i
                break
        
        print(f"{sub_first=}")
        print(f"{sub_last=}")
        if sub_first is None or sub_last is None:
            return 0
        else:
            return sub_last-sub_first+1
            
        