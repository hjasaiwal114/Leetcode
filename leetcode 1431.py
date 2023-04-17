class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        stack = []
        max_candies = max(candies)
        for i in range(len(candies)):
            check = candies[i] + extraCandies
            if check >= max_candies:
                stack.append(True)
            else:
                stack.append(False)
        return stack