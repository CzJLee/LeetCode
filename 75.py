# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        front = 0
        back = len(nums) - 1
        
        pointer = 0
        
        while pointer <= back:
            if nums[pointer] == 0:
                nums[front], nums[pointer] = nums[pointer], nums[front]
                front += 1
                pointer += 1
            elif nums[pointer] == 2:
                nums[back], nums[pointer] = nums[pointer], nums[back]
                back -= 1
            else:
                pointer += 1
        