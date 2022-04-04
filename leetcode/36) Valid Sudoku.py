class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rows=[]
            columns=[]
            for j in range(len(board)):
                row=board[i][j]
                column=board[j][i]
                if row!='.' and row in rows:
                    return False
                else:
                    rows.append(row)
                    
                if column!='.' and column in columns:
                    return False
                else:
                    columns.append(column)
        li=[0,3,6]           
        for i in li:
            datas=[]
            for j in li:
                datas=[]
                for k in range(3):
                    for l in range(3):
                        data=board[i+k][j+l]
                        if data!='.' and data in datas:
                            return False
                        else:
                            datas.append(data)
        return True
                        
