# https://leetcode.com/problems/range-sum-query-2d-immutable/
import numpy as np
import functools
class NumMatrix:
    # Solve using np and caching
    def __init__(self, matrix: List[List[int]]):
        self.matrix = np.array(matrix, dtype=int)

    @functools.cache
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return np.sum(self.matrix[row1:row2+1, col1:col2+1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)