class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1. Check Rows & Columns
        for i in range(9):
            seen_r=set()
            seen_c=set()
            for j in range(9):
                row=board[i][j]
                col=board[j][i]
                if row != ".":
                    if row in seen_r:
                        return False
                    seen_r.add(row)
                if col != ".":
                    if col in seen_c:
                        return False
                    seen_c.add(col)
        #2. Check Sub-boxes
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col=(square%3)*3+j
                    if board[row][col]==".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

            



                



    