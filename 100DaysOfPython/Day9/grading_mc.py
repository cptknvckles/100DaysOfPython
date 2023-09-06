student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for student in student_scores :
    score = student_scores[student]
    if score in range(91, 100) :
        student_grades[student] = "Outstanding"
    elif score in range(81,90) :
        student_grades[student] = "Exceeds Expectations"
    elif score in range(71,80) :
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Troll"
print(student_grades)