import json

students = {
    "students": [
        {
            "name": "Atul",
            "age": 21,
            "course": "Python"
        },
        {
            "name": "Rahul",
            "age": 22,
            "course": "Java"
        },
        {
            "name": "Amit",
            "age": 20,
            "course": "Python"
        }
    ]
}

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
