from typing import Any, Optional, Tuple, Union, Iterable, Mapping, Counter, Dict, List, Set
from functools import cache
from itertools import product, permutations, combinations, combinations_with_replacement
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import math
import bisect
import sys

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        results = []

        for i in range(len(searchWord)):
            # Remove all words that are shorter than the length we need
            products = [word for word in products if len(word) > i]
            char = searchWord[i]
            start = 0
            end = len(products)
            for j, word in enumerate(products):
                if word[i] == char:
                    start = j
                    break
            for j, word in enumerate(products[start:]):
                # Offset
                j += start
                if word[i] != char:
                    end = j
                    break
            products = products[start:end]
            results.append(products[:3])

        return results

