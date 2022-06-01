# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Algorithm

        Initialize an array sub which contains the first element of nums.

        Iterate through the input, starting from the second element. For each element num:

        If num is greater than any element in sub, then add num to sub.
        Otherwise, perform a binary search in sub to find the smallest element that is greater than or equal to num. Replace that element with num.
        Return the length of sub.
        """
        # Optimal Longest Increasing Subsequence 
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)