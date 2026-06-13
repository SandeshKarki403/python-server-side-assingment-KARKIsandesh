class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def show(self):
        print("Name is:", self.name)
        print("Roll is:", self.roll)
        print("Marks are:", self.marks)

obj = Student("Sandesh", 1, 67)
obj1 = Student("John", 2, 89)

obj.show()
obj1.show()
