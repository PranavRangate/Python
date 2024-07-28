class Person:
    name = "pranav"
    age = "20"
    
class Student(Person):
    PRN = "22UAI104"
    
    def print_info(self):
        print("name = ",self.name)
        print("Age = ",self.age)
        print("PRN = ",self.PRN)
        
    
class AISA_club(Student):
    position = "precidant"
    
    def print_pos(self):
        print("position in AISA_club = ",self.position)
    
a1 = AISA_club()
a1.print_info()
a1.print_pos()