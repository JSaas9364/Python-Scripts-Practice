'''
def get_month_as_int(monthString):
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int

# Get first user input
user_input = input()

while user_input != "-1":  # Ensure comparison is with a string
    parts = user_input.split()
    
    if len(parts) == 3 and "," in parts[1]:  # Validate input format
        month = parts[0]
        day = parts[1].replace(",", "")  # Remove comma
        year = parts[2]

        month_int = get_month_as_int(month)  # Convert month to number

        if month_int != 0 and day.isdigit() and year.isdigit():
            print(f"{month_int}/{day}/{year}")  # Print formatted date

    user_input = input()  # Get next input

'''
'''
import csv

filename = 'input1.csv'  # Change to input() if needed

my_dict = {}

with open(filename, 'r') as file:
    reader = csv.reader(file)
    rows = [list(map(str.strip, row)) for row in reader] # list map str strip row - strip leading and ending whitespace
    #print(rows)
    for row in rows:
        my_dict = {row[i]: row[i + 1] for i in range(0, len(row), 2)}
        print(my_dict)
        
########################

with open(filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = [list(map(str.strip, row)) for row in reader]  # Strip leading/trailing spaces

    for row in rows:
        row_dict = {row[i]: row[i + 1] for i in range(0, len(row), 2)}  # Convert row into dictionary
        print(row_dict)  # Output each row as a dictionary
'''
'''
arr = list(map(int, [100, 50, 60, 140, 200, 75, -1]))

def output(array, threshold):
    for num in array:
        if num == -1:
            break
        if num <= threshold:
            print(num)

if __name__ == '__main__':
    threshold = int(arr[0])
    array = arr
    output(array, threshold)
'''

'''words = 'hey Hi Mark hi mark hi hi mark Mark Hey Bob'  # Given words as a string
w = words.lower().split()
arr = []
counts = []

for word in w:
    if word not in arr:
        arr.append(word)
        counts.append(1) # Start counter at 1
    else:
        counts[arr.index(word)] += 1

output = list(zip(arr, counts))
results = ', '.join([f"{word} {count}" for word, count in output])
print(results)'''

'''
for word in w:
    if word not in arr:
        arr.append(word)
        counts.append(1)  # Initialize count
    else:
        #counts[arr.index(word)] += 1  # Increment count
        counts[arr.index(word)] += 1
        print(counts)

#print(list(zip(arr, counts)))  # Output as list of (word, count) pairs
#for word, count in zip(arr, counts):
# print(f"The word: '{word}' occurs '{count}' times.")
output = ", ".join([f"The word: '{word}' occurs '{count}' times" for word, count in zip(arr, counts)])
print(output)

'''
'''
for word in w:
    for i, (existing_word, count) in enumerate(arr):
        if existing_word == word:
            arr[i] = (existing_word, count + 1)  # Update count
            break
    else:
        arr.append((word, 1))  # Append new word with count 1

print(arr)

'''

'''
people = [
    {
        "name": "Alice Johnson",
        "age": 25,
        "occupation": "Software Engineer",
        "skills": ["Python", "Java", "SQL"],
        "location": "New York",
    },
    {
        "name": "Bob Smith",
        "age": 30,
        "occupation": "Data Scientist",
        "skills": ["Python", "R", "Machine Learning"],
        "location": "San Francisco",
    },
    {
        "name": "Charlie Davis",
        "age": 22,
        "occupation": "Cybersecurity Analyst",
        "skills": ["Networking", "Ethical Hacking", "Linux"],
        "location": "Austin",
    },
    {
        "name": "David Brown",
        "age": 28,
        "occupation": "Web Developer",
        "skills": ["HTML", "CSS", "JavaScript", "React"],
        "location": "Seattle",
    },
    {
        "name": "Emily White",
        "age": 35,
        "occupation": "IT Support Specialist",
        "skills": ["Windows", "Troubleshooting", "Networking"],
        "location": "Chicago",
    },
    {
        "name": "Franklin Green",
        "age": 40,
        "occupation": "Network Engineer",
        "skills": ["Cisco", "Routing", "Firewall"],
        "location": "Miami",
    },
    {
        "name": "Grace Adams",
        "age": 27,
        "occupation": "Cloud Engineer",
        "skills": ["AWS", "Azure", "Docker"],
        "location": "Boston",
    },
    {
        "name": "Henry Wilson",
        "age": 24,
        "occupation": "DevOps Engineer",
        "skills": ["CI/CD", "Kubernetes", "Terraform"],
        "location": "Denver",
    },
    {
        "name": "Ivy Turner",
        "age": 33,
        "occupation": "Database Administrator",
        "skills": ["MySQL", "PostgreSQL", "MongoDB"],
        "location": "Houston",
    },
    {
        "name": "Jake Martinez",
        "age": 29,
        "occupation": "AI Researcher",
        "skills": ["Deep Learning", "TensorFlow", "NLP"],
        "location": "Los Angeles",
    },
]

vowels = {"a", "e", "i", "o", "u"}  # Set of vowels

# List people in dict
for person in people:
    article = 'an' if person['occupation'][0].lower() in vowels else 'a'
    print(f"{person['name']} is {article} {person['occupation']} in {person['location']}")

# List unique skills    
unique_skills = set()
for person in people:
    unique_skills.update(person['skills'])
print(f"All unique skills: {unique_skills}")

# Find the oldest person
oldest = max(people, key = lambda p: p['age'])
print(f"The oldest person is {oldest['name']} who is {oldest['age']} years old")

# Filter people by occupation
software_engineers = [p for p in people if p['occupation'] == 'Software Engineer']
print('Software engineers', software_engineers)

# List of all cities
cities = {p['location'] for p in people}
print("Cities:", cities )
'''

'''

# Vending machine dictionary with item codes and prices
snacks = {
    "A1": 1.50, "A2": 2.00, "A3": 2.50,
    "B1": 1.75, "B2": 2.25, "B3": 3.00,
    "C1": 1.25, "C2": 2.50, "C3": 3.50
}

# Get the number of selections
dinput = int(input("Enter Val: "))
tcost = 0
arr = []

while len(arr) < dinput:
    dinput2 = input("Snack num: ").upper()
    
    if dinput2 in snacks:
        arr.append(dinput2)
        tcost += snacks[dinput2]

print(tcost)
'''
'''import os

# Task 1: Return the current working directory
def getCurrentDirectory():
    return os.getcwd()

print(getCurrentDirectory())

# Task 2: Return the directory name from the given file path
def getDirectoryName(fileName):
    return os.path.dirname(fileName)

print(getDirectoryName("/var/www/test.html"))
print(getDirectoryName("/var/www/apple/test.html"))

# Task 3: Return the file name from the given file path
def getFileName(fileName):
    return os.path.basename(fileName)

print(getFileName("/var/www/test.html"))
print(getFileName("/var/www/apple/names.txt"))

# Task 4: Create the specified file
def createFile(filename):
    with open(filename, 'w') as f:
        pass

createFile("test.txt")
print(os.path.exists("test.txt"))

# Task 5: Print all files in the given directory
def printFiles(someDirectory):
    for file in os.listdir(someDirectory):
        print(file)

printFiles(os.getcwd())

# Task 6: Identify if a path is a file, directory, or neither
def whatIsIt(somePath):
    if os.path.isdir(somePath):
        return "DIRECTORY"
    elif os.path.isfile(somePath):
        return "FILE"
    else:
        return "NEITHER"

print(whatIsIt(os.getcwd()))
print(whatIsIt(os.listdir(os.getcwd())[0])) 
print(whatIsIt("apple.pie.123.txt"))

# Task 7: Read and print the contents of a file
def printFileContents(filename):
    with open(filename, 'r') as f:
        print(f.read())

with open("test.txt", 'w') as f:
    f.write("Hello")

printFileContents("test.txt")

# Task 8: Append data to a file and print its contents
def appendAndPrint(filename, newData):
    with open(filename, 'a') as f:
        f.write("\n" + newData)
    printFileContents(filename)

with open("test.txt", 'w') as f:
    f.write("Hello")

appendAndPrint("test.txt", "World")
'''
'''
#filename = input().strip()

tv_shows  = {}

with open('Overwrite_File.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]
   
for i in range(0, len(lines), 2): #step through every 2 lines start, stop, step
    season_count = (lines[i].strip())
    show_title = lines[i+1].strip()
    
    if season_count not in tv_shows:
        tv_shows[season_count] = [] 
    tv_shows[season_count].append(show_title)
    
with open('output_keys.txt', 'w') as file:
    for season in sorted(tv_shows.keys()): # Sort keys by ascending
        file.write(f"{season}: {'; '.join(tv_shows[season])}\n")

all_shows = [] # Initialize empty string to store all show titles

for shows in tv_shows.values(): # For loop, iterate through each list of shows
    all_shows.extend(shows)
    print(all_shows) # Add all TV shows to a single list
        
with open('output_titles.txt', 'w') as file:
    for show in sorted(all_shows):  # Alphabetically sorted TV shows
        file.write(f"{show}\n")
'''  
    
'''
# Read input filename
filename = input().strip()

# Dictionary to store TV shows with season count as keys
tv_shows = {}

# Read the file and process the data
with open(filename, "r") as file:
    lines = file.readlines()

# Process the file contents into dictionary
for i in range(0, len(lines), 2):  # Step through every two lines (season, show)
    season_count = int(lines[i].strip())  # Convert season number to integer
    show_title = lines[i + 1].strip()  # Get the corresponding TV show title

    # Add the show to the dictionary under the correct season count
    if season_count not in tv_shows:
        tv_shows[season_count] = []
    tv_shows[season_count].append(show_title)

# **1️⃣ Write to `output_keys.txt` (Sorted by Number of Seasons)**
with open("output_keys.txt", "w") as file:
    for season in sorted(tv_shows.keys()):  # Sort by season count (ascending)
        file.write(f"{season}: {'; '.join(tv_shows[season])}\n")

# **2️⃣ Write to `output_titles.txt` (Sorted Alphabetically)**
all_shows = []
for shows in tv_shows.values():
    all_shows.extend(shows)  # Add all TV shows to a single list

# Sort the list alphabetically and write to file
with open("output_titles.txt", "w") as file:
    for show in sorted(all_shows):  # Alphabetically sorted TV shows
        file.write(f"{show}\n")
'''


'''
import numpy as np
import time

start_time = time.perf_counter()

total = np.sum(np.arange(1_000_000))

end_time = time.perf_counter()

#return ','.join(group)[::-1]
print(f"Execution Time: {end_time - start_time} seconds, value is {total:,}")
'''
'''
import math

def calcArea(radius):
    area = math.pi * (radius ** 2)
    return math.ceil(area), math.floor(area), round(area,2)


uInput = float(input("Enter Val: "))
print(f"The area of the circle is: between {calcArea(uInput)[1]} and {calcArea(uInput)[0]}, actual value being: {calcArea(uInput)[2]}")
'''
'''
import math

def quadratic_formula(a, b, c):
    """Computes the roots of a quadratic equation ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return (x1, x2)

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print(f'{prefix_str}{number:.0f}')
    else:
        print(f'{prefix_str}{number:.2f}')

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])

    solution = quadratic_formula(a, b, c)
    if solution:
        print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
        print_number(solution[0], 'x1 = ')
        print_number(solution[1], 'x2 = ')
    else:
        print("No real solutions")


# TODO: Import math module
import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    # TODO: Compute the quadratic formula results in variables x1 and x2
    return (x1, x2)
    

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print(f'{prefix_str}{number:.0f}')
    else:
        print(f'{prefix_str}{number:.2f}')
    

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    
    solution = quadratic_formula(a, b, c)
    print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
    print_number(solution[0], 'x1 = ')
    print_number(solution[1], 'x2 = ')
'''

'''# TODO: Import the random module
import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    random_number = random.randint(1, 100)
    # TODO: Compare parameter num to the random number
    if num < random_number:
        print(f"{num} is too low. Random number was {random_number}.")
    elif num > random_number:
        print(f"{num} is too high. Random number was {random_number}.")
    else:
        print(f"{num} is correct!")
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)
'''
'''
# TODO: Import the random module
import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    random_number = random.randint(1, 100)
    # TODO: Compare parameter num to the random number
    if num < random_number:
        print(f"{num} is too low. Random number was {random_number}.")
    elif num > random_number:
        print(f"{num} is too high. Random number was {random_number}.")
    else:
        print(f"{num} is correct!")
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)
'''
'''
import random

# Create a shuffled card deck with 4 suites of cards 2-10, and face cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

num_drawn = 0
game_over = False
user_input = input("Press any key to draw a card ('q' to quit): ")

while user_input != 'q' and not game_over:

    # Draw a random card, and remove card from the deck
    card = random.choice(deck)
    deck.remove(card)
    num_drawn += 1

    print('\nCard drawn:', card)

    # Game is over if an ace was drawn
    if card == 'A':
        game_over = True
    else:
        user_input = input("Press any key to draw a card ('q' to quit): ")

if user_input == 'q':
    print("\nGame was quit")
else:
    print(num_drawn, 'card(s) were drawn to find an ace.')

'''
'''
import smtplib
from email.mime.text import MIMEText

header = 'Hello. This is an automated email.\n\n'

def send(subject, to, frm, text):
    # The message to send
    msg = MIMEText(header + text)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = frm

    # Connect to gmail's email server and send
    s = smtplib.SMTP('smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login(user=frm, password='password')
    s.sendmail(frm, [to], msg.as_string())
    s.quit()

if __name__ == "__main__":
    send(
        subject='A coupon for you!',
        to='billgates@microsoft.com',
        frm='JohnnysHotDogs1@gmail.com',
        text='Enjoy!')
'''

'''
import urllib.request

def search(terms):
    """Do a fictional web engine search and return the results"""
    html = _send_request(terms)
    results = _get_results(html)
    return results

def _send_request(terms):
    """Send search to fictional web search engine and receive HTML response"""
    terms = terms.replace(' ', '%20')  #replace spaces
         
    url = 'http://www.search.fake.zybooks.com/search?q=' + terms
    info = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=info)
                  
    response = urllib.request.urlopen(req)
    html = str(response.read())
    return html

def _get_results(html):
    """
    Finds the links returned in 1st page of results.
    """
    start_tag = '<cite>'  # start of results
    end_tag = '</cite>'   # Results end with this tag
    links = []            # list of result links
                  
    start_tag_loc = html.find(start_tag)  # find 1st link
                     
    while start_tag_loc > -1:
        link_start = start_tag_loc + len(start_tag)
        link_end = html.find(end_tag, link_start)
        links.append(html[link_start:link_end])
        start_tag_loc = html.find(start_tag, link_end)

    return links

search_term  = input('Enter search terms: ')
result = search(search_term)

print(f'Found {len(result)} links:')
for link in result:
    print(' ', link)'''
'''
from hashlib import md5, sha1, sha256

text = input("Enter text to hash ('q' to quit): ")

while text != 'q':
    algorithm = input('Enter algorithm (md5/sha1/sha256): ')
    if algorithm == 'md5':
        output = md5(text.encode('utf-8'))
    elif algorithm == 'sha1':
        output = sha1(text.encode('utf-8'))
    elif algorithm == 'sha256':
        output = sha256(text.encode('ASCII'))
    else:
        output = 'Invalid algorithm selection'
    print('Hash value:', output.hexdigest())

    text = input("\nEnter text to hash ('q' to quit): ")
'''

'''
from matplotlib import pyplot as plt
import numpy as np

import math
x=np.arange(0, math.pi*2, 0.05)
y=np.sin(x)
plt.plot(x,y)

#Titles
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')

plt.show()
'''

'''
# Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message

    def __str__(self):
        return self.message  # Return exception message when printed


def find_ID(name, info):
    """Finds student ID by name or raises an exception if name is not found."""
    if name in info:
        return info[name]
    else:
        raise StudentInfoError(f"Student ID not found for {name}")
    
    
def find_name(ID, info):
    """Finds student name by ID or raises an exception if ID is not found."""
    for name, student_ID in info.items():
        if student_ID == ID:
            return name
    raise StudentInfoError(f"Student name not found for {ID}")
    # Type your code here.


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }
    
    userChoice = input()    # Read search option from user. 0: find_ID(), 1: find_name()
    
    # FIXME: find_ID() and find_name() may raise an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    try:
            
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)
    except StudentInfoError as e:
        print(e)
        
"""       
12.10 LAB: Student info not found - custom exception types
Given a main program that searches for the ID or the name of a student from a dictionary, complete the find_ID() and the find_name() functions that return the corresponding information of a student. Then, insert a try/except statement in main() to catch any exceptions raised by find_ID() or find_name(), and output the exception message. Each entry of the dictionary contains the name (key) and the ID (value) of a student.

Function find_ID() takes two parameters, a student's name and a dictionary. Function find_ID() returns the ID associated with the student's name if the name is in the dictionary. Otherwise, the function raises a custom exception type, StudentInfoError, with the message "Student ID not found for studentName", where studentName is the name of the student.

Function find_name() takes two parameters, a student's ID and a dictionary. Function find_name() returns the name associated with the student's ID if the ID is in the dictionary. Otherwise, the function raises a custom exception type, StudentInfoError, with the message "Student name not found for studentID", where studentID is the ID of the student.

The main program takes two inputs from a user: a user choice of finding the ID or the name of a student (int), and the ID or the name of a student (string). If the user choice is 0, find_ID() is invoked with the student's name as one of the arguments. If the user choice is 1, find_name() is invoked with the student's ID as one of the arguments. The main program finally outputs the result of the search or a message if an exception is caught.

Note: StudentInfoError is defined in the program as a custom exception type. StudentInfoError has an attribute to store an exception message.

Ex: If the input of the program is:
"""

'''

'''
# 9 Complete the function to return a dictionary using 
# list1 as the keys and list2 as the values
def createDict(list1, list2):
    return dict(zip(list1,list2))
        
# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}  
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))        
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))

# Work To Complete

# 10 Complete the function to return a dictionary value 
# if it exists or return Not Found if it doesn't exist
def findDictItem(mydict, key):
    if key in mydict:
        return mydict[key]
    else:
        return 'Not Found'
# Student code goes here
        
# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))


# 11 Complete the function to remove a dictionary item if it exists
def removeDictItem(mydict, key):
    if key in mydict:
        del mydict[key]
    return mydict
# Student code goes here
 
# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))


# Complete the function to print every key and value
def printDict(mydict):
    for key, value in mydict.items():
        print(key + '=' + value)
# Student code goes here
        
# expected output: 
#        tomato=red
#        banana=yellow
#        lime=green
printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})
 
# expected output: 
#        Brazil=Brasilia
#        Ireland=Dublin
#        Indonesia=Jakarta
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})


#COMPLETED WORK
# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
    if ascending:
        mylist.sort()
    else:
        mylist.sort(reverse=True)
    return mylist
    
    
# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))
 
# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))
'''

'''
# Complete the function to remove the third item in the given list
def removeThird(mylist):
    mylist.pop(2)
    return mylist
# Student code goes here
 
# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))
 
# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))

'''

'''
# Complete the function to remove the first item in the given list
def removeFirst(mylist):
    mylist.pop(0)
    return mylist
# Student code goes here
 
# expected output: [7, 8, 9]
print(removeFirst([6,7,8,9]))
 
# expected output: [2, 3, 4]
print(removeFirst([1,2,3,4]))

'''

'''
# Complete the function to return a new list containing 
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
    return mylist[:2] + mylist[-2:]
# Student code goes here
 
# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
 
# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))
'''

'''
# Complete the function to return the last two items in the given list
def getFirstTwo(mylist):
    return mylist[-2:]

 
# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))  
 
# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))
'''

'''
def get_num_of_characters(input_str):
    # Type your code here
    count = 0
    for char in input_str:
        count += 1
    return count

def output_no_whitestpace(input_str):
    modified_str = "".join(input_str.split())
    return modified_str

if __name__ == '__main__':
    # Type your code here
    user_input = input("Enter a sentence or phrase:\n")
    print(f"\nYou entered: {user_input}")
    
    # Step 2 and 3
    num_chars =  get_num_of_characters(user_input)
    print(f"\nNumber of characters: {num_chars}")
    
    modified_str = output_no_whitestpace(user_input)
    print(f"String with no whitespace: {modified_str}")
'''
'''
services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

base_price = 10
total = base_price
print("ZyCar Wash")
print(f"Base car wash -- ${base_price}")

if service_choice1 in services:
    print(f"{service_choice1} -- ${services[service_choice1]}")
    total += services[service_choice1]

if service_choice2 in services:
    print(f"{service_choice2} -- ${services[service_choice2]}")
    total += services[service_choice2]
    
print("----")
print(f"Total price: ${total}")
'''

'''
try:
    user_num = int(input())
    div_num = int(input())
    
    result = user_num // div_num
    print(result)
    
except ZeroDivisionError:
    print(f"Zero Division Exception: integer division or modulo by zero")
    
except ValueError as e:  
    print(f"Input Exception: invalid literal for int() with base 10: '{e}'")
    
    
try:
    user_num = int(input())
    div_num = int(input())

    result = user_num // div_num
    print(result)

except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")

except ValueError as e:
    print(f"Input Exception: {e}")
'''
'''
# Define your method here
def steps_to_miles(steps):
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    return steps / 2000  # Convert steps to miles

if __name__ == "__main__":
    # Read input
    steps = int(input())
    
    try:
        # Convert steps to miles and print the result formatted to 2 decimal places
        miles = steps_to_miles(steps)
        print(f"{miles:.2f}")
    
    except ValueError as e:
        print(e)  # Print exception message if steps are negative
'''
'''
synonyms = {}  # Define dictionary

# Get user input
word = input().strip()
letter = input().strip()

# Open the corresponding text file
filename = word + ".txt"
try:
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()  # Split the line into words
            if words:  # Ensure the line is not empty
                first_letter = words[0][0]  # Get first letter of the first word
                synonyms[first_letter] = words  # Store the words in dictionary

    # Check if the letter exists in the dictionary
    if letter in synonyms:
        for synonym in synonyms[letter]:
            print(synonym)
    else:
        print(f"No synonyms for {word} begin with {letter}.")

except FileNotFoundError:
    print(f"Error: {filename} not found.")

'''

'''
import csv

filename = input()
oout_str = ''
word_dict = {}

with open(filename, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    
    for row in reader:
        for word in row:
            word = word.strip()
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
for word in word_dict:              
    print(f'{word} {word_dict[word]}')
'''
'''
import csv


file_name = input()
movies = {}

with open(filename, r) as file:
    reader = csv.reader(file)
    for row in reader:
        showtime, title, rating = row[0], row[1], row[2]
        if title not in movies:
            movies[title] = {'rating': rating, 'showtimes': []}
        movies[title]['showtimes'].append(showtime)
        
# print output formatted
for title, details in movies.items():
    formatted_title = f"{title[:44]:<44}"  # Left-justified, limit 44 chars
    formatted_rating = f"{details['rating']:>5}" # Right justified
    formatted_showtimes = " ".join(details['showtimes']) # join showtimes
    print(f"{formatted_title} | {formatted_rating} | {formatted_showtimes}")
    
    
    
    import csv
'''
'''
grades = {
    "Alice": [90, 85, 88],
    "Bob": [78, 92, 80],
    "Charlie": [88, 76, 95]
}
arr = []
for student, scores in grades.items():
    #if (scores[1] > 90): print(scores[1])
    if student == 'Alice':
        for score in scores:
            arr.append(score)
        print(f"{student}: " + ", ".join([f"Grade # {i + 1}: {score}" for i, score in enumerate(sorted(grades['Alice'], reverse = True))]))
'''
'''
def display_menu():
    print("\nMENU") 
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")

def output_roster(team):
    """Outputs the team roster sorted by jersey number."""
    print("ROSTER")
    for jersey in sorted(team.keys()):
        print(f"Jersey number: {jersey}, Rating: {team[jersey]}")


def add_player(team):
    """Adds a new player to the roster."""
    jersey = int(input("\nEnter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    team[jersey] = rating  # Add to dictionary


def remove_player(team):
    """Removes a player from the roster."""
    jersey = int(input("\nEnter a jersey number:\n"))
    if jersey in team:
        del team[jersey]
    else:
        print("Player not found!")  # Optional message


def update_player_rating(team):
    """Updates a player's rating."""
    jersey = int(input("\nEnter a jersey number:\n"))
    if jersey in team:
        new_rating = int(input("Enter a new rating for player:\n"))
        team[jersey] = new_rating  # Update dictionary value
    else:
        print("Player not found!")  # Optional message


def output_above_rating(team):
    """Displays players with a rating above a given value."""
    rating = int(input("\nEnter a rating:\n"))
    print(f"\nABOVE {rating}")
    for jersey in sorted(team.keys()):
        if team[jersey] > rating:
            print(f"Jersey number: {jersey}, Rating: {team[jersey]}")


# ✅ Step 1: Initialize Dictionary and Get Input
team_roster = {}

for i in range(1, 6):  # Loop for 5 players
    jersey = int(input(f"Enter player {i}'s jersey number:\n"))
    rating = int(input(f"Enter player {i}'s rating:\n\n"))
    team_roster[jersey] = rating  # Store in dictionary

# ✅ Step 2: Output Initial Roster
output_roster(team_roster)

# ✅ Step 3: Display Menu and Process User Commands
while True:
    display_menu()  # ✅ Ensure this prints correctly
    choice = input("Choose an option:\n").strip().lower()

    if choice == 'o':
        output_roster(team_roster)
    elif choice == 'a':
        add_player(team_roster)
    elif choice == 'd':
        remove_player(team_roster)
    elif choice == 'u':
        update_player_rating(team_roster)
    elif choice == 'r':
        output_above_rating(team_roster)
    elif choice == 'q':
        break  # Quit program
    else:
        print("Invalid option! Please try again.")
'''
'''
# Step 0: Input values

nums = [int(n) for n in input().split()]


# Step 1: Find minimum and maximum values
# Type your code here.
min_val = min(nums)
max_val = max(nums)

print(f"Minimum: {min_val}\nMaximum: {max_val}")

# Step 2: Calculate mean
# Type your code here.
mean = sum(nums)/len(nums)
print(f"Mean: {mean:.1f}")

# Step 3: Check if palindrome
# Type your code here.
if nums == nums[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")
    

# Sort list
nums.sort()

# Step 4: Find and output median
# Type your code here.
n = len(nums)
if n % 2 == 1:
    median = nums[n //2] # Middle element for odd length
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) / 2 # Average of middle two for even length

print(f"Median: {median:.1f}")

# Step 5: Find and output mode
# Type your code here.
mode = nums[0]         # Stores the mode (most frequent number)
max_count = 1          # Tracks the highest frequency seen so far
current_num = nums[0]  # Tracks the current number being counted
current_count = 1      # Tracks how many times current_num appears consecutively

mode = max(nums, key = nums.count)
print(f"Mode: {mode}")




# Step 0: Input values
nums = [int(n) for n in input().split()]

# Step 1: Find minimum and maximum values
min_value = min(nums)
max_value = max(nums)
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")

# Step 2: Calculate mean
mean = sum(nums) / len(nums)
print(f"Mean: {mean:.1f}")

# Step 3: Check if palindrome
if nums == nums[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")

# Step 4: Find and output median
nums.sort()  # Sorting the list
n = len(nums)
if n % 2 == 1:
    median = nums[n // 2]  # Middle element for odd length
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) / 2  # Average of middle two for even length

print(f"Median: {median:.1f}")

# Step 5: Find and output mode
mode = nums[0]
max_count = 1
current_num = nums[0]
current_count = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        current_count += 1
    else:
        current_count = 1
        current_num = nums[i]

    if current_count > max_count:
        max_count = current_count
        mode = nums[i]

print(f"Mode: {mode}")

'''
'''
# Read input as a list of integers
user_values = list(map(int, input().split()))

# Always define user_vals
if len(user_values) > 1:
    user_vals = user_values[-1:] + user_values[1:-1] + user_values[:1]
else:
    user_vals = user_values  # Keep the same list if only one element

# Print output with spaces, ensuring a space after the last number
print(" ".join(map(str, user_vals)) + " ")

'''
'''
# num_count [] counts the number of occurrences for values 1-20 in the corresponding array index.
# Items in index 0 are ignored
num_count = [0] * 21  # Initialize a list of 21 0's for tallies

# Read input as space-separated integers
user_input = list(map(int, input().split()))

# Loop through the numbers and update the count, stopping at -1
for num in user_input:
    if num == -1:
        break  # Stop processing at -1
    if 1 <= num <= 20:  # Only count valid numbers in range 1-20
        num_count[num] += 1  # Increment count at index 'num'

# Find the mode (the number with the highest count)
mode = num_count.index(max(num_count))

# Print the mode
print(mode)


user_input = list(map(int, input().split()))

for num in user_input:
    if num == -1:
        break
    if 1 <= num <= 20:
        num_count[num] += 1
        
mode = num_count.index(max(num_count))

max_count = max(num_count)
modes = [i for i, count in enumerate(num_count) if count == max_count]
'''
'''def read_customer_data(filename):
    """Read and return data from filename as lists (names, states, debts)"""
    names, states, debts = [], [], []
    
    with open(filename) as f:
        for row in f:
            row = row.strip().split(',')
            names.append(row[0])
            states.append(row[1])
            debts.append(float(row[2]))
    
    return names, states, debts

# Main portion of the program
if __name__ == '__main__':
    # Read user input
    num_customers = int(input())
    debt_limit = int(input())
    search_phrase = input().strip()
    state_abbr = input().strip()
    
    # Read customer data from file
    names, states, debts = read_customer_data("CustomerData.csv")
    
    # Process the first `num_customers`
    selected_names = names[:num_customers]
    selected_debts = debts[:num_customers]
    selected_states = states[:num_customers]
    
    # Find the customer with the highest debt
    max_debt = max(selected_debts)
    highest_debt_name = selected_names[selected_debts.index(max_debt)]
    
    # Count customers whose names start with `search_phrase`
    name_count = sum(1 for name in selected_names if name.startswith(search_phrase))
    
    # Count customers with debt above `debt_limit` and those with no debt
    debt_above_limit = sum(1 for debt in selected_debts if debt > debt_limit)
    debt_free_count = sum(1 for debt in selected_debts if debt == 0)
    
    # Print the U.S. report
    print("U.S. Report")
    print(f"Customers: {num_customers}")
    print(f"Highest debt: {highest_debt_name}")
    print(f'Customer names that start with "{search_phrase}": {name_count}')
    print(f"Customers with debt over ${debt_limit}: {debt_above_limit}")
    print(f"Customers debt free: {debt_free_count}")
    
    # Process state-specific report
    state_customers = [i for i, state in enumerate(selected_states) if state == state_abbr]
    if state_customers:
        state_debts = [selected_debts[i] for i in state_customers]
        state_names = [selected_names[i] for i in state_customers]
        
        max_state_debt = max(state_debts)
        state_highest_debt_name = state_names[state_debts.index(max_state_debt)]
        state_name_count = sum(1 for name in state_names if name.startswith(search_phrase))
        state_debt_above_limit = sum(1 for debt in state_debts if debt > debt_limit)
        state_debt_free = sum(1 for debt in state_debts if debt == 0)
        
        print(f"\n{state_abbr} Report")
        print(f"Customers: {len(state_customers)}")
        print(f"Highest debt: {state_highest_debt_name}")
        print(f'Customer names that start with "{search_phrase}": {state_name_count}')
        print(f"Customers with debt over ${debt_limit}: {state_debt_above_limit}")
        print(f"Customers debt free: {state_debt_free}")



# Step 0: Input values

nums = [int(n) for n in input().split()]


# Step 1: Find minimum and maximum values
# Type your code here.
min_val = min(nums)
max_val = max(nums)

print(f"Minimum: {min_val}\nMaximum: {max_val}")

# Step 2: Calculate mean
# Type your code here.
mean = sum(nums)/len(nums)
print(f"Mean: {mean:.1f}")

# Step 3: Check if palindrome
# Type your code here.
if nums == nums[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")
    

# Sort list
nums.sort()

# Step 4: Find and output median
# Type your code here.
n = len(nums)
if n % 2 == 1:
    median = nums[n //2] # Middle element for odd length
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) / 2 # Average of middle two for even length

print(f"Median: {median:.1f}")

# Step 5: Find and output mode
# Type your code here.
mode = nums[0]         # Stores the mode (most frequent number)
max_count = 1          # Tracks the highest frequency seen so far
current_num = nums[0]  # Tracks the current number being counted
current_count = 1      # Tracks how many times current_num appears consecutively

mode = max(nums, key = nums.count)
print(f"Mode: {mode}")
'''
'''#filename =input().strip()
filename = 'WordTextFile1.txt'

with open(filename, "r") as file:
    words = file.read().splitlines()

sentence = " ".join(words)

with open(filename, 'a') as file:
    file.write(f"\n{sentence}")
    
with open(filename, 'r') as file:
    print(file.read())'''
    
'''
import csv

filename = "input1.csv"

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        row = [space.strip() for space in row]
        row_dict = dict(zip(row[::2], row[1::2]))
        print(row_dict)


with open(filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = [list(map(str.strip, row)) for row in reader]  # Strip leading/trailing spaces

    for row in rows:
        row_dict = {row[i]: row[i + 1] for i in range(0, len(row), 2)}  # Convert row into dictionary
        print(row_dict)  # Output each row as a dictionary

'''
'''
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

item_purchased = input().strip()
amount = int(input())

if item_purchased in purchase:
    if 10 <= amount <= 20:
        total_purchase_cost = (purchase[item_purchased] * amount) * .95
    elif amount >= 21:    
        total_purchase_cost = (purchase[item_purchased] * amount) * .90
    else:
        total_purchase_cost = purchase[item_purchased] * amount
   
print(f"{item_purchased} ${total_purchase_cost:.2f}")
'''

'''
import csv


filename = "WordTextFile1.txt"
arr = []

with open(filename,  'r') as file:
    reader = csv.reader(file)
    for lines in reader:
        cleaned = list(map(str.strip, lines))
        print("".join(cleaned))
        arr.extend(lines)
sentence = " ".join(arr)
print(sentence)
  
with open(filename, 'a') as file:
    file.write(sentence)
'''
'''
import csv 

filename = "input1.csv"

with open(filename, 'r') as file:
    reader = csv.reader(file)
    rows = [list(map(str.strip, row)) for row in reader]

    # Print each row separately
    for key in rows[0]:
        #print(key)
        dict_row = {rows[0][index]: rows[0][index + 1] for index in range(0, len(rows[0]), 2)}
    print(dict_row)
    for key in rows[1]:
        #print(key)
        dict_row2 = {rows[1][index]: rows[1][index + 1] for index in range(0, len(rows[1]), 2)}
    print(dict_row2)

    # Print each row, overlapping row_dict during printout  
    for item in rows:
        row_dict = {item[key]: item[key + 1] for key in range(0, len(item), 2)}
        print(row_dict)
        
'''