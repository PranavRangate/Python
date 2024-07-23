class Student:
    
    def __init__(self):
        self.name="none"
    
    def __init__(self,nm):
        self.name=nm
        
    def welcome(self):
        print("welcome ",self.name)

S = Student("pranav")
S.welcome()