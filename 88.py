# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        
        t = m + n - 1
        
        while t >= 0:
            if p2 < 0:
                nums1[t] = nums1[p1]
                t -= 1
                p1 -= 1
            elif p1 < 0:
                nums1[t] = nums2[p2]
                t -= 1
                p2 -= 1
            elif nums1[p1] >= nums2[p2]:
                nums1[t] = nums1[p1]
                t -= 1
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[t] = nums2[p2]
                t -= 1
                p2 -= 1
            else:
                print("edge case")
        
        