'''import csv

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
'''
'''import csv

filename = 'input1.csv'

row1 = ['100', '200', '300']
row2 = ['400', '500', '600']


rowkeep = []
f = open(filename, 'r', newline = '')
reader = csv.reader(f)
for i, row in enumerate(reader):
    if i <= 2:
        #print(*row, "keep")
        rowkeep.append(row)
    else:
        #print(*row, "skip")
        continue
f.close()

f = open(filename, 'w', newline = '')
writer = csv.writer(f)
writer.writerows(rowkeep)
f.close()


f = open(filename, 'r', newline = '')
reader = csv.reader(f)
for row in reader:
    print(*row)
'''
'''with open(filename, 'a', newline = '') as f:
    writer = csv.writer(f)
#    writer.writerow(row1)
#    writer.writerow(row2)
    writer.writerow([row1, row2])
    writer.writerows([row1, row2])
with open(filename, 'r', newline = '') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''

'''
[' a', ' 100', ' b', ' 200', ' c', ' 300']
['bananas', ' 1.85', ' steak', ' 19.99', ' cookies', ' 4.52']
['apples', ' 2.99', ' chicken', ' 9.99', ' milk', ' 3.49']
['oranges', ' 3.49', ' fish', ' 12.99', ' bread', ' 2.99']
['pears', ' 4.99', ' pork', ' 14.99', ' eggs', ' 2.49']
['grapes', ' 5.99', ' beef', ' 17.99', ' cheese', ' 6.49']
'''