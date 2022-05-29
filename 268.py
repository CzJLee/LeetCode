# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(N) space, O(N) Time
        n = len(nums)
        nums = set(nums)
        all_n = set(range(n + 1))
        missing = all_n - nums
        return missing.pop()

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(1) Space, O(N Log N) Time
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(1) Space
        # O(3N) Time
        max_n = len(nums) + 1
        zero_seen = False
        for i, n in enumerate(nums):
            if n == 0:
                zero_seen = True
                break
        if zero_seen is False:
            return 0
        
        nums.append(0)
        for i, n in enumerate(nums):
            nums[n % max_n] += max_n
        for i, n in enumerate(nums):
            if n < max_n:
                return i

class Solution:
    def missingNumber(self, nums):
        """
        Approach #3 Bit Manipulation [Accepted]
        Intuition
        We can harness the fact that XOR is its own inverse to find the missing element in linear time.

        Algorithm
        Because we know that nums contains n numbers and that it is missing exactly one number on the range [0..n-1], we know that n definitely replaces the missing number in nums. Therefore, if we initialize an integer to n and XOR it with every index and value, we will be left with the missing number. 
        """
        # XOR Bit manipulation

        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class Solution:
    def missingNumber(self, nums):
        # Using math trick adding sequence of numbers 1 through N
        # Gauss' Formula
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

class Solution:
    def missingNumber(self, nums):
        # Alternative Gauss' Formula
        result = 0
        for i in range(len(nums)):
            result += ((i + 1) - nums[i])
        return result