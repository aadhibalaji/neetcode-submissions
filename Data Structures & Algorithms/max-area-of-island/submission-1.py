class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        res = 0


        visit = set()

        def bfs(r, c):

            q = deque()
            visit.add((r, c))
            q.append((r, c))

            area = 1
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] == 1 and (r, c) not in visit:
                        area += 1
                        visit.add((r, c))
                        q.append((r, c))

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:

                    res = max(res, bfs(r, c))

        
        return res