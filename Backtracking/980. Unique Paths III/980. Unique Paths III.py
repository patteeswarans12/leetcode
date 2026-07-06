class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
            r=len(grid)
            n=len(grid[0])
            s1,s2=0,0
            c=0
            for i in range(r):
                for j in range(n):
                    if grid[i][j]==1:
                        s1,s2=i,j
                    if grid[i][j]!=-1:
                        c+=1
            m=0
            v=[[0]*n for i in range(r)]
            def solve(i,j,t):
                nonlocal m,c
            
                if i<0 or j<0 or i>=r or j>=n or grid[i][j]==-1 or v[i][j]==1:
                    return 'false'
                v[i][j]=1
            
                if t==c and grid[i][j]==2:
                    m+=1
                    v[i][j]=0
                    return 'false'
                solve(i-1,j,t+1)
                solve(i+1,j,t+1)
                solve(i,j-1,t+1) 
                solve(i,j+1,t+1)
                v[i][j]=0
                return 'false'
            solve(s1,s2,1)
            return m