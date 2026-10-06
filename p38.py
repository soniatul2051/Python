with open("data.txt","r") as file:
     lines = file.readlines()


for number, line in enumerate(lines, start=1):
    print(f"{number}:{line.strip()}")


