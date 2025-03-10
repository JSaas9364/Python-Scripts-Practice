arr = [5, 3, 8, 6, 2, 7, 4, 1, 25, 9, 10, 11, 12, 13, 14, 15, 100]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

sorted_arr = quicksort(arr)
print(sorted_arr)