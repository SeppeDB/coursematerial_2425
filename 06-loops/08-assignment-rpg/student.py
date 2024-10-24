def rpg2(n_sides, goal):
    valid_combinations = 0
    for i in range(1, n_sides + 1):
        for j in range(1, n_sides + 1):
            if i + j >= goal:
                valid_combinations += 1
                
    return valid_combinations / n_sides ** 2 * 100


def rpg3(n_sides, goal):
    valid_combinations = 0
    for i in range(1, n_sides + 1):
        for j in range(1, n_sides + 1):
            for k in range(1, n_sides + 1):
                if i + j + k >= goal:
                    valid_combinations += 1
                    
    return valid_combinations / n_sides ** 3 * 100
