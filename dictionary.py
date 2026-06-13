sandesh = []

for i in range(3):
    name = input("Enter name: ")
    contact = int(input("Enter the age: "))
    roll = int(input("Enter your roll number: "))
    mark = input("Enter your grade: ")
    
    student = {
        "name": name,
        "roll": roll,
        "marks": mark,
        "contact": contact
    }
    sandesh.append(student)

print(sandesh)

print("Click 1 to search student and click 2 to display student")
option = int(input("Enter your number: "))

if option == 1:
    choice = int(input("Input the roll number of the student: "))
    for student in sandesh:
        if student["roll"] == choice:
            print("He is the bloody student", student["name"])
            break
    else:
        print("Something is wrong")

if option == 2:
    for student in sandesh:
        print(student)
