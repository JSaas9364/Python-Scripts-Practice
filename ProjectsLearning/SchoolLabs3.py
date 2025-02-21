grades = {
    "Alice": [90, 85, 88],
    "Bob": [78, 92, 80],
    "Charlie": [88, 76, 95]
}
arr = []
for student, scores in grades.items():
    if (scores[1] > 90): print(scores[1])
    if student == 'Alice':
        for score in scores:
            arr.append(score)
        print(f"{student}: " + ", ".join([f"Grade # {i + 1}: {score}" for i, score in enumerate(sorted(grades['Alice'], reverse = True))]))
# print(f"{student}: " + " ".join([f"Grade # {i + 1}: {score}" for i, score in enumerate(sorted(grades['Alice']))]))