"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
"""
import functools


class Solution:

    @functools.cache
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if len(s1) == 0 and len(s2) == 0:
            return 0
        elif len(s1) == 0:
            return ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:])
        elif len(s2) == 0:
            return ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2)
        elif s1[0] == s2[0]:
            return self.minimumDeleteSum(s1[1:], s2[1:])
        else:
            return min(ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2),
                       ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:]))
