# Get input and split it into the character and phrase
user_input = input().strip()
char = user_input[0]  # The first character is the one to count
phrase = user_input[2:]  # The rest of the input is the phrase

# Count occurrences of the character in the phrase
count = phrase.count(char)

# Determine correct pluralization
if count == 1:
    print(f"{count} {char}")
else:
    print(f"{count} {char}'s")


inputs = input().strip().split()
char = inputs[0]
phrase = inputs[2:]
count = phrase.count(char)

if count == 1:
    print(f"{count} {char}")   
else:
    print(f"{count} {char}'s")