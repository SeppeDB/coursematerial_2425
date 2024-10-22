def invest(amount, rate, goal):
    years = 0
    while amount < goal:
        amount *= rate / 100 + 1
        years += 1

    return years
