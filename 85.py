    """
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)  # Include an extra element for easier calculation
        max_area = 0
        
        for row in matrix:
            for i in range(cols):
                # Construct a heights array, which can be thought of as the
                # histogram of heights for the current row.
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate max area using histogram method
            stack = []
            for i in range(len(heights)):
                # We are iterating over row index. 
                # If there are elements in the stack, then we are forming some rectangle.
                # Then compare the height of the current bar with the high of the bar located at index i.
                # The heights of the bar at the top of the stack is the left most bar in the histogram to consider.
                while stack and heights[i] < heights[stack[-1]]:
                    # Since the current bar is smaller than the bar at the top of the stack, all future rectangles will be limited by this height. Remove the current bar from the top of the stack. This will be the height of the previous rectangle before this iteration i. 
                    h = heights[stack.pop()]
                    # If the stack is empty, thn all bars that came before this one were greater in value and previously got popped. So the width of the rectangle is i. If the stack is not empty, then the width of the rectangle is i - stack[-1] - 1. The stack[-1] represents the index value of the left most bar of the histogram, which can be used to calculate the width of the rectangle.
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area               