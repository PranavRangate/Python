class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

    def copy_constructor(self):
        return Person(self.name, self.age, self.address)

original_person = Person("Pranav", 20, "123 Main St")

copied_person = original_person.copy_constructor()

original_person.display()
copied_person.display()

copied_person.name = "Saptarshi"
copied_person.address = "456 Elm St"
print("\nAfter modifying the copied person:")
original_person.display()
copied_person.display()
