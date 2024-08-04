class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def address(self):
        return self._address

    def _get_private_data(self):
        return f"Name: {self._name}, Age: {self._age}, Address: {self._address}"

class Friend:
    def __init__(self, person):
        self.person = person

    def access_private_data(self):
        return self.person._get_private_data()

person = Person("Pranav", 20 , "123 Main St")

friend = Friend(person)

print(friend.access_private_data())
