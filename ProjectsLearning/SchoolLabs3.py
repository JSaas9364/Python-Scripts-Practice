numarray = [2, 3, 20, 11, 7, 19, 7, 8, 14, 19]



def findpair(numarray, target):
    for i in range(len(numarray)):
        for j in range(i + 1, len(numarray)):
            if numarray[i] + numarray[j] == target:
                return (numarray[i], numarray[j])
    return None

target = 5
result = findpair(numarray, target)
if result:
    print(f"Pair found: {result}")
else:
    print("No pair found")
    
    
    
 numarray = [2, 3, 20, 11, 7, 19, 7, 8, 14, 19]

def findpair(numarray, target):
    for i in range(len(numarray)):
        for j in range(i + 1, len(numarray)):  # Ensure j starts after i
            if numarray[i] + numarray[j] == target:
                return (i, j)  # Correctly returning indices

    return None  # If no pair is found

target = 5
result = findpair(numarray, target)

if result:
    print(f"Pair found at indices: {result}")
else:
    print("No pair found")
