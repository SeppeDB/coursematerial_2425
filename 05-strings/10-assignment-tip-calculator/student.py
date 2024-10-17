def tip_calculator():
    total_price = int(input("Enter total price: "))
    tip_percentage = input("Enter tip percentage (default=20): ")

    if tip_percentage == "":
        tip_percentage = 1.2
    else:
        tip_percentage = int(tip_percentage) / 100 + 1

    print(f"You have to pay {round(total_price * tip_percentage)}")
