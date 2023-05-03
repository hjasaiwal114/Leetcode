class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums)
        res = [[] , []]
        for num1 in nums1:
            if num1 not in s2 and num1 not in res[0]:
                res[0].append(num1)

        for num2 in nums2:
            if num2 not in s1 and num2 not in res[1]:
                res[1].append(num2)
            
        return res
