class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                if board[r][c]  in columns[c]:
                    return False
                columns[c].add(board[r][c])

                if board[r][c] in squares[(r//3)*3 + (c//3)]:
                    return False
                squares[(r//3)*3 + (c//3)].add(board[r][c])

        return True



    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rows = len(board)
    #     columns = len(board[0])
    #     rowc, columnc, squarec = True, True, True
    #     for r in range(rows):
    #         row = [board[r][c] for c in range(columns) if board[r][c]!="."]
    #         if len(row) != len(set(row)):
    #             rowc = False
    #             break
    #     for c in range(columns):
    #         column = [board[r][c] for r in range(rows) if board[r][c]!="."]
    #         if len(column) != len(set(column)):
    #             columnc = False
    #             break
    #     for r in range(0,9,3):
    #         for c in range(0,9,3):
    #             square=[]
    #             for i in range(3):
    #                 for j in range(3):
    #                     if board[r+i][c+j]!=".":
    #                         square.append(board[r+i][c+j])
    #             if len(square)!=len(set(square)):
    #                 squarec = False
    #                 break
    #     return rowc and columnc and squarec
        
        
            
            


        