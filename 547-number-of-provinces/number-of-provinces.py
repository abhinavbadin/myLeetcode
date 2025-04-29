class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(n,array,vs):
            vs[n] = 1
            for it in array[n]:
                if vs[it] != 1:
                    dfs(it,array,vs)
        
        n = len(isConnected)
        visited = [0] * (n+1)
        counter = 0
        
        adj_dict = {i+1: [] for i in range(n)}
    
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    adj_dict[i+1].append(j+1)
                    adj_dict[j+1].append(i+1)
        
        for i in range(1,n+1):
            if visited[i] != 1:
                counter +=1
                dfs(i,adj_dict,visited)
                
        
        return counter