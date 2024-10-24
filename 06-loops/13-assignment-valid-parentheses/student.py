def valid_parentheses(string):
    opened = 0
    closed = 0
    total = 0

    for char in string:
        if char in "()":
            total += 1

        if char == "(" and opened >= closed:
            opened += 1

        if char == ")" and opened > closed:
            closed += 1

    return opened + closed == total and closed == opened

print(valid_parentheses("((((((((()(()))("))