```python
# University Scholarship Allocation System

students = []

n = int(input("Enter the number of students: "))

for i in range(n):
    print("\nEnter details for Student", i + 1)

    name = input("Enter student name: ")
    marks = []

    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input("Enter marks for subject " + str(j + 1) + ": "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total = sum(marks)
    aggregate = total / subjects

    # Check eligibility
    eligible = True

    if aggregate < 75:
        eligible = False

    if attendance < 75:
        eligible = False

    if income > 250000:
        eligible = False

    for mark in marks:
        if mark < 40:
            eligible = False

    student = [
        name,
        aggregate,
        attendance,
        income,
        eligible
    ]

    students.append(student)

# Separate eligible students
eligible_students = []

for student in students:
    if student[4]:
        eligible_students.append(student)

# Sort by aggregate (descending),
# attendance (descending), income (ascending)
eligible_students.sort(
    key=lambda x: (-x[1], -x[2], x[3])
)

# Display results
print("\n========== SCHOLARSHIP RESULTS ==========")

if len(eligible_students) == 0:
    print("No students are eligible for the scholarship.")

else:
    print("\nEligible Students Ranked by Merit:")

    rank = 1

    for student in eligible_students:
        print(
            "Rank:", rank,
            "| Name:", student[0],
            "| Aggregate:", round(student[1], 2), "%",
            "| Attendance:", student[2], "%",
            "| Family Income: Rs.", student[3]
        )
        rank += 1

print("\nIneligible Students:")

found = False

for student in students:
    if not student[4]:
        print(student[0], "- Not eligible")
        found = True

if not found:
    print("None")
```