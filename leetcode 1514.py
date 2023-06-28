class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            s, e = edges[i]
            graph[s].append((-succProb[i], e))
            graph[e].append((-succProb[i], s))
        max_heap = [(-1, start)]
        visited = set()
        while max_heap:
            p, node = heapq.heappop(max_heap)
            if node == end:
                return -p
            visited.add(node)
            for q, adj in graph[node]:
                if adj not in visited:
                    heapq.heappush(max_heap, (-(p*q), adj))
        return 0