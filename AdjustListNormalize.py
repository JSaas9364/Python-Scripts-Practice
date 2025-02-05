
import random
import time

time_start = time.time()  # Start the timer


randints = [random.randint(1, 100) for _ in range(100)]
#randints = list(map(int, input().split()))

# The words parameter is a list of strings.
# The words parameter is a list of strings.
def build_dictionary(words):
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies
    

# The following code asks for input, splits the input into a word list, 
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input("Enter words separated by spaces: ").split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))



time_end = time.time()
elapsed_time = time_end - time_start
print(f"{elapsed_time:.10f}")  # Print the elapsed time


