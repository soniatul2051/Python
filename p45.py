import json

with open("students.json", "r") as file:
    data = json.load(file)


for student in data["students"]:
    if student["course"] == "Python":
       print(student["name"])
