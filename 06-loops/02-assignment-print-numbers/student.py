def print_numbers(start, stop, step):
    i = 0
    while start + i * step < stop:
        print(start + (i * step))
        i += 1


print_numbers(5, 10, 2)
