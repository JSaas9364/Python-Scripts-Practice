# Exam Review Part 2

# Do those LABS
# Ch 2-14... all Labs!
# Ch 33 and 34... get to know the Prac Tests. Use them MORE than the Pre.

# Use Submit Mode and get them to 100%!!!
# PAY ATTENTION to the unit tests!
# ... then UNIT TEST more! Unit test, unit test, unit test!

# Last Week:
# Comp 1: Basic syntax and knowledge: operators, data types, etc
# Comp 2: Control Flow

# This Week...
# Data Types and Their Methods and Comp 3: Modules and Files

# STRINGS
# be able to refer by index, and to slice
# myStr = "abcdef"
# # slice[start:stop:step]
# revStr = myStr[::-1]
# print(revStr)

# KNOW YOUR WHITESPACE
# " " space from the spacebar
# a lot of variations in Unicode
# "\n" # new line return
# "\t" # tab
# "\r" # carriage return

# STRING METHODS
# print(dir(str)) # will show you them all
# myStr.format() # "Stuff I want to add into this string like {:.2f} and {}".format(var1, var2)
# myStr.strip() # input().strip()
# myStr.split() # returns a list of smaller strings
# myStr.join(listOfStrings) # ",".join(), " ".join(), "".join()
# myStr.replace(subStr, newStr) # "remove"... myStr = myStr.replace(subStr, "")
# myStr.index(subStr) # return the int index where this is found, raises error if not found
# myStr.find(subStr) # return the int index where this is found, return -1 if not found
# myStr.count(subStr) # return the int count of how many times that's there
# case methods: myStr.lower(), myStr.upper(), myStr.title(), myStr.capitalize()
# is/Boolean: myStr.islower(), myStr.isspace(), myStr.isupper(), myStr.isalpha(), myStr.isnumeric(), myStr.isdigit(), myStr.alnum()
# myStr.startswith(subStr), myStr.endswith(subStr)

# LISTS
# be able to refer by index and to slice

# LIST METHODS
# # +
# myList.append(item)
# myList.insert(i, item)
# myList.extend(anotherList)
# # -
# myList.pop(i)
# myList.remove(item) # pop() by index, remove() by value
# myList.clear()
# # "others"
# myList.index(item) # return index where item is, raises error if not there
# myList.sort() # no return
# myList.reverse() # no return
# myList.count(item) # return count of num occurrences
# myList.copy()

# DICT
# use the key like an index []... then you don't really need DICT methods
# myDict["someKey"] # get the value for that key
# myDict["someKey"] = value # assign a (new) value to key
#
# # membership check:
# if ___ in myDict: # looking at keys
# # membership check on values
# if ___ in myDict.values()
#
# # to get all keys in one object
# myDict.keys()

# MODULES
# math and csv

# MATH MODULE
# import math # FULL IMPORT
# math.factorial(x)
# math.ceil(x)
# math.floor(x)
# math.sqrt(x) # returns a float
# math.pow(x, y)
# math.fabs(x)
# math.pi
# math.e
#
# # PARTIAL IMPORT
# from math import sqrt # sqrt()
# from math floor, ceil # floor(), ceil()
# from math import * # still just ceil(), factorial(), e, etc
#
# # ALIAS IMPORT
# import math as m
# m.floor() # not math.floor()
#
#

# FILES
# mode: r, w, a

# READ MODE
# filename = input()
# with open() as f:
#     f.read() # returns one big string of the whole file
#     f.readlines() # returns a list of strings, line by line
#     f.readline() # ITERATOR... will return ONE ENTRY at time... for line in f.readline():
#     f.write(someStr) # write this str into the file

with open("test.txt", "r") as f:
    # contents = f.read()
    contents = f.readlines()
# print(contents)
# for line in contents:
#     line = line.strip()
#     print(line)
# print(contents)
# print(contents[4]) # 5th thing in the list from readlines()

import csv
# csv.reader() # ITERATOR... csv.reader(f), csv.reader(f, delimiter="\t")

with open("mock_data.csv", "r") as f: # mockaroo.com
    # 2 options with csv.reader()
    # Option 1 loop directly over it
    # for row in csv.reader(f):
    #     print(row)

    # Option 2 cheat... recast with list()
    contents = list(csv.reader(f))

    # Option 0 use readlines() instead
    # for row in f.readlines():
    #     row = row.strip().split(",")
    #     print(row)
# print(contents)
# for row in contents:
#     print(row)

# WRITE MODE
# write out a new file from the above for only rows with .co.uk email

# with open("output_data46.csv", "w") as f1:
#     for row in contents:
#         email = row[3]
#         if email.endswith("co.uk"):
#             f1.write(",".join(row) + "\n")

# APPEND MODE
# let's read so we can check that last line for a line return or not?
# with open("append_to_this.txt", "r") as f:
#     print(f.readlines()) # ['Frodo\n', 'Sam\n', 'Merry']
# with open("append_to_this.txt", "a") as f:
#     f.write("\nPippin")

###
# Pop Quiz
# How do you add to a list?... myList.append(item)
# How do you add to a dict?... myDict[key] = value
# How do you add to a str?...  myStr += "another string"
#
# In conclusion:
# Unit test!
# Unit test!
# Unit test!!!