class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]

        def solve(row : int , col :int ) -> None :
            if row < 0 or col < 0 or row >= n or col >= m or grid[row][col] == '0' or vis[row][col] :
                return        

            vis[row][col] = True
            solve(row + 1, col)
            solve(row - 1,col)
            solve(row ,col + 1)
            solve(row,col - 1)

        res  = 0
        for i in range(n) :
            for j in range(m) :
                if not vis[i][j] and grid[i][j] == '1' :
                    res += 1
                    solve(i,j)

        return res
