def drop_last_digit(n):
    last = n % 10
    n = (n - last) / 10
    return n
