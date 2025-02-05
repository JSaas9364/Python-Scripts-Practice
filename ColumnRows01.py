import nltk
from nltk.corpus import words
import random



'''
The given program reads a list of single-word first names and
ages (ending with -1), and outputs that list with the age incremented. 
The program fails and throws an exception if the second input on a line is a 
string rather than an integer.
At FIXME in the code, add try and except blocks to catch the 
ValueError exception and output 0 for the age.

'''


'''
# Read first input line
parts = input().split()
name = parts[0]

while name != '-1':  # Continue until sentinel value "-1"
    try:
        # Try to convert the second part to an integer and increment
        age = int(parts[1]) + 1
    except ValueError:
        # If conversion fails, set age to 0
        age = 0  

    # Print the result
    print(f"{name} {age}")

    # Read next line
    parts = input().split()
    name = parts[0]
'''















'''

nltk.download("words")


wordL = words.words()
x = 5 # Desired Char length

# Word length of 5 characters
Filtered_words = [word for word in wordL if len(word) == x]

# Word length range between 3 and 7 characters
filtered_words = [word for word in wordL if 4 <= len(word) <= 6]
# Random Dict with 5 words and 4 digit numbers
random_dict = {random.choice(filtered_words): random.randint(1000,9999) for _ in range(5)}
# Shuffle random dict items
random.shuffle(items := list(random_dict.items())) 

passphrase = "-".join(f"{word.capitalize()}{num}" for word, num in random_dict.items())
print(passphrase)
'''



'''
# Read the first line (list of integers)
nums = list(map(int, input().split()))

# Read the second line (lower and upper bounds)
lower, upper = map(int, input().split())

# Filter numbers that are within the range (inclusive)
filtered_nums = [num for num in nums if lower <= num <= upper]

# Print space-separated values
print(" ".join(map(str, filtered_nums)), end =" ")

'''

'''
for i in range(3):  # 3 rows
    row = [str(counter + j) for j in range(3)]  # Generate row of 3 numbers
    print(" ".join(row))  # Print row with spaces
    counter += 3  # Move to the next set of numbers

'''
'''
counter = 1  # Start counting from 1
row = []
columns = 3
rows = 3
for i in range(rows):  # 3 rows
    row = [(counter + j) for j in range(columns)]
    print(" ".join(map(str, row)))  # Print row
    counter += columns  # Move to the next set of numbers
''' 
'''
# Unoptimized
start = time.time()
for i in range(3):  # 3 rows
    for j in range(3):
        counter += 1
        row.append(counter)
    if len(row) == 3:
        print(" ".join(map(str, row)))
        row = []
end = time.time()
execution_time = end - start
print(f"Unoptimized: {execution_time}")
'''
'''
# Optimized   
start = time.time()

counter = 1  # Start counting from 1

for i in range(3):  # 3 rows
    row = [(counter + j) for j in range(3)]
    print(" ".join(map(str, row)))  # Print row
    counter += 3  # Move to the next set of numbers

end = time.time()
execution_time = end - start
print(f"Unoptimized: {execution_time}")
'''
