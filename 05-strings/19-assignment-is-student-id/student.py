<<<<<<< HEAD
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
=======
# write your code here
>>>>>>> 9d2e6f6b0d66889fcf68a22f9172d09f0711fd68
