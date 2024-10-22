def sum_input():
    sum = 0
    while True:
        nr = int(input("Enter integer: "))

        if nr == 0:
            break

        sum += nr

    print(f"The sum equals {sum}.")
