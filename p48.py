import json

try:
    with open("studets.json", "r") as file:
         data = json.load(file)

         print(data)

except FileNotFoundError:
    print("students.json file nahi mili")

except json.JSONDecodeError:
    print("JSON file ka format invalid hai")
