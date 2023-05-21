from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visit = set()

        def is_invalid(r, c):
            return r < 0 or c < 0 or r >= N or c >= N

        def dfs(r, c):
            if is_invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            res, queue = 0, deque(visit)
            while queue:
                length = len(queue)
                for _ in range(length):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if is_invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC] == 1:
                            return res
                        visit.add((curR, curC))
                        queue.append((curR, curC))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()