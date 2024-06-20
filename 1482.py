"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
 

Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n
"""

class Solution:
    def count_boquets(self, bloomDay: list[int], k: int, day: int):
        """Count the number of boquets possible on this day."""
        bloom_on_day = [max(0, x-day) for x in bloomDay]
        count = 0
        collected = 0
        for x in bloom_on_day:
            if x == 0:
                collected += 1
                if collected == k:
                    count += 1
                    collected = 0
            else:
                collected = 0
        return count

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            # Impossible, not enough flowers
            return -1
        elif m * k == len(bloomDay):
            # Exactly all flowers needed. Need to wait for longest flower.
            return max(bloomDay)
        
        # Binary search across number of days.

        left = 0
        right = max(bloomDay)

        midpoint = (right + left) // 2

        while left < midpoint:
            print(f"{left=}, {right=}, {midpoint=}")
            count = self.count_boquets(bloomDay, k, day=midpoint)
            print(count)
            if count >= m:
                right = midpoint
            else:
                left = midpoint
            midpoint = (right + left) // 2

        return midpoint + 1