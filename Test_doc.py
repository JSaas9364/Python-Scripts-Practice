import random
import time


'''
random_list = [random.randint(-100, 100) for _ in range(20)]  # Generate a list of 10 random integers between 0 and 100
time_start = time.time()  # Start the timer
print(random_list)  

# Filtered list
#filtered_list = [element for element in random_list if -10 <= element <= 20]
#print(filtered_list)
    
def filter_and_sort(lst, min_value, max_value):
    lst.sort()
    filtered_list = []
    for element in lst:
        if min_value <= element <= max_value:
            filtered_list.append(element)
    return filtered_list


filtered_list = filter_and_sort(random_list, -10, 20)
print(f"Filtered list: {filtered_list}")

# Calculate the elapsed time
time_end = time.time()
elapsed_time = time_end - time_start
print(f"{elapsed_time:.10f}")  # Print the elapsed time

'''


'''
# Step 1: Prompt for title
title = input("Enter a title for the data:\n")
print(f"You entered: {title}\n")

# Step 2: Prompt for column headers
col1_header = input("Enter the column 1 header:\n")
print(f"You entered: {col1_header}\n")

col2_header = input("Enter the column 2 header:\n")
print(f"You entered: {col2_header}\n")

# Step 3: Collect data points with validation
data_points = []

while True:
    data_input = input("Enter a data point (-1 to stop input):\n")
    
    if data_input == "-1":
        break

    # Count the number of commas
    if data_input.count(',') == 0:
        print("Error: No comma in string.\n")
        continue
    elif data_input.count(',') > 1:
        print("Error: Too many commas in input.\n")
        continue

    # Split into name and value
    name, value = data_input.split(',', 1)
    name = name.strip()
    value = value.strip()

    # Error handling for integer
    if not value.isdigit():
        print("Error: Comma not followed by an integer.\n")
        continue

    # Confirmation output
    print(f"Data string: {name}")
    print(f"Data integer: {value}\n")

    data_points.append((name, int(value)))

# Step 4: Print the formatted table
print(f"\n{title}")
print(f"{col1_header:<33}| {col2_header:>20}")
print("-" * 55)

for name, value in data_points:
    print(f"{name:<33}| {value:>20}")

# Step 5: Print histogram
for name, value in data_points:
    print(f"{name:>33} {'*' * value}")


'''