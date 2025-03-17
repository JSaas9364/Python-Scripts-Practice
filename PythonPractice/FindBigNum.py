import time

# First Approach: Reading All at Once
start_time = time.time()

with open("list_content.txt") as file:
    content = file.readlines()
    content = " ".join(content).replace(",", " ").replace("\n", " ")
    num_list = [int(num) for num in content.split()]

print("Max number (Method 1):", max(num_list))
print("Execution Time (Method 1):", time.time() - start_time, "seconds\n")


# Second Approach: Optimized Line-by-Line Processing
start_time = time.time()

max_num = float('-inf')  # Initialize with the smallest possible number

with open("list_content.txt") as file:
    for line in file:
        for num in line.replace(",", " ").split():
            number = int(num)
            if number > max_num:
                max_num = number  # Update max if a larger number is found

print("Max number (Method 2):", max_num)
print("Execution Time (Method 2):", time.time() - start_time, "seconds")
