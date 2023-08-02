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
        end = len(t)

        t_counts = collections.Counter(t)
        window_counts = collections.Counter(s[start:end])

        shortest_substring = s

        while end < len(s) + 1:
            if t_counts <= window_counts:
                # Is substring.
                # print(f"Is a substring {s[start:end]}")
                if len(s[start:end]) < len(shortest_substring):
                    shortest_substring = s[start:end]
                # Contract start.
                start += 1
                window_counts[s[start - 1]] -= 1
            else:
                # Not substring.
                # Expand end.
                # print(f"Not a substring {s[start:end]}")
                end += 1
                if end > len(s):
                    break
                window_counts[s[end - 1]] += 1


        return shortest_substring
