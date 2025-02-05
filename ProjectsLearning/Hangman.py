print("Welcome to Hangman!")
print("Enter 'quit' to quit at any time or any other key to continue: ")

# Valid word Entry Check
while True:
    try:
        word = str(input("Enter the word you'd like to guess: "))
        if not word.isalpha():
            raise ValueError()
        elif len(word) < 3:
            raise ValueError()
        elif word == "quit":
            raise ValueError()
        break
    except ValueError as e:
        print(f"{word} was an invalid input, enter valid words only")
obfuscate_word = '-' * len(word)
max_guesses = len(word) - 1
guess_counter = 0
word_bank = []

# Game Loop
while guess_counter <= max_guesses  and '-' in obfuscate_word:
    
    if len(word_bank) > 0:
        print(f"Word: {obfuscate_word}, letters guessed:{word_bank}, tries remaining: {max_guesses - guess_counter}")
    try:
        word_guess = str(input("Enter your guess: "))
        if word_guess.lower() == word.lower():
            print("You've Won!!")
            break
        elif len(word_guess) != 1:
            raise ValueError
        elif not word_guess.isalpha():
            raise ValueError
        elif word_guess.lower() == "quit":
            break
    except ValueError:
        print("Invalid Entry")
        guess_counter += 1
        
    if word_guess in word_bank:
        print("Already guessed, try a different letter")
        guess_counter += 1
        continue
    else:
        word_bank.append(word_guess)
    
    if word_guess in word:
        obfuscate_word = ''.join(word_guess if word [i] == word_guess else obfuscate_word[i] for i in range(len(word)))
        if obfuscate_word == word:
            print(f"You won!")
    else:
        print(f"{word_guess}, not in {obfuscate_word}")
        guess_counter += 1 
        
    if word_guess.lower() == "quit":
        break
    else:
        continue
    
# Ending Game Loop
if '-' not in obfuscate_word:
    print(f"Congratulations! You guessed the word: {word}")
elif guess_counter >= max_guesses:
    print(f"You've run out of guesses. The word was: {word}") 
    

