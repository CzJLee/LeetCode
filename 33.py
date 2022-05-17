# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        rotate_split = nums[0]
        
        # If we ever encounter a number < rotate_split in the array, we know that we are in the second half of the rotation
        
        # Do two steps, one to find split, then one normal binary search
        # This should be O(2 log n)
        
        # Find start of the rotation point
        if nums[-1] >= rotate_split:
            # No rotation occured
            sorted_nums = nums
            split_index = 0
        else:
            def find_split(nums, first, last):
                if nums[first] < rotate_split:
                    # Found it
                    return first
                
                index = (last + first) // 2
                if nums[index] >= rotate_split:
                    # Split is to the right
                    return find_split(nums, index+1, last)
                else:
                    # Split is to the left
                    return find_split(nums, first, index)

            split_index = find_split(nums, 0, len(nums) - 1)
            sorted_nums = nums[split_index:] + nums[:split_index]
            
        def binary_search(nums, target, first, last):
            if nums[first] == target:
                return first
            elif first >= last:
                return -1

            index = (last + first) // 2
            if nums[index] < target:
                # Split is to the right
                return binary_search(nums, target, index+1, last)
            else:
                # Split is to the left
                return binary_search(nums, target, first, index)
            split_index = find_split(nums, 0, len(nums) - 1)
            sorted_nums = nums[split_index:] + nums[:split_index]
            
        sorted_index = binary_search(sorted_nums, target, 0, len(nums) - 1)
        
        if sorted_index == -1:
            return -1
        else:
            return (sorted_index + split_index) % len(nums)
        
        