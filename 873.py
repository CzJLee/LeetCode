# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
import itertools
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        
        max_length = 0
        
        # Test ever 2 number pair
        # O(N^2)
        # print(list(itertools.combinations(arr, 2)))
        
        for a, b in itertools.combinations(arr, 2):
            sequence_length = 2
            c = a + b
            while c in nums:
                a, b = b, c
                c = a + b
                sequence_length += 1
            
            max_length = max(max_length, sequence_length)
        
        if max_length == 2:
            return 0
        else:
            return max_length
            