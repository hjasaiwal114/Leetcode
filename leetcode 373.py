class Solution:
    def kSmallestPairs(self, A: List[int], B: List[int], k: int) -> List[List[int]]:
        n = len(A)
        m = len(B)
        pq = []
        hashSet = set()
        ans = []
        heappush(pq, (A[0] + B[0], 0, 0))
        hashSet.add((0, 0))
        while pq and k > 0:
            min_val, i, j = heappop(pq)
            ans.append([A[i], B[j]])
            if i < n - 1 and (i + 1, j) not in hashSet:
                heappush(pq, (A[i + 1] + B[j], i + 1, j))
                hashSet.add((i + 1, j))
            if j < m - 1 and (i, j + 1) not in hashSet:
                heappush(pq, (A[i] + B[j + 1], i, j + 1))
                hashSet.add((i, j + 1))
            k -= 1
        return ans