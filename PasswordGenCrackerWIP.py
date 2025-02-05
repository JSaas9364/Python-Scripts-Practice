import random
import string
import nltk
from nltk.corpus import words
nltk.download('words')

numRandPass = 4  # Number of random passwords
wordLen = 4  # Length of each word
allowedPunctuation = "!@#$%&*()-_=+"


''' Password generator'''
# Load words corpus correctly
word_list = [word.capitalize() for word in words.words() if len(word) == wordLen]
randNumArray = [random.randint(10**(wordLen-1), 10**(wordLen)-1) for _ in range(numRandPass)]

def generate_arrays(num_items=numRandPass):
    """Generate equal-length arrays of words and numbers."""
    word_array = [random.choice(word_list) for _ in range(num_items)]
    num_array = [random.choice(randNumArray) for _ in range(num_items)]
    return word_array, num_array

def shuffle_word(word):
    """Shuffle the characters of a word."""
    word_chars = list(word)
    random.shuffle(word_chars)
    return ''.join(word_chars)

def merge_arrays(word_array, num_array):
    """Merge the two arrays into a single array where each word is paired with a number."""
    return [f"{shuffle_word(word)}{num}" for word, num in zip(word_array, num_array)]

def array_salt(merged_array):
    """Salt the merged array with random punctuation and uppercase letters, then shuffle."""
    salted_array = [f"{item}{random.choice(allowedPunctuation)}{random.choice(string.ascii_uppercase)}"
                    for item in merged_array]
    random.shuffle(salted_array)
    return salted_array

def save_to_file(passwords, filename="Passkeys.txt"):
    with open(filename, 'a') as file:
        for password in passwords:
            file.write(password+"\n")
    print(f"{len(passwords)} passwords appended to {filename}")


merged_array = merge_arrays(*generate_arrays()) # Generate and merge arrays
salted_array = array_salt(merged_array) # Salt and shuffle the merged array
save_to_file(salted_array, "Passkeys.txt") # Save the salted and shuffled array to a file

# Print the final salted and shuffled array
print("Salted & Shuffled Array:", salted_array)


''' Brute force cracker'''
import itertools

def brute_force_crack(target_password, max_length=8):
    """Attempts to crack a password using a brute force attack."""
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    for length in range(1, max_length+1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if guess == target_password:
                print(f"Password cracked: {guess}")
                return guess
    print("Failed to crack password.")
    return None


'''Dictionary Attack Simulation'''
def dictionary_crack(target_password, dictionary_file="Passkeys.txt"):
    """Attempts to crack a password using a wordlist (dictionary attack)."""
    try:
        with open(dictionary_file, "r") as file:
            for line in file:
                guess = line.strip()
                if guess == target_password:
                    print(f"Password cracked: {guess}")
                    return guess
    except FileNotFoundError:
        print("Dictionary file not found.")
    
    print("Failed to crack password.")
    return None

# Example usage
password_to_crack = "Tgori39284@L"
dictionary_crack(password_to_crack)
