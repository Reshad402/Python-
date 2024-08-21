student_score ={
    "Harry": 81,
    "Ron": 78,
    "her":99,
    "draco":74
}

student_grade = {}
for student in student_score:
    score = student_score[student]
    print(score)
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectation" 
    elif score > 70:
        student_grade[student] = "Accepts Expectation"
    else:
        student_grade[student] = "fail"
print(student_grade)