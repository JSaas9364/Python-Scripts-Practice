"""
Nested Loop...
5.  Specific Name example:
Create a dictionary with one key and a list of values for that one key. 
An example dictionary may look like the following:
    students = {
        "male": ["Tom", "Charlie", "Harry", "Frank"],
        "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }
Print out the dictionary values that contain an 'a'.
Sample Output:
Charlie, Harry, Frank, Sarah, Huda, Samantha, Elizabeth
All of those names contain an 'a' in it.
"""

students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for gender in students:
    for name in students[gender]:
        if 'a' in name:
            print(name)