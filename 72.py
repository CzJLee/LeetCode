# https://leetcode.com/problems/edit-distance/
# Probably Accurate, but too slow
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Use BFS -> Backtrack
        # At every letter in word1, either insert, delete, replace, or pass if valid
        # End when you reach the end of word1
        
        # Find minimum path
        
        sol_lengths = []
        
        def bfs(word, target, p1, p2, ops):
            # print(word, target)
            if word == target:
                sol_lengths.append(ops)
                return
            if p2 >= len(target):
                # Reached end of target
                # Word should contain target in first half
                extra_length = len(word) - len(target)
                bfs(word[:len(target)], target, p1, p2, ops + extra_length)
                return
            if p1 >= len(word):
                # Word is smaller, insert char
                bfs(word + target[p2], target, p1 + 1, p2 + 1, ops + 1)
                return
            # Check for pass
            if word[p1] == target[p2]:
                bfs(word, target, p1 + 1, p2 + 1, ops)
                return
            
            # Insert
            letter = target[p2]
            bfs(word[:p1] + letter + word[p1:], target, p1 + 1, p2 + 1, ops + 1)
            
            # Delete
            bfs(word[:p1] + word[p1 + 1:], target, p1, p2, ops + 1)
            
            # Replace
            letter = target[p2]
            bfs(word[:p1] + letter + word[p1 + 1:], target, p1 + 1, p2 + 1, ops + 1)
            
        bfs(word1, word2, 0, 0, 0)
        
        # print(sol_lengths)
        # print(min(sol_lengths))
        return min(sol_lengths)