grades = [45, 85, 90, 67, 33, 78, 92, 100, 55]
old_grade = filter(lambda x: x >= 60, grades)
new_grade = map(lambda x: round((x / 100) * 12),old_grade)
print(list(new_grade))