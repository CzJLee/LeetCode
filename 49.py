# https://leetcode.com/problems/group-anagrams/
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group by letter sort
        anagram_set = collections.defaultdict(list)
        
        for word in strs:
            anagram_set[tuple(sorted(word))].append(word)
            
        anagram_groups = []
        for group in anagram_set.values():
            anagram_groups.append(group)
        
        return anagram_groups