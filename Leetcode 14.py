class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)

        for i in range(min_length):

            if any(strs[j][i] != strs[0][i] for j in range(1, len(strs))):

                return strs[0][:i]

        return strs[0][:min_length]