class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            while queue:
                row,col = queue.popleft()
                for (x,y) in directions: 
                    nr = row + x 
                    nc = col + y
                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or (nr, nc) in visited
                        or grid[nr][nc] == "0"
                    ):
                        continue 
                   
                    visited.add((nr,nc))
                    queue.append((nr,nc))


        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    count = count + 1
        return count 