from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = set(),set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        for row in r:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        
        for col in c:
            for i in range(len(matrix)):
                matrix[i][col] = 0