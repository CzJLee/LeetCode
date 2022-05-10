# https://leetcode.com/problems/combination-sum-iii/

import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # The most number of checks we will have to do is 9 choose 5. 
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        combinations = itertools.combinations(nums, k)
        
        valid_sums = []
        
        for combo in combinations:
            if sum(combo) == n:
                valid_sums.append(combo)
                
        return valid_sums
        