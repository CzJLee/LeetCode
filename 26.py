# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        pointer = 1
        while pointer < len(nums):
            if nums[pointer] == prev:
                nums.pop(pointer)
            else:
                prev = nums[pointer]
                pointer += 1
                
        
        return len(nums)