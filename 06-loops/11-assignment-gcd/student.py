def gcd(x, y):
    lowest = min(abs(x), abs(y))

    for i in range(lowest, 0, -1):
        if x % i == 0 and y % i == 0:
            return i