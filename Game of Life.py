# my approach
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def countNeighbours(board,row,col,maxRow,maxCol):
            count = 0
            neighbours = [[row-1, col-1], [row-1, col], [row-1, col+1],[row, col-1],[row, col+1],[row+1, col-1], [row+1, col], [row+1, col+1]]
            
            for r,c in neighbours:
                if 0 <= r < maxRow and 0<= c < maxCol:
                    count += board[r][c]
            return count

        copyBoard = [row[:] for row in board]
        maxR, maxC = len(board),len(board[1])

        for i in range(maxR):
            for j in range(maxC):
                neighbours = countNeighbours(copyBoard,i,j,maxR,maxC)
                if board[i][j] == 1 and (neighbours < 2 or neighbours > 3):
                    board[i][j] = 0
                elif board[i][j] == 0 and neighbours == 3:
                    board[i][j] = 1
