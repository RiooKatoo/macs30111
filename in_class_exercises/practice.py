with open("names.txt", "w") as f:
    f.write("Rio Kato\n")
    f.write("Jenna Sun\n")
    f.write("Charlie Chi\n")
    f.write("Fay Guan\n")
    f.write("Reace Guy\n")


with open("names.txt", "a") as f:
    f.write("Rowan Wang\n")
    f.write("Bella Wang\n")


with open("names2.txt", "w") as file:
    print("Rio Kato", file=file)
    print("Jenna Sun", file=file)
    print("Charlie Chi", file=file)
    print("Fay Guan", file=file)

with open("names2.txt", "a") as file:
    print("Belllaaa", file=file)
    print("Doria", file=file)


import csv
import csv

# 1. csv.writer — write lists to a CSV file
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])  # Header
    writer.writerow(["Rio", 25])
    writer.writerow(["Jenna", 24])


# 2. csv.reader — read CSV rows as lists
with open("people.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    for row in reader:
        print(row)       # ['Rio', '25']
        print(row[0])    # Rio


# 3. csv.DictWriter — write dictionaries to a CSV file
with open("people_dict.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])

    writer.writeheader()  # Header
    writer.writerow({"name": "Rio", "age": 25})
    writer.writerow({"name": "Jenna", "age": 24})


# 4. csv.DictReader — read CSV rows as dictionaries
with open("people_dict.csv", "r", newline="") as file:
    reader = csv.DictReader(file)  # Uses the header as keys

    for row in reader:
        print(row)          # {'name': 'Rio', 'age': '25'}
        print(row["name"])  # Rio


# Create a practice file
with open("names_practice.txt", "w") as file:
    file.write("Rio\nJenna\nCharlie\nAnne\nMatthew\nAlex\n")


# Method 1: Skip the first 3 lines using next()
with open("names_practice.txt", "r") as file:
    next(file)  # Skip Rio
    next(file)  # Skip Jenna
    next(file)  # Skip Charlie

    remaining = file.readlines()

print("Method 1:", remaining)


# Method 2: Keep selected lines using enumerate()
selected = []

with open("names_practice.txt", "r") as file:
    for i, line in enumerate(file):
        if i > 2 and i < 5:  # Keep indexes 3 and 4
            selected.append(line.strip())

print("Method 2:", selected)




fruits = ["Apple", "Orange", "Pineapple", "Strawberry", "Orange"]
fruits.pop(2)

# print(result)
print(fruits)

nums = [1, 2, 3, 4, 5, 6]
result = ["even" if n % 2 == 0 else "odd" for n in nums]
print(result)
# ["odd", "even", "odd", "even"]