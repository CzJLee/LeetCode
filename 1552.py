"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length
"""


class Solution:
    def check(self, position: list[int], m: int, ans: int) -> bool:
        # Assume position is sorted
        range = position[-1] - position[0]

        last_checkpoint = position[0]
        desired = last_checkpoint + ans
        m -= 1

        for x in position:
            if x >= desired:
                # Place a ball
                m -= 1
                last_checkpoint = x
                desired = last_checkpoint + ans
                if m == 0:
                    # We have placed all balls
                    return True
        
        # We have exhausted all bins and can't create ans.
        return False

    def maxDistance(self, position: list[int], m: int) -> int:
        # Use binary search on answer.

        # Sort position to allow for easy checking
        position.sort()

        max_range = position[-1] - position[0]

        if m == 2:
            # If only two balls, then use two bookends.
            return max_range
        
        # Create binary search range.
        # Minimum possible is minimum separation distance.
        low = 1
        high = max_range
        estimate = (low + high) // 2

        while low < estimate:
            # print(f"Checking {estimate=}, {low=}, {high=}")
            is_possible = self.check(position, m, estimate)
            # print(f"Is possible: {is_possible=}")
            if is_possible:
                # If it is possible to do it with estimate, then it may also be possible to do it with a higher estimate.
                low = estimate
            else:
                # If not possible, then our estimate is too high. 
                high = estimate
            estimate = (low + high) // 2
        
        return estimate