students = [1,2.11,32,"dfsd", "Foo bar","end","CoC"]

students[3] = "CoC"
students.extend(["end3","end4"])
# students.append("end3")
# students.append("end4")

students.insert(1, "New Value")
print(students)
# students.remove("New Value")
students.pop(1)
students.pop()
print(students)

if "CoC" in students:
    print("IN")

print(f" CoC is indexed at: {students.index("CoC")} ")

print(students.count("CoC"))

mynumber = [1,22,3,4] 

# mynumber.sort()
mynumber = sorted(mynumber)
print(mynumber)