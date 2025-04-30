class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(sr,sc,col,mod,img,ini):
            mod[sr][sc] = col
            m = len(img)
            n = len(img[0])
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr,dc in directions:
                nr = sr + dr
                nc = sc + dc
                if(nr >=0 and nr < m and nc>=0 and nc < n and img[nr][nc]== ini and mod[nr][nc]!=col):
                        dfs(nr,nc,col,mod,img,ini)

        modified = image
        initial = image[sr][sc]
        dfs(sr,sc,color,modified,image,initial)
        return modified