# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                # print(f"{i=}")
                # print(f"{j=}")
                row.append(matrix[j][i])
            t.append(row)
            
        return t