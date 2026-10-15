
# Open and read the file

student_file = open("Student Records.txt", "r")
records = student_file.readlines()
student_file.close()

# Print each student record with tabs between fields
for i in range(0, len(records), 3):
    name = records[i].strip()
    major = records[i + 1].strip()
    year = records[i + 2].strip()

    print(name + "\t" + major + "\t" + year)
    print()


# Open the file in append mode

student_file = open("Student Records.txt", "a")
student_file.write("Madison Gardner\nEducation\n2026\n")
student_file.close()

# Print the updated file

student_file = open("Student Records.txt", "r")
print(student_file.read())
student_file.close()


# Open and read the file

student_file = open("Student Records.txt", "r")
records = student_file.read()
student_file.close()

# Change the Engineering student's graduation year

records = records.replace(
    "Mary Smith\nEngineering\n2025",
    "Mary Smith\nEngineering\n2024"
)

# Rewrite the file with the updated information

student_file = open("Student Records.txt", "w")
student_file.write(records)
student_file.close()

# Print the final file

student_file = open("Student Records.txt", "r")
print(student_file.read())
student_file.close()
