"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row_count = 0
        for row in grid:
            current = 0
            for cell in row:
                if cell != current:
                    current = cell
                    row_count += 1
            if current == 1:
                row_count += 1
        
        col_count = 0
        for col in range(len(grid[0])):
            current = 0
            for row in range(len(grid)):
                if grid[row][col] != current:
                    current = grid[row][col]
                    col_count += 1
            if current == 1:
                row_count += 1

        return row_count + col_count