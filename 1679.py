# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt, ans = Counter(n for n in nums if n < k), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans//2