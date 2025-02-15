import csv

grades = []
total_mid1 = total_mid2 = total_final = 0
num_students = 0

# Read the file
with open('StudentInfo.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')  # Tab delimiter
    data = list(reader)

# Function to assign a letter grade
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Process each student and compute running sums for averages
for row in data:
    last_name, first_name, mid1, mid2, final = row
    mid1, mid2, final = map(int, [mid1, mid2, final])  # Convert scores to integers

    # Compute student average
    avg_score = (mid1 + mid2 + final) / 3
    letter_grade = assign_grade(avg_score)

    # Append student data to grades list
    grades.append([last_name, first_name, mid1, mid2, final, letter_grade])

    # Running totals for calculating averages
    total_mid1 += mid1
    total_mid2 += mid2
    total_final += final
    num_students += 1

# Compute exam averages (Ensure correct rounding)
midterm1_avg = round(total_mid1 / num_students, 2)
midterm2_avg = round(total_mid2 / num_students, 2)
final_avg = round(total_final / num_students, 2)

# Write to report.txt with proper formatting
with open('report.txt', 'w') as file:
    # Write each student's data using tab separation
    for student in grades:
        file.write(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\n")

    # Append the exam averages at the end with correct formatting
    file.write(f"\nAverages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n")
