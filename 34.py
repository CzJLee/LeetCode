# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Double binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_first(nums, target, first, last):
            # Return first index
            if first > last:
                return -1
            if nums[first] == target:
                return first
            
            index = (first + last) // 2
            
            if nums[index] == target:
                return binary_search_first(nums, target, first, index)
            elif nums[index] > target:
                # Search left half
                return binary_search_first(nums, target, first, index-1)
            else:
                # Search right half
                return binary_search_first(nums, target, index + 1, last)
            
        def binary_search_last(nums, target, first, last):
            # Return last index
            if first > last:
                return -1
            if nums[last] == target:
                return last
            
            index = (first + last + 1) // 2
            
            if nums[index] == target:
                return binary_search_last(nums, target, index, last)
            elif nums[index] > target:
                # Search left half
                return binary_search_last(nums, target, first, index-1)
            else:
                # Search right half
                return binary_search_last(nums, target, index + 1, last)
            
        first = binary_search_first(nums, target, 0, len(nums) - 1)
        last = binary_search_last(nums, target, 0, len(nums) - 1)
        
        if first == -1:
            return [-1, -1]
        else:
            return [first, last]