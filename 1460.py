# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Fast answer using length of number of substring permutations 
        if len(s) < k:
            return False
        
        substrings = set()
        for i in range(len(s) - k + 1):
            substrings.add(s[i:i+k])
            
        k10 = 2**k - 1
    
        if len(substrings) < 2 ** k:
            return False
        return True