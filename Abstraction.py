class Car:
    def __init__(self):
        self.acc=False
        self.cluch=False
        self.brk=False
    def start(self):
        self.cluch=True
        self.acc=True
        print("Car started...")
Car1=Car()
Car1.start()