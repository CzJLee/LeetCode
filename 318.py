# https://leetcode.com/problems/maximum-product-of-word-lengths/
import itertools
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # O(N^2) Time
        words.sort(key = lambda x: len(x), reverse = True)
        pairs = list(itertools.combinations(range(len(words)), 2)).sort(key = lambda x: x[0] * x[1], reverse=True)
        print(list(pairs))
        max_val = 0
        for i in range(len(words)):
            letters = set(words[i])
            for j in range(i, len(words)):
                if all([char not in letters for char in words[j]]):
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return max_val

