class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        leng=len(matrix)
        t=leng//2
        for i in range(t): #홀수, 짝수 나눠서
            for j in range(i,leng-1-i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[leng-1-j][i]
                matrix[leng-1-j][i]=matrix[leng-1-i][leng-1-j]
                matrix[leng-1-i][leng-1-j]=matrix[j][leng-1-i]
                matrix[j][leng-1-i]=temp
            print(matrix)
            
        return matrix
