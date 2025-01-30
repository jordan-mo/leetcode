'''
Difficulty: Medium
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
'''
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and (i, j) not in visited:
                    #print(i,j)
                    q = deque([(i, j)])
                    tmp = 0
                    while q:
                        x, y = q.popleft()
                        if (x, y) in visited:
                            continue
                        tmp += grid[x][y]
                        for dx, dy in d:
                            mx, my = dx+x, dy+y
                            if 0 <= mx < n and 0 <= my < m:
                                if grid[mx][my] != 0:
                                    q.append((mx, my))
                        visited.add((x, y))
                    res = max(res, tmp)
            
        return res