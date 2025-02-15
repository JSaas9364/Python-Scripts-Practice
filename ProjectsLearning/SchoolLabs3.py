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