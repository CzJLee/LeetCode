# https://leetcode.com/problems/combination-sum/

# Fix up backtracking solution using solution as a guide. 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # Use backtracking
        
        # Try an element until it either equals the target or you exceed
        # If sum is valid, add it to list
        # Else move on to next try
        
        results = []
        
        values = []
        
        def backtrack(values, candidates):
            if sum(values) == target:
                results.append(values.copy())
            elif sum(values) > target:
                return
            
            for i, x in enumerate(candidates):
                values.append(x)
                # print(values)
                backtrack(values, candidates[i:])
                values.pop()
        
        backtrack(values, candidates)
        
        return results
                    