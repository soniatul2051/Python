import json

with open("students.json", "r") as file:
    data = json.load(file)


for student in data["students"]:
    if student["course"] == "Python":
       student["age"] +=1
       print(student)


with open("students.json", "w") as file:
     json.dump(data, file, indent=4)
