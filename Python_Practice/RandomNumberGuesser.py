import random
import re
import time

################################################################
# Game Intro
print("Number Guesser!\n")

while True:
    playing = input("Do you want to play? \nEnter Yes or No: ").lower().strip()
    
    # Check if yes or no
    if playing in["no", "n"]:
        quit()
    elif playing in ["yes", "y"]:
        break
    else:
        print("Invalid input. Please enter Yes or No")
        
#Penalty Checker
lowerScore = input("Do you want wrong guesses to lower your score? (Yes or No): ").lower()
apply_penalty = lowerScore in ["yes", "y"]
print("Penalty On" if apply_penalty else "Penalty Off")

# Get the number of rounds
while True:
    try:
        times = int(input("OK, How many times?: ").strip())
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#################################################################
# Pre-Game Probability scores
#Counter Scores
score = 0

# Set game question and answer parameters
while True:
    try:
        number_Ranges = int(input("Enter your number range 2 - 100: ").strip())
        player_Guesses = int(input("How guesses would you like? between 1 - 10: ").lower().strip())
        
        # Check for valid ranges
        if 2 <= number_Ranges <= 100 and 1 <= player_Guesses <= 10:
            print("\nStarting Game...\n")
            break # Exit Loop on valid input
        else:
            # print error based on input
            if not (2 <= number_Ranges <= 100):
                print("Invalid input! Number not in range 2 - 100, Try again. ")
            if not (1 <= player_Guesses <= 10):
                print("Invalid input! Number not in range 1 - 10, Try again. ")
    except ValueError:
        print("Invalid Input! Please enter a valid number between 2 and 100")
        
# Calculate probability of winning 
singleRoundProbability = (player_Guesses / number_Ranges)
# Cap odds at 100%
singleRoundProbability = min(singleRoundProbability, 1)
# Calculate overall Probability of winning
overallProbability = 1 - (1 - singleRoundProbability) ** times
# Convert probabilities to percentages  
singleRoundProbability *= 100
overallProbability *= 100

# Display probabilities
print(f"Your odds of winning a round are {singleRoundProbability:.0f}%, if playing optimally.")
print(f"Your odds of winning at least once are {overallProbability:.0f}%, if playing optimally. ")

###########################################################
#Main Game Loop for Multiple Rounds
for round_num in range(1, times + 1):
        
    # Take user input, sort, and filter
    while True:
        try:
            # Take input and generate guess list
            print("", end="", flush=True)
            guess_List = input(f"\nEnter your {player_Guesses} guesses, separated by spaces or commas:\n").strip()
            # Split input by spaces or commas
            raw_guesses = re.split(r"[ ,]+", guess_List)
            
            # Init Tracking
            valid_guesses = []
            seen = set()
            
            # Process each input and add valid guesses
            for num in raw_guesses:
                try:
                    guess = int(num)
                    #include only valid guesses within range and not dupe
                    if 1 <= guess <= number_Ranges and guess not in seen:
                        valid_guesses.append(guess)
                        seen.add(guess)
                        #stop on limit reached
                        if len(valid_guesses) == player_Guesses:
                            break
                except ValueError:
                    #ignore non-integer values
                    continue
                
            # Check for empty list after filtering
            if not valid_guesses:
                print ("Invalid input! please enter at least one valid number within the specified range... ")
                continue
            
            valid_guesses.sort()
            # Print the filtered, unique guesses limited to the first player_Guesses entries
            print("You guessed:", ', '.join(map(str, valid_guesses)))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            
    # Countdown animation
    print("\nGenerating a random number...", end=" ")
    for _ in range(5):
        random_display = random.randint(1, number_Ranges)
        print(f" {random_display}", end=" ", flush=True)
        time.sleep(0.5)
    
    # Generate a random number for the game - after taking guesses to avoid cheating
    random_number = random.randint(1, number_Ranges)
    
    # Check if number is in user guesses
    if random_number in valid_guesses:
        print(f"The answer was {random_number}. You guessed right!")
        score += 1
    
    else:
        print(f"The answer was {random_number}. You guessed wrong!")
        score -= 1
        
    # Update player on score
    print(f"Your score is: {score}")

#################################################################
# Game ending win or loss
print("\nGame Over!")
print(f"Your final score is: {score} out of {times}")

if score < 2:
    print("Better Luck Next Time!")
elif 2 <= score <= 5:
    print("Good effort! Keep practicing!")
else:
    print("Wow! Superb!")
