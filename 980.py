# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # iterate through the grid to get relevant info
        start = None  # to store starting point
        count = 0  # to count number of squares to walk over
        for i in range(m):
            for j in range(n):
                count += grid[i][j] == 0
                if not start and grid[i][j] == 1:
                    start = (i, j)
        
        def backtrack(i: int, j: int) -> int:
            """
            Backtracking algo to find all valid paths from (i, j).
            :param i: Index of row (where top = 0) of coordinate.
            :param j: Index of column (where left = 0) of coordinate.
            :returns: Total number of valid paths from (i, j).
            """
            nonlocal count
            result = 0
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                # border check
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0:
                        # traverse down this path
                        grid[x][y] = -1
                        count -= 1
                        result += backtrack(x, y)
                        # backtrack and reset
                        grid[x][y] = 0
                        count += 1
                    elif grid[x][y] == 2:
                        # check if all squares have been walked over
                        result += count == 0
            return result
        
        # perform DFS + backtracking to find valid paths
        return backtrack(start[0], start[1])