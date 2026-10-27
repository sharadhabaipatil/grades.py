# Student Grade Calculator

# Accept student details
name = input("Enter student name: ")
department = input("Enter department: ")
semester = input("Enter semester: ")

# Accept marks in three subjects
mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

# Calculate average marks
average = (mark1 + mark2 + mark3) / 3

# Assign grade based on average marks
if average >= 90:
    grade = "S"
elif average >= 80:
    grade = "A"
elif average >= 65:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

# Display student details and result
print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("Department:", department)
print("Semester:", semester)
print("Subject 1 Marks:", mark1)
print("Subject 2 Marks:", mark2)
print("Subject 3 Marks:", mark3)
print("Average Marks:", round(average, 2))
print("Grade:", grade)