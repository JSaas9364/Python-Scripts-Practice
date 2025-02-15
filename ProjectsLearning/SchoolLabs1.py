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