
'''
# UNOPTIMIZED VERSION
# This version uses a while loop and a nested for loop to find the solution.
# It sorts the array in descending order and uses a set to keep track of used numbers.
# It checks if the current sum is less than the target number and returns a message if no solution is found.
# The function returns the solution in a formatted string if a valid combination is found.
# The else statement after the for loop is redundant and can be removed for clarity.
# The while loop continues until the current sum is less than the target number.
# The function also uses a break statement to exit the for loop when a valid number is found.
# The function returns a message if no solution is found using only distinct values.
# The code is not optimized for performance and may not handle large arrays efficiently.
# The function does not handle the case where the input array is empty or the target number is zero.
# The function does not check for duplicate values in the input array and may return incorrect results if duplicates are present.
# The function does not handle the case where the input array contains negative numbers or zero.
# The function does not handle the case where the input array contains non-integer values.
# The function does not handle the case where the input array contains non-numeric values.
# The function does not handle the case where the input array contains non-unique values.
# The function does not handle the case where the input array contains non-distinct values.

def calculate(arr, no):
    arr.sort(reverse = True)
    sol, used, current_sum = [], set(), 0
    
    while current_sum < no:
        for num in arr:
            if num not in used and current_sum + num <= no:
                sol.append(num)
                used.add(num)
                current_sum += num
                break
        else:
            return "No solution found using only distinct values"
    return f"{' + '.join(map(str, sol))} = {no}"  # No redundant else

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no = int(input("Enter a number: "))
        
print(f"Solution: {calculate(arr, no)}")
'''

# OPTIMIZED VERSION
# This version uses a single loop and removes the while loop for efficiency. 
# It also ensures that the array is sorted in descending order and removes duplicates before processing.
# It checks if the sum of the array is less than the target number and returns a message if no solution is found. 
# The function returns the solution in a formatted string if a valid combination is found.

def calculate(arr, no):
    arr = list(set(arr)) # Remove dupes(O(n))
    arr.sort(reverse=True) # Sort in descending order(O(nlogn))
    
    if sum(arr) < no:
        return "No solution found using only distinct values"
    sol, used, current_sum = [], set(), 0
    #Single loop
    for num in arr:
        if current_sum + num <= no:
            sol.append(num)
            used.add(num)
            current_sum += num
            
        if current_sum == no:
            return f"{' + '.join(map(str, sol))} = {no}"
    return "No solution found using only distinct values"  # No redundant else
    # No need for a while loop as it is not required to keep checking once the sum is reached

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no = int(input("Enter a number: "))
        
print(f"Solution: {calculate(arr, no)}")