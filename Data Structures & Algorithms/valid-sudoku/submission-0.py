class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=defaultdict(list)
        row=defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in row[i] or board[i][j] in col[j]:
                        return False
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
        for i in range(0,9,3):
            for j in range(0,9,3):
                box=set()
                for k in range(i,i+3):
                    for p in range(j,j+3):
                        if board[k][p]!="." and board[k][p] in box:
                            return False
                        box.add(board[k][p])
        return True