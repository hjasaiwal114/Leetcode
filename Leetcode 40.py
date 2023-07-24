class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1

        result = 1
        is_negative = False

        if exponent < 0:
            is_negative = True
            exponent = -exponent

        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return 1 / result if is_negative else result