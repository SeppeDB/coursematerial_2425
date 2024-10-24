def remove_backspaces(string):
    if not string or string == "\b":
        return ""
    
    new_string = string[0]
    for i in range(1, len(string)):
        current_char = string[i]
        
        if current_char == "\b":
            new_string = new_string[:len(new_string) - 1]
        else:
            new_string += current_char
    
    return new_string

print(remove_backspaces("\b"))