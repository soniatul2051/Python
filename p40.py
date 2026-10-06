languages = ["Python", "Linux", "Automation", "Docker", "JavaScript"]


with open("output2.txt", "w") as file:
     for lang in languages:
        file.write(lang + "\n")
with open("output2.txt", "r") as file:
     lines = file.readlines()


for line in lines:
    if "o" in line:
         print(line.strip())
