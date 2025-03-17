import time

list1 = [1,2,4,3]
list2 = [1,2]
list3 = [1,2,3,10]

combined_list = [list1, list2, list3]
highest_sum = float('-inf')  # Initialize to negative infinity
highest_sum_list = None  # To store the list with the highest sum
#print(combined_list)

for list in combined_list:
    current_sum = sum(list)
    print(f"Current sum: {current_sum}, Current_list: {list}")
    time.sleep(1)
    if highest_sum < current_sum:
        highest_sum = current_sum
        print(f"The highest sum is: {highest_sum}")
        highest_sum_list = list
        print(f"The highest sum list is: {list}")
        time.sleep(1)