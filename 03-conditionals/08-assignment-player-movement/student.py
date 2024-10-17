def player_movement(position, left_arrow, right_arrow, shift):
    return position + ((left_arrow * -1 + right_arrow) * (shift + 1))
