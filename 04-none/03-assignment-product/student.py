def product(a, b, c):
    return (a, 1)[a == None] * (b, 1)[b == None] * (c, 1)[c == None]
