def middle(a, b, c):
    ceil = max(a, b, c)
    floor = min(a, b, c)
    mid = (a + b + c) - ceil - floor

    return mid
