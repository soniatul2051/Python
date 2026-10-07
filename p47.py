import json



with open("students.json", "r") as file:
     data = json.load(file)

for student in data["students"]:
    if student["name"] == "Neha":
       print("Already have data")
       break
else:
    data["students"].append({
    "name": "Neha",
    "age": 23,
    "course": "Python"
    })

with open("students.json", "w") as file:
     json.dump(data, file, indent = 4)
