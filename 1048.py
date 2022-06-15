# https://leetcode.com/problems/longest-string-chain/
from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
import math
import bisect
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple

def is_precursor(word1, word2):
    if len(word1) + 1 != len(word2):
        return False

    # Find the first instance when a character does not match
    non_match = None
    for i, (c1, c2) in enumerate(zip(list(word1), list(word2))):
        if c1 != c2:
            # Remove letter from word2
            word2 = word2[:i] + word2[i+1:]
            break
    else:
        word2 = word2[:-1]

    return word1 == word2

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Direct DP approach
        # At each word, determine the maximum subsequence ending at this position 
        
        # Sort words by length
        words.sort(key = len)

        # Create word to index mapping
        word_dict = {word: i for i, word in enumerate(words)}

        # Init list to 1's
        longest_chain = [1 for _ in range(len(words))]

        for n, word in enumerate(words):
            indices_of_valid_precursors = []
            for i in range(len(word)):
                precursor = word[:i] + word[i+1:]
                if precursor in word_dict:
                    indices_of_valid_precursors.append(word_dict[precursor])
            longest_chain[n] = max([longest_chain[i] for i in indices_of_valid_precursors], default=0) + 1

        return max(longest_chain)

class Solution:
    def longestStrChain(self, words):
        # Even simpler
        dp = {}
        for word in sorted(words, key=len):
            # Check every single possible precursor word with one letter removed
            dp[word] = max(dp.get(word[:i] + word[i + 1:], 0) + 1 for i in range(len(word)))
        return max(dp.values())