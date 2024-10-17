def multiple_choice(right_answer, given_answer):
    return [1, -0.2, 0][((0, 1)[given_answer != right_answer], 2)[given_answer == None]]
