"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""

import collections

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """Do something similar to two sum."""

        total_boats = 0
        counts = collections.Counter(people)

        weights = sorted(counts.keys(), reverse=True)

        for weight in weights:
            if counts[weight] <= 0:
                # No more people of this weight left
                continue
            
            # Find a pair
            if weight == limit:
                # No possible match, just give each their own boat.
                total_boats += counts[weight]
                counts[weight] = 0
            else:
                # Weight is under the limit, try to find someone to match with.
                while counts[weight] > 0:
                    desired_weight = limit - weight
                    while desired_weight > 0:
                        if counts[desired_weight] > 0 and desired_weight != weight:
                            num_boats_needed = min(counts[weight], counts[desired_weight])
                            total_boats += num_boats_needed
                            counts[weight] -= num_boats_needed
                            counts[desired_weight] -= num_boats_needed
                            break
                        elif counts[desired_weight] > 1 and desired_weight == weight:
                            num_boats_needed = counts[weight] // 2
                            total_boats += num_boats_needed
                            counts[weight] -= num_boats_needed * 2
                            break
                        else:
                            desired_weight -= 1
                    else:
                        # No pair can be found, just give these people their own boat.
                        total_boats += counts[weight]
                        counts[weight] = 0

        return total_boats