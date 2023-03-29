### File handling ###

import xml
import csv
import json
import os

# .txt file
txt_file = open("./file.txt", "r+")  # w+ -> write and r+ -> read
# txt_file.write("My name is Antony\nMy last name is Jordan\n30 age\nAnd my favorite language is Python")

print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.read())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAnd i like angular")
print(txt_file.readline())

txt_file.close()

with open("./file.txt", "a") as my_other_file:
    my_other_file.write("\nAnd too C#")

# os.remove("./file.txt")

# .json file
json_file = open("./file.json", "w+")
json_test = {
    "name": "Antony",
    "surname": "Jordan",
    "age": 30,
    "language": "English"
}

json.dump(json_test, json_file, indent=4)
json_file.close()

with open("./file.json") as my_other_json:
    for line in my_other_json.readlines():
        print(line)

json_dict = json.load(open("./file.json"))
print(json_dict)
print(json_dict["name"])

# .csv file
csv_file = open("./file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Antony", "Jordan", 30, "English"])
csv_writer.writerow(["Juan", "Valdez", 35, "Spanish"])
csv_file.close()

with open("./file.csv") as csv_other_file:
    for line in csv_other_file.readlines():
        print(line)

# .xlsx -> Installation a module
# xml files
