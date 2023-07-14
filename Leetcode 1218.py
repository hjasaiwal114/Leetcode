"""
1218. Longest Arithmetic Subsequence of Given Difference
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.
"""

from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], dif: int) -> int:
        # Create a defaultdict to store the lengths of subsequences
        lengths = defaultdict(lambda: 0)
        
        # Iterate over the array elements
        for num in arr:
            # Calculate the length of the subsequence ending at the current element
            lengths[num] = lengths[num - dif] + 1

        # Return the maximum length of subsequences
        return max(lengths.values())