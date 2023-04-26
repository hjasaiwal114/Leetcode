def add_digits(num):
    while num > 9:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num
