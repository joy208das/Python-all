'''Grading program'''

student_scores={
 "harry":81,
 "joy":90,
 "bag":25,
 "goat":69,
 "messi":100
}
grade={}
for n in student_scores:
    score=student_scores[n]
    if score>90:
     grade[n]="outstanding"
    elif score>80:
     grade[n]="good"
    elif score>70:
     grade[n]="nice"
    elif score>60:
     grade[n]="ok"
    else :
     grade[n]="not so good"

print(grade)       
