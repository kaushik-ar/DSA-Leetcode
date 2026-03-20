class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        columns = len(board[0])
        rowc, columnc, squarec = True, True, True
        for r in range(rows):
            row = [board[r][c] for c in range(columns) if board[r][c]!="."]
            if len(row) != len(set(row)):
                rowc = False
                break
        for c in range(columns):
            column = [board[r][c] for r in range(rows) if board[r][c]!="."]
            if len(column) != len(set(column)):
                columnc = False
                break
        for r in range(0,9,3):
            for c in range(0,9,3):
                square=[]
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j]!=".":
                            square.append(board[r+i][c+j])
                if len(square)!=len(set(square)):
                    squarec = False
                    break
        return rowc and columnc and squarec
        
        
            
            


        