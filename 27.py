# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer_start = 0
        pointer_end = len(nums) - 1

        while pointer_start <= pointer_end:
            if nums[pointer_start] == val:
                # Swap
                nums[pointer_start], nums[pointer_end] = nums[pointer_end], nums[pointer_start]
                pointer_end -= 1
            else:
                pointer_start += 1
        
        return pointer_start