def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


with open("nameslist.txt", "r") as f:
    words = f.read().splitlines()
    
# call function
frequency = count_word_frequency(words)
print(frequency)

from collections import Counter

for word, count in frequency.items():
    print(f"{word}: {count}")