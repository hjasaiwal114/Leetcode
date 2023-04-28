class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        adj = self.createGraph(strs, n) # Create an adjacency list to represent the graph
        vis = [False] * n # Create a boolean array to keep track of visited nodes
        ans = 0
        for i in range(n):
            if not vis[i]: # Traverse the graph using DFS and count the number of connected components
                self.dfs(i, vis, adj)
                ans += 1
        return ans

    def dfs(self, i: int, vis: List[bool], adj: List[List[int]]) -> None: # Depth-first search to traverse the graph
        vis[i] = True
        for j in adj[i]:
            if not vis[j]:
                self.dfs(j, vis, adj)

    def createGraph(self, strs: List[str], n: int) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]): # Check if two strings are similar with max of 1 swap
                    ans[i].append(j)
                    ans[j].append(i)
        return ans

    def isSimilar(self, a: str, b: str) -> bool:
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
        return c == 0 or c == 2