class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat=[[0]*n for i in range(m)]
        
        mat[m-1][n-1]=1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1<m:
                    mat[i][j]+=mat[i+1][j]
                if j+1<n:
                    mat[i][j]+=mat[i][j+1]

        return mat[0][0]
        