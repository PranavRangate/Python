class Perosn:
    name = "pranav"
    
    @classmethod
    def changename(cng,name):
        cng.name=name

p1 = Perosn()
print(p1.name)
p1.changename("Parth")
print(p1.name)