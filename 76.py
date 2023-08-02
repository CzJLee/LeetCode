"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
import collections


class Solution:
    def is_substring(self, window: str, t: str) -> bool:
        return collections.Counter(t) <= collections.Counter(window)

    def minWindow(self, s: str, t: str) -> str:
        if not self.is_substring(s, t):
            return ""

        # Find substring candidates by starting a sliding window from the beginning of the string.
        # Increase the window until a substring is found.
        # Start a reverse window starting from the other end until a shortest is found. 
        # This is the smallest substring for that section.
        # Save that part of the string.
        # Continue.
        start = 0
        end = 0

        shortest_substring = s

        while end < len(s):
            end += 1
            if self.is_substring(s[start:end], t):
                new_start = end - len(t)
                while new_start >= start:
                    if self.is_substring(s[new_start:end], t):
                        window = s[new_start : end]
                        if len(window) < len(shortest_substring):
                            shortest_substring = window
                        break
                    new_start -= 1
                start = new_start

        return shortest_substring
