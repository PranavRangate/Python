class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class Student(Person):
    def __init__(self, PRN, name, age):
        self.PRN=PRN
        super().__init__(name, age)
    
s1 = Student("22UAI104","pranav",19)
print(s1.name)
print(s1.age)
print(s1.PRN)
