"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.


Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1

        def is_binary_search_helpful(nums, start, element):
            """Return true if we can continue binary search"""
            return nums[start] != element

        def element_in_first(nums, start, element):
            """True if element in first array, False if in second."""
            return nums[start] <= element

        while start <= end:
            mid = start + (end - start) // 2
            print(start, mid, end)

            if nums[mid] == target:
                return True

            if not is_binary_search_helpful(nums, start, nums[mid]):
                # Bump by one and continue search.
                start += 1
                continue

            # Determine where the pivot is and where the target is.
            pivot_in_first = element_in_first(nums, start, nums[mid])
            target_in_first = element_in_first(nums, start, target)

            if pivot_in_first ^ target_in_first:
                # If pivot and target are not in same segment.
                if pivot_in_first:
                    # Pivot is in first, target is in second.
                    start = mid + 1
                else:
                    # Pivot is in second, target is in first.
                    end = mid - 1
            else:
                # If pivot and target are in same segment.
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

        return False
