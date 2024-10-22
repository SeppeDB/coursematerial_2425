def gcd(x, y):
    x = abs(x)
    y = abs(y)

    lowest = min(x, y)
    highest = max(x, y)

    for i in range(lowest, 0, -1):
        if lowest % i == 0 and highest % i == 0:
            return i
