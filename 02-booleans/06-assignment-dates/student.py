<<<<<<< HEAD
def is_valid_month(month):
    return month >= 1 and month <= 12


def is_leap_year(year):
    divisible_4 = year % 4 == 0
    divisible_100 = year % 100 == 0
    divisible_400 = year % 400 == 0

    if divisible_4:
        if divisible_100 and divisible_400:
            return True

        if divisible_100 and not divisible_400:
            return False

        return True

    return False


def has_28_days(month, year):
    return month == 2 and not is_leap_year(year)


def has_29_days(month, year):
    return month == 2 and is_leap_year(year)


def has_30_days(month):
    return month == 4 or month == 6 or month == 9 or month == 11


def has_31_days(month):
    return (
        month == 1
        or month == 3
        or month == 5
        or month == 7
        or month == 8
        or month == 10
        or month == 12
    )


def is_valid_date(day, month, year):
    if not is_valid_month(month):
        return False

    if has_28_days(month, year):
        return day >= 1 and day <= 28

    if has_29_days(month, year):
        return day >= 1 and day <= 29

    if has_30_days(month):
        return day >= 1 and day <= 30

    if has_31_days(month):
        return day >= 1 and day <= 31

    return False
=======
# write your code here
>>>>>>> 9d2e6f6b0d66889fcf68a22f9172d09f0711fd68
