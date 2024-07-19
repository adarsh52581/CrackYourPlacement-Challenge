from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        maxR, maxCol = len(board),len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row<0 or row>=maxR or col<0 or col>=maxCol or board[row][col] != word[index]:
                return False

            temp = board[row][col]
            board[row][col] = 'V'

            found = (dfs(row+1,col,index+1) or dfs(row-1,col,index+1) or dfs(row,col+1,index+1) or dfs(row,col-1,index+1))

            board[row][col] = temp

            return found

        for i in range(maxR):
            for j in range(maxCol):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False