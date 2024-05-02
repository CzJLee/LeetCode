"""
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
"""

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # https://leetcode.com/problems/number-of-wonderful-substrings/solutions/1299525/count-bitmasks-with-picture/?envType=daily-question&envId=2024-05-02
        # Create an array to hold the counts that each bit mask has been seen.
        # Since there are 10 letters (a-j), there are 2^10=1024 possible masks.
        mask_counts = [0] * 1024
        # The mask "0" should start at 1, to consider the empty string "" case.
        mask_counts[0] = 1
        # The total number of wonderful substrings.
        total = 0
        # Our working bitmask. This is a binary representation of each letter
        # indicating if the total count is even (0) or odd (1).
        mask = 0
        for char in word:
            # Iterate through each character in the word, updating it's bitmask
            # with each character.

            # If a character is encountered, update the bitmask.
            mask ^= 1 << (ord(char) - ord('a'))

            # We then count substrings for each time that we have encountered
            # this mask before.
            total += mask_counts[mask]

            # Then consider the cases where there is one odd count.
            # For each letter a-j
            for n in range(10):
                total += mask_counts[mask ^ 1 << n]

            # Update mask_counts for this current mask.
            mask_counts[mask] += 1

        return total