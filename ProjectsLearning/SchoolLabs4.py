
'''
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