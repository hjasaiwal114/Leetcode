class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)
        n = len(isConnected)
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return components
