
def box(string):
    vert_line = "+" + ("-" * (len(string) + 2)) + "+"
    return vert_line + "\n" + "| " + string + " |\n" + vert_line