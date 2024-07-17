list = ["hermione","harry","ron","draco"]
houses = ["gryffindor","gryffindor","gryffindor","slytherin"]
students = {
    "hermione": "gryffindor",
    "harry": "gryffindor",
    "ron": "gryffindor",
    "draco": "slytherin"
    }
#print(students["draco"])
for student in students:
    print(student,students[student], sep=", ")
