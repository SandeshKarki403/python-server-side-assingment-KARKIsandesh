import csv

# Write data
with open("main.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "marks"])
    for i in range(4):
        name = input("Enter student name: ")
        marks = int(input("Enter marks of the student: "))
        writer.writerow([name, marks])

# Read data
with open("main.csv", "r") as file:
    reader = csv.reader(file)
    main = list(reader)
    
    for row in main:
        print(row)

    print("If you want to have an average of the marks of students press 1")
    press = int(input("Enter 1: "))
    
    if press == 1:
        total = 0
        count = 0
        for row in main[1:]:
            if len(row) > 1: 
                total += int(row[1])
                count += 1
        average = total / count
        print("Average marks of students:", average)

                