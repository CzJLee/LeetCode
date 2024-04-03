"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

import itertools


class Solution:
    def get_neighbors(self, coordinate: tuple[int, int], board: list[list[str]]):
        max_y = len(board)
        max_x = len(board[0])
        x, y = coordinate
        coordinates = []
        if x > 0:
            coordinates.append((x - 1, y))
        if x < max_x - 1:
            coordinates.append((x + 1, y))
        if y > 0:
            coordinates.append((x, y - 1))
        if y < max_y - 1:
            coordinates.append((x, y + 1))
        return set(coordinates)

    def exist(self, board: list[list[str]], word: str) -> bool:
        letters_in_board = set(itertools.chain.from_iterable(board))
        letters_in_word = set(word)
        # If one of the letters is missing, then the word can't exist.
        if not letters_in_word.issubset(letters_in_board):
            return False

        stack = []
        for y, row in enumerate(board):
            for x, letter in enumerate(row):
                if letter == word[0]:
                    stack.append((x, y, word[1:], set([(x, y)])))

        while stack:
            x, y, word, visited = stack.pop()
            # print((x, y, word, visited))
            if not word:
                return True
            # print(f"Checking coordinate ({x}, {y}) : {board[y][x]} for letter {word[0]}.")

            neighbors = self.get_neighbors((x, y), board)
            unvisited_neighbors = neighbors - visited
            for neighbor in unvisited_neighbors:
                x, y = neighbor
                if board[y][x] == word[0]:
                    stack.append((x, y, word[1:], visited.union([(x, y)])))

        return False
