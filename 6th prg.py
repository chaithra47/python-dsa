student = {}
for i in range(3):
    name = input("enter name of student {i + 1}")
    marks = int(input("enter marks of student {i + 1}"))
    student[name] = marks
Topper = max(student, key = student.get)
print("topper is", topper)

