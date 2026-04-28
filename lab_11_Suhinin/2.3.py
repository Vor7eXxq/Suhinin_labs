
with open("grades.csv", "r", encoding="utf-8") as f:
    grades = f.readlines()

students = []
subjsums = [0,0,0,0,0]
for line in grades:
    data = line.strip().split(",")

    name = data[0]
    surname = data[1]
    grades = list(map(int, data[2:]))
    average = sum(grades)/len(grades)
    students.append({
        "name" : name,
        "surname" : surname,
        "average" : average
    })

    for i in range(5):
        subjsums[i] += grades[i]

best_student = students[0]
for student in students:
    if student["average"] > best_student["average"]:
        best_student = student

subjavg = []
for i in subjsums:
    subjavg.append(i/len(students))

with open("report.txt", "w", encoding="utf-8") as rep:
    rep.write("CЕРЕДНІ БАЛИ СТУДЕНТІВ:\n")

    for student in students:
        rep.write(
            f"{student["name"]} {student["surname"]}: {student["average"]:.1f}\n"
        )
    rep.write(
        "\nКРАЩИЙ СТУДЕНТ: \n"
        f"{best_student["name"]} {best_student["surname"]}: {best_student["average"]:.1f}\n"
    )
    rep.write("\nСЕРЕДНІ БАЛИ З ПРЕДМЕТІВ:\n")

    for i in range(5):
        rep.write(f"Предмет {i + 1}: {subjsums[i]:.1f}\n")