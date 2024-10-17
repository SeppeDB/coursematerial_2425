def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    grades = [grade1, grade2, grade3, grade4, grade5]
    valid_grades = [x for x in grades if x != None]

    if len(valid_grades) < 4:
        return False

    return (sum(valid_grades) / len(valid_grades)) >= 12
