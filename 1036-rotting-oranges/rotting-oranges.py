class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for i in range(n)] for j in range(m)]
        mtime = 0
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and visited[i][j]!=2:
                    q.append((i,j,mtime))
                    visited[i][j] = 2
        while q:
            row,col,time = q.popleft()
            mtime = max(time,mtime)
            #traverse the neighbours
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr,dc in directions:
                nr = row + dr
                nc = col + dc
                if(nr >=0 and nr < m and nc>=0 and nc < n and grid[nr][nc]==1 and visited[nr][nc]!=2):
                    visited[nr][nc] = 2
                    q.append((nr,nc,time+1))    
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j]!=2:
                    return -1
        
        return mtime