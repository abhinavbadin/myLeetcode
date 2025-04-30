class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(row,col,vis,grid):
            vis[row][col] = 1
            q = deque()
            q.append((row,col))
            m = len(grid)
            n = len(grid[0])
            area = 0
            while q:
                row,col = q.popleft()
                area +=1
                #traverse the neighbours
                directions = [(-1,0), (1,0), (0,-1), (0,1)]
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if(nr >=0 and nr < m and nc>=0 and nc < n and grid[nr][nc]==1 and vis[nr][nc]==0):
                        vis[nr][nc] = 1
                        q.append((nr,nc))
            return area
    
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        islands = 0
        max_area = 0
        for row in range(0,m):
            for col in range(0,n):
                if visited[row][col] == 0 and grid[row][col] == 1:
                    ar = bfs(row,col,visited,grid)
                    max_area = max(ar, max_area)
                    islands+=1
        return max_area 