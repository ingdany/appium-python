import csv
import json


try:
    a = 1 / 1
    print(a)
except ZeroDivisionError:
    print("Cannot divisible by 0")
except TypeError:
    print("unsupported operand type(s) for /: str")
finally:
    print("Run")


with open("files/textfile.txt", "r") as file:
    text = file.read()
    print(text)


with open("files/textfile.txt", "a") as file:
    file.write("\nHi this is prasanth")


with open("files/test_csv.csv", mode="w", newline="") as file:
    csv_content = csv.writer(file)
    csv_content.writerow(["Name", "Age"])
    csv_content.writerow(["prasanht", "25"])
    csv_content.writerow(["ram", "24"])


with open("files/test_csv.csv", mode="r") as file:
    csv_content = csv.reader(file)
    for con in csv_content:
        print(con)


with open("files/test.json", "w") as file:
    data = {"name": "ram", "age": 24}
    json.dump(data, file)


with open("files/test.json", "r") as file:
    data = json.load(file)
    print(data)
