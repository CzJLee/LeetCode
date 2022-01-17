# https://leetcode.com/problems/word-pattern/submissions/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split(" ")
        a_split = [char for char in pattern]
        
        if len(s_split) != len(a_split):
            return False
        
        s_hash = {}
        a_hash = {}
        
        a_val = 0
        s_val = 0
        for a, s in zip(a_split, s_split):
            if a in a_hash:
                a_val = a_hash[a]
            else:
                a_val += 1
                a_hash[a] = a_val
            if s in s_hash:
                s_val = s_hash[s]
            else:
                s_val += 1
                s_hash[s] = s_val
            if a_val != s_val:
                return False
        return True

        