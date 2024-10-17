def is_capitalized(string):
    if len(string) == 1:
        return string[0] == string[0].upper()

    if len(string) > 1:
        return string[0] == string[0].upper() and string[1:] == string[1:].lower()

    return False
