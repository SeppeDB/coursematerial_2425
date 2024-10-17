# 5 / 2 / 1
def coins(amount):
    coin_qty = coin_5(amount)
    amount -= coin_5(amount) * 5

    coin_qty += coin_2(amount)
    amount -= coin_2(amount) * 2

    coin_qty += amount

    return coin_qty


def coin_5(amount):
    return amount // 5


def coin_2(amount):
    return amount // 2
