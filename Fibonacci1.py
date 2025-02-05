import random
import time

#random_list = [random.randint(-100, 100) for _ in range(20)]  # Generate a list of 10 random integers between 0 and 100

def fibonacci(index):
    seq = [0, 1]  # Initialize the sequence
    for i in range(2, index + 1):  # Start from 2 and loop up to the desired index
        seq.append(seq[-1] + seq[-2])  # Append the next Fibonacci number
    return seq[index]  # Return the Fibonacci number at the given index
    
def Fibonacci(index):
    if index <= 1:
        return index
    else:
        return Fibonacci(index - 1) + Fibonacci(index - 2)
    
print("**** recursion ****")
rec = time.time()
print(Fibonacci(21))
print("speed" + str(time.time() - rec))

print("**** iteration ****")
it = time.time()
print(fibonacci(21))
print("speed" + str(time.time() - it))
