import copy

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

original_person = Person("Pranav", 20, "123 Main St")

shallow_copied_person = copy.copy(original_person)

deep_copied_person = copy.deepcopy(original_person)

original_person.display()
shallow_copied_person.display()
deep_copied_person.display()

shallow_copied_person.name = "Saptarshi"
shallow_copied_person.address = "456 Elm St"

deep_copied_person.name = "Amit"
deep_copied_person.address = "789 Pine St"

print("\nAfter modifying the shallow and deep copied persons:")
original_person.display()
shallow_copied_person.display()
deep_copied_person.display()
