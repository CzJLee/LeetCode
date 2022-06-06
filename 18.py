# https://leetcode.com/problems/4sum/
import collections
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(nums)
        num_set = set(nums)

        ans_set = set()
        
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    t = target - nums[i] - nums[j] - nums[k]
                    if t in num_set and collections.Counter([nums[i], nums[j], nums[k]])[t] < counter[t]:
                        ans_set.add(tuple(sorted([nums[i], nums[j], nums[k], t])))
                            
        ans_list = []
        for a in ans_set:
            ans_list.append(list(a))
            
        return ans_list