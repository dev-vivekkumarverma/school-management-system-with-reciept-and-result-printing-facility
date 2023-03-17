def grade_decider(percentage):
    if percentage >= 75:
        return 'A+'
    elif percentage >=60 and percentage < 75:
        return 'A'
    elif percentage >=45 and percentage <60:
        return 'B'
    elif percentage >= 33 and percentage <45 :
        return 'C'
    else:
        return 'D'


def division_decider(percentage):
    if percentage >= 85 :
        return "Distinction"
    elif percentage >= 60 and percentage < 85:
        return "1st Div"
    elif percentage >= 45 and percentage <60:
        return "2nd Div"
    elif percentage >= 33 and percentage < 45:
        return "3rd Div"
    else:
        return "Fail"

