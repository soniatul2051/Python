import json

student = {
    "name": "Atul",
    "age": 25,
    "course": "Python",
    "skills": ["Linux", "Docker", "Python"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
