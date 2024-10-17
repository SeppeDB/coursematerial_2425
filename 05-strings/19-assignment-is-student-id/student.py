def is_student_id(string):
    string = string.lower()
    first_char = string[0]
    remaining_chars = string[1:]

    if len(string) != 8:
        return False

    if first_char not in ("r", "s"):
        return False

    if not remaining_chars.isdigit():
        return False

    return True
