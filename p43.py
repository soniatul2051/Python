import json

with open("student.json","r") as file:
         student = json.load(file)


print(student)


student["age"] = 21
student["city"] = "New York"


with open("student.json", "w") as file:
        json.dump(student, file, indent=4)

