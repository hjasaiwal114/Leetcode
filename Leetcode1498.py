class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        res = 0
        mod = 10**9 + 7
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1
        return res