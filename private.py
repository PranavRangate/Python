class person:
    __name="pranav"
    
    def __hello(self):
        print("Hello person!")
        
    def welcome(self):
        self.__hello()
        
p1=person()
p1.welcome()