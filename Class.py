class Student:
    def __init__(self, name, greet):
        self.name = name
        self.greet= greet
    

obj = Student("John ","says hi")

print(obj.name + obj.greet)