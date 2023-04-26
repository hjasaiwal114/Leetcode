class less_Optimal():
    def add_digits(num):
        while num > 9:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            num = digit_sum
        return num
class more_optimal():
    def add_digits(num):
    if num == 0:
        return 0
    return 1 + ((num - 1) % 9)
# formula (num - 1) % 9

