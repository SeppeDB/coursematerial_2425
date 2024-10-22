def parse_position_x(string):
    string = string[1 : len(string) - 1]
    return float(string.split(",")[0].strip())


def parse_position_y(string):
    string = string[1 : len(string) - 1]
    return float(string.split(",")[1].strip())
