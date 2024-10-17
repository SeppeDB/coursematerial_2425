def earlier(h1, m1, h2, m2):
    minutes_1 = h1 * 60 + m1
    minutes_2 = h2 * 60 + m2

    return minutes_1 < minutes_2
