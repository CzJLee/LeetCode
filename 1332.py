# https://leetcode.com/problems/remove-palindromic-subsequences/
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Solution is actually easier than expected, since there are only two possible characters 
        if s == s[::-1]:
            return 1
        else:
            return 2