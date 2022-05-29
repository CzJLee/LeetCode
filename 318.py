# https://leetcode.com/problems/maximum-product-of-word-lengths/
import itertools
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # O(N^2) Time
        words.sort(key = lambda x: len(x), reverse = True)
        pairs = list(itertools.combinations(range(len(words)), 2))
        pairs.sort(key = lambda x: len(words[x[0]]) * len(words[x[1]]), reverse = True)
        # print(words)
        # print(pairs)
        # max_val = 0
        for i, j in pairs:
            letters = set(words[i])
            if all([char not in letters for char in words[j]]):
                print(words[i], words[j])
                return len(words[i]) * len(words[j])
        return 0
        # for i in range(len(words)):
        #     letters = set(words[i])
        #     for j in range(i, len(words)):
        #         if all([char not in letters for char in words[j]]):
        #             max_val = max(max_val, len(words[i]) * len(words[j]))
        # return max_val

