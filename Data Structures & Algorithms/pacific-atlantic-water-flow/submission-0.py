class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl_set = set()
        pac_set = set()
        
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r,c,sett,prev):
            if ((r,c) in sett or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev):
                return

            sett.add((r,c))
            dfs(r + 1, c, sett, heights[r][c])
            dfs(r - 1, c, sett, heights[r][c])
            dfs(r, c + 1, sett, heights[r][c])
            dfs(r, c - 1, sett, heights[r][c])

            
        

        for r in range(rows):
            dfs(r,0,pac_set,heights[r][0])
            dfs(r,cols-1,atl_set,heights[r][cols-1])

        
        for c in range(cols):
            dfs(0,c,pac_set,heights[0][c])
            dfs(rows-1,c,atl_set,heights[rows-1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_set and (r, c) in atl_set:
                    res.append([r, c])
        return res