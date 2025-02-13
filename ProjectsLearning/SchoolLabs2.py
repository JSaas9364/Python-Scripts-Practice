

#filename = input().strip()

tv_shows  = {}

with open('Overwrite_File.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

    
for i in range(0, len(lines), 1): #step through every 2 lines start, stop, step
    season_count = (lines[i].strip())
    show_title = lines[i+1].strip()
    print(show_title)
    
    
    
    
    
    
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