class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1
        
        lo = 1
        hi = max(dist) * 100
        while (lo < hi):
            speed = (lo + hi) // 2
            time = 0
            for i in range(n-1):
                time += math.ceil(dist[i] / speed)
            time += dist[-1] / speed
            if time <= hour:
                hi = speed
            else:
                lo = speed + 1

        return lo