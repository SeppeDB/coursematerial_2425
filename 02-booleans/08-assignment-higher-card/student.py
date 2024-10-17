def higher_card(card1, card2):
    if card1 == 1:
        card1 += 13

    if card2 == 1:
        card2 += 13

    return card1 > card2
