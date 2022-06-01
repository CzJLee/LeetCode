import itertools
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Using built in itertools
        return list(itertools.accumulate(nums))