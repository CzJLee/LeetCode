# https://leetcode.com/problems/delete-operation-for-two-strings/
# Modified edit distance problem

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # BFS
        # Goal: When strings match
        # At each step: remove a character 
        
        # queue = deque()
        # seen = set()
        
        char_in_word1 = set(word1)
        char_in_word2 = set(word2)
        
        reduced_word1 = [char for char in word1 if char in char_in_word2]
        reduced_word2 = [char for char in word2 if char in char_in_word1]
        reduced_word1 = "".join(reduced_word1)
        reduced_word2 = "".join(reduced_word2)
        
        steps = (len(word1) - len(reduced_word1)) + (len(word2) - len(reduced_word2))
    
#         print(reduced_word1)
#         print(reduced_word2)
#         print(steps)
        
        @cache
        def minDistance(word1, word2):
            """Naive recursive solution"""
            if not word1 and not word2:
                return 0
            if not word1:
                return len(word2)
            if not word2:
                return len(word1)
            if word1[0] == word2[0]:
                return minDistance(word1[1:], word2[1:])
            delete1 = 1 + minDistance(word1[1:], word2)
            delete2 = 1 + minDistance(word1, word2[1:])
            return min(delete1, delete2)
    
        return minDistance(reduced_word1, reduced_word2) + steps

