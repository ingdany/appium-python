# statement
age = 15
if age >= 18:
    print("eligible")
else:
    print("not eligible")


score = 75


if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C")


# loop
for i in range(10):
    print(i)


name = "ram"


# break
for i in name:
    if i == "a":
        break
    print(i)


# while
count = 0


while count < 5:
    count += 1  # count = count+1
    print(count)


# string
text = "Hi this is prasanth"


print(len(text))
print(text.count("is"))
print(text.lower())
print(text.upper())


print(text.replace("prasanth", "ram"))
names = text.split(" ")
print(names)
joins = ",".join(names)
print(joins)


print("H0" in text)
